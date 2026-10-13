# Secure Coding Review



## Project Overview



This project demonstrates secure coding practices by identifying a possible SQL injection vulnerability in a Python application and improving the code to reduce the risk.



## Objectives



- Identify a potential SQL injection vulnerability.

- Scan Python code using Bandit.

- Replace unsafe SQL query construction with parameterized queries.

- Improve password storage and login handling.

- Compare vulnerable and revised application scan results.



## Technologies Used



- Python 3.13

- SQLite

- Bandit 1.9.4

- Git and GitHub



## Project Files



- `vulnerable_app.py` — Demonstrates unsafe SQL query construction.

- `secure_app.py` — Uses parameterized SQL queries and salted password hashing.

- `requirements.txt` — Lists the required security scanning tool.

- `reports/bandit-report.txt` — Bandit scan report for the vulnerable application.

- `reports/security-review.md` — Security findings, remediation, and test results.

- `reports/secure-report.txt` — Intended report file for the secure application scan.



## Installation



Install the dependencies:



```bash

python -m pip install -r requirements.txt

```



## Run the Applications



Run the vulnerable demonstration:



```bash

python vulnerable_app.py

```



Run the secure login demonstration:



```bash

python secure_app.py

```



The secure application lets you register a username and password, then test login with the correct or an incorrect password.



## Security Scanning



Scan the vulnerable application:



```bash

python -m bandit -r vulnerable_app.py -f txt -o reports/bandit-report.txt

```



Scan the secure application:



```bash

python -m bandit -r secure_app.py -f txt -o reports/secure-report.txt

```



Display the reports:



```bash

cat reports/bandit-report.txt

cat reports/secure-report.txt

```



## Findings



The vulnerable application produced a Bandit B608 finding for a possible SQL injection vector, rated Medium severity with Low confidence.



The secure application scan reported no issues identified. The revised code uses parameterized queries, salted password hashing with `hashlib.scrypt`, and constant-time hash comparison with `hmac.compare_digest`.



## Testing



- Registration: Successful.

- Login with the correct password: Successful.

- Login with an incorrect password: Rejected.



## Disclaimer



This project is an educational demonstration. A clean Bandit report does not guarantee complete security. Additional manual review and testing are recommended before production use.

