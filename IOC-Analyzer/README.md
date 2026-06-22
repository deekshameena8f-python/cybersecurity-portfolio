# IOC Analyzer

## Overview

The IOC Analyzer is a Python-based cybersecurity utility that analyzes Indicators of Compromise (IOCs) such as IP addresses, file hashes, and email addresses.

The project validates and categorizes IOCs using pattern matching techniques and generates structured reports.

---

## Features

* IP address identification
* MD5 hash identification
* Email address detection
* IOC categorization
* Report generation
* Automated analysis workflow

---

## Project Structure

IOC-Analyzer/

├── data/

│ └── iocs.txt

├── src/

│ └── analyzer.py

├── screenshots/

├── README.md

---

## Technologies Used

* Python
* Regular Expressions (Regex)
* Text Processing

---

## Supported IOC Types

### IP Addresses

Example:

192.168.1.1

### MD5 Hashes

Example:

5f4dcc3b5aa765d61d8327deb882cf99

### Email Addresses

Example:

[example@email.com](mailto:example@email.com)

---

## Workflow

1. Read IOC entries from file.
2. Analyze each indicator.
3. Identify indicator type.
4. Generate report.
5. Display results.

---

## Screenshots

### IOC Input File
### Analysis Results
### Generated Report
<img width="689" height="972" alt="Screenshot (722)" src="https://github.com/user-attachments/assets/f351cb80-f8ad-4a8d-bd1a-a4877e25b78a" />
<img width="685" height="968" alt="Screenshot (723)" src="https://github.com/user-attachments/assets/98df4450-64f8-4d31-9cb1-0cefb041e070" />



---

## Future Improvements

* Threat Intelligence API Integration
* URL Detection
* Domain Detection
* SHA-256 Support
* CSV Export

---

## Educational Objectives

This project demonstrates:

* IOC Analysis
* Threat Hunting Concepts
* Pattern Matching
* Security Automation
* Data Validation

