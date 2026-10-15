# KARTAVYA – Python Backend

## Project Overview

KARTAVYA is an MCA mini-project focused on civic responsibility and community development. This repository contains the **Python backend code** developed for the project.

## Python Work Completed

The Python backend uses Python's built-in `http.server` module to handle browser requests and process submitted form data.

### Features Implemented in Python

1. **HTTP Server:** Starts a local web server to serve the homepage and other project files.
2. **Form Data Handling:** Receives POST requests and extracts submitted form values using `urllib.parse`.
3. **User Registration:** Processes registration details and checks whether the password and confirmation match.
4. **Login Verification:** Checks login credentials against stored user records in the Oracle database.
5. **Help Connect:** Processes requests for community assistance.
6. **Share & Reuse:** Processes details of reusable items submitted by users.
7. **Civic Voice:** Processes reports about local civic issues.
8. **Password Hashing:** Uses password hashing to avoid storing passwords as plain text.
9. **Oracle Database Integration:** Uses the `oracledb` Python driver to connect to Oracle and execute SQL statements.

*Note: Oracle connectivity and database operations require a correctly configured database and must be tested before they can be considered fully functional.*

## Technologies Used

- Python
- Python `http.server`
- `urllib.parse`
- `hashlib`
- `oracledb`
- Oracle SQL

## Python Libraries

- `http.server` – handles HTTP requests.
- `pathlib` – works with file paths.
- `urllib.parse` – parses submitted form data.
- `hashlib` – supports password hashing.
- `secrets` – generates secure random values.
- `oracledb` – connects Python to Oracle Database.

## How to Run

### 1. Install the Oracle driver

```bash
python -m pip install oracledb
```

### 2. Configure Oracle

Set the correct Oracle database username, password, and connection string in the Python configuration. Ensure the database service is running and the required tables exist.

Do not publish actual database credentials in the repository.

### 3. Start the server

```bash
python server.py
```

### 4. Open the application

```text
http://localhost:8000
```

## Current Status

The Python HTTP server and form-processing logic have been developed. The Oracle database connection currently requires configuration and verification. Complete database functionality has not yet been confirmed.

## Project Purpose

This work demonstrates Python backend programming, HTTP request handling, form processing, password hashing, SQL execution, and database connectivity for an academic MCA mini-project.

## Project Type

MCA Mini-Project — Python Backend Development

## Python Source Code

The main Python backend implementation is available here:

[**View server.py — KARTAVYA Python Backend**](./server.py)



