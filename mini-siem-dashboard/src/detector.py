# src/detector.py

def detect_alerts(logs):

    alerts = []

    for log in logs:

        if log["level"] == "ERROR":
            alerts.append(
                f"ALERT: {log['message']}"
            )

        if "Suspicious" in log["message"]:
            alerts.append(
                f"ALERT: {log['message']}"
            )

    return alerts
