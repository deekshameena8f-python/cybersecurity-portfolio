
import re

SUSPICIOUS_IPS = [
    "192.168.1.10",
    "10.0.0.5"
]

def detect_alerts(logs):

    alerts = []

    for log in logs:

        if log["level"] == "ERROR":
            alerts.append(
                f"ERROR ALERT: {log['message']}"
            )

        for ip in SUSPICIOUS_IPS:

            if ip in log["message"]:
                alerts.append(
                    f"IOC DETECTED: {ip}"
                )

    return alerts
