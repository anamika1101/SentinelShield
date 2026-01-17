# SentinelShield – Intrusion Detection & Web Protection System

## Overview
SentinelShield is an educational Python-based project that simulates the behavior of a
Web Application Firewall (WAF) and Intrusion Detection System (IDS). The system inspects
incoming requests, detects common web attacks, monitors abusive traffic behavior, and
logs security events for analysis.

This project is developed strictly for academic and ethical cybersecurity learning.

---

## Project Objectives
- Understand HTTP request inspection from a security perspective
- Detect common web attacks such as SQL Injection and XSS
- Implement rule-based attack detection
- Simulate rate limiting and behavior monitoring
- Generate security logs for analysis

---

## Features
- Simulated HTTP request inspection
- SQL Injection detection
- Cross-Site Scripting (XSS) detection
- Command Injection detection
- Directory Traversal detection
- Rate limiting based on IP behavior
- Security event logging with timestamps

---

## Technologies Used
- Python
- VS Code
- GitHub

---
SentinelShield/
│
├── main.py
├── rules.py
├── detector.py
├── rate_limiter.py
├── logger.py
├── logs/
│ └── security.log
└── screenshots/



---

## How to Run the Project
1. Clone or download the repository
2. Open the project folder in VS Code
3. Run the main file:

4. Enter IP address and request payload when prompted

---

## Sample Test Payloads
- Normal request: `hello world`
- SQL Injection: `' OR 1=1 --`
- XSS: `<script>alert(1)</script>`
- Directory Traversal: `../../etc/passwd`

---

## Output
- Normal requests are allowed
- Malicious requests are blocked
- Repeated requests from the same IP are rate-limited
- All events are logged in `logs/security.log`

---

## Disclaimer
This project is intended for educational and academic purposes only.
No malicious usage is intended.


## Project Structure
