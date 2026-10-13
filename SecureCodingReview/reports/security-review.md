# Secure Coding Review

## 1. Project Overview

This project demonstrates the identification of common security weaknesses in Python code and their remediation through secure coding practices.

## 2. Tools Used

- Python 3.13
- Bandit 1.9.4
- SQLite
- Git and GitHub

## 3. Vulnerability Identified

**Vulnerability:** Possible SQL Injection

**Tool:** Bandit

**Issue ID:** B608

**CWE:** CWE-89

**Severity:** Medium

**Confidence:** Low

The vulnerable application constructs an SQL query by concatenating user-supplied input directly into the query string. This can allow specially crafted input to alter the intended SQL query.

## 4. Remediation

The secure application uses parameterized SQL queries with placeholders instead of directly concatenating user input.

Additional security improvements include:

- Salted password hashing using Python's `hashlib.scrypt`.
- Constant-time password hash comparison using `hmac.compare_digest`.
- Password input hidden using `getpass`.
- Generic login failure messages.
- SQLite connection context managers.

## 5. Security Scan Results

| Application | Bandit result |
|---|---|
| `vulnerable_app.py` | 1 Medium-severity finding (B608) |
| `secure_app.py` | No issues identified |

## 6. Functional Testing

- User registration: Successful.
- Login with correct password: Successful.
- Login with incorrect password: Rejected.

## 7. Conclusion

The review identified a possible SQL injection vulnerability in the original application. The revised application uses parameterized queries and improved password-handling practices. Bandit reported no issues in the revised code during this scan.

A clean Bandit report does not guarantee complete security. Additional manual review and testing are recommended before production use.