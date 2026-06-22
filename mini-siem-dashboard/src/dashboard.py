

import streamlit as st

from parser import parse_logs
from detector import detect_alerts

logs = parse_logs("logs/sample.log")

alerts = detect_alerts(logs)

st.title("Mini SIEM Dashboard")

st.header("Log Statistics")

total_logs = len(logs)

error_logs = len(
    [log for log in logs if log["level"] == "ERROR"]
)

warning_logs = len(
    [log for log in logs if log["level"] == "WARNING"]
)

st.metric("Total Logs", total_logs)
st.metric("Errors", error_logs)
st.metric("Warnings", warning_logs)

st.header("Alerts")

for alert in alerts:
    st.error(alert)

st.header("Raw Logs")

st.write(logs)
