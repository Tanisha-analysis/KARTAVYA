from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs
import hashlib
import hmac
import os
import secrets
import html
import logging
import oracledb

DB_USER = os.getenv("KARTAVYA_DB_USER", "YOUR_ORACLE_USERNAME")
DB_PASSWORD = os.getenv("KARTAVYA_DB_PASSWORD", "YOUR_ORACLE_PASSWORD")
DB_DSN = os.getenv("KARTAVYA_DB_DSN", "localhost:1521/XEPDB1")

HOST = "127.0.0.1"
PORT = 8000

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    """Open a connection to Oracle Database."""
    if DB_USER == "YOUR_ORACLE_USERNAME" or DB_PASSWORD == "YOUR_ORACLE_PASSWORD":
        raise RuntimeError(
            "Set KARTAVYA_DB_USER and KARTAVYA_DB_PASSWORD "
            "to your Oracle credentials before using database features."
        )

    return oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN,
    )


# ============================================================
# PASSWORD HASHING
# PBKDF2 with a unique random salt for each password.
# Existing SHA-256 hashes from an earlier version will not
# match this format; users may need to register again.
# ============================================================

def hash_password(password):
    salt = secrets.token_bytes(16)
    iterations = 600_000
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations,
    )
    return f"pbkdf2_sha256${iterations}${salt.hex()}${digest.hex()}"


def verify_password(password, stored_hash):
    """Verify a PBKDF2 hash; also recognises legacy SHA-256 hashes."""
    try:
        algorithm, iterations_text, salt_hex, digest_hex = stored_hash.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations_text)
        salt = bytes.fromhex(salt_hex)
        expected_digest = bytes.fromhex(digest_hex)
        actual_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations,
        )
        return hmac.compare_digest(actual_digest, expected_digest)
    except (ValueError, TypeError):
        # Compatibility with the earlier unsalted SHA-256 version.
        legacy_digest = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hmac.compare_digest(legacy_digest, stored_hash)


# ============================================================
# DATABASE HELPERS
# ============================================================

def execute_insert(sql, values):
    """Run an INSERT and always close the cursor and connection."""
    connection = None
    cursor = None