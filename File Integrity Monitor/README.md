# File Integrity Monitor

## Overview

The File Integrity Monitor (FIM) is a cybersecurity tool designed to monitor files and directories for unauthorized modifications. The system creates a baseline of file hashes and continuously compares current file states against the baseline to detect file creation, modification, and deletion events.

This project demonstrates fundamental security monitoring concepts used in Host Intrusion Detection Systems (HIDS) and enterprise security solutions.

---

## Features

* SHA-256 file hashing
* Baseline creation and storage
* File modification detection
* New file detection
* File deletion detection
* Continuous monitoring loop
* Colorized console alerts
* CSV report generation
* Email alert support
* Log file generation

---

## Project Structure

File Integrity Monitor/

├── data/

│ ├── baseline.json

│ └── reports/

├── logs/

│ └── fim.log

├── src/

│ ├── **init**.py

│ ├── alerts.py

│ ├── baseline.py

│ ├── exports.py

│ ├── hash_utils.py

│ ├── monitor.py

│ ├── report.py

│ └── scanner.py

├── screenshots/

├── README.md

├── main.py

└── requirements.txt

---

## Technologies Used

* Python
* SHA-256 Hashing
* JSON
* CSV
* Colorama

---

## How It Works

1. A baseline of file hashes is generated.
2. Files are scanned periodically.
3. Current hashes are compared with baseline hashes.
4. Changes are identified.
5. Alerts and reports are generated.

---

## Screenshots

<img width="1920" height="1080" alt="Screenshot (926)" src="https://github.com/user-attachments/assets/a2a53b09-717d-49e3-a3ad-1ffe62fccc5d" />
<img width="1920" height="1080" alt="Screenshot (924)" src="https://github.com/user-attachments/assets/1d17eee6-a586-40f5-b0de-c25b78eefe69" />


---

## Future Improvements

* Real-time file monitoring
* Web dashboard
* Database storage
* Threat scoring
* SIEM integration

---

## Educational Objectives

This project demonstrates:

* File Integrity Monitoring
* Security Automation
* Incident Detection
* Log Management
* Cybersecurity Monitoring Workflows
