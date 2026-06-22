# Mini SIEM Dashboard

## Overview

The Mini SIEM Dashboard is a simplified Security Information and Event Management (SIEM) system built in Python. The project collects and parses security logs, applies detection rules to identify suspicious activity, and presents findings through a lightweight dashboard.

The project demonstrates core Security Operations Center (SOC) concepts including log collection, event analysis, alert generation, and threat detection.

---

## Features

* Security log parsing
* Event normalization
* Rule-based threat detection
* Alert generation
* Dashboard visualization
* Unit testing
* Modular architecture

---

## Project Structure

mini-siem-dashboard/

├── logs/

│ └── sample.log

├── src/

│ ├── dashboard.py

│ ├── detector.py

│ └── parser.py

├── tests/

│ ├── test_detector.py

│ └── test_parser.py

├── screenshots/

├── .gitignore

├── README.md

└── requirements.txt

---

## Technologies Used

* Python
* Streamlit (if implemented)
* File Parsing
* Rule-Based Detection
* Unit Testing

---

## Workflow

1. Security logs are collected.
2. Log entries are parsed and normalized.
3. Detection rules analyze events.
4. Suspicious activities generate alerts.
5. Alerts are displayed in the dashboard.

---

## Detection Capabilities

### Failed Login Detection

Identifies repeated login failures that may indicate brute-force attacks.

### Suspicious Activity Detection

Flags predefined high-risk events within the logs.

### Event Monitoring

Provides visibility into security-related events.

---

## Testing

Unit tests are provided for:

* Log parser functionality
* Detection engine functionality

Example:

python -m unittest discover tests

---

## Screenshots

### Dashboard Overview

(Add screenshot)

### Parsed Log Events

(Add screenshot)

### Alert Generation

(Add screenshot)

### Detection Results

(Add screenshot)

---

## Future Improvements

* Real-time log ingestion
* Threat scoring
* Geolocation enrichment
* Elasticsearch integration
* Kibana dashboard support
* MITRE ATT&CK mapping

---

## Educational Objectives

This project demonstrates:

* SIEM Fundamentals
* Log Analysis
* Threat Detection
* Event Correlation
* SOC Workflows
* Security Monitoring

