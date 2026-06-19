from src.baseline import load_baseline
from src.monitor import (
    check_integrity,
    detect_changes,
    detect_new_files,
    detect_deleted_files
)

from src.report import (
    generate_report,
    log_changes
)

baseline = load_baseline(
    "data/baseline.json"
)

current = check_integrity(
    "test_data",
    baseline
)

modified = detect_changes(
    current,
    baseline
)

new_files = detect_new_files(
    current,
    baseline
)

deleted = detect_deleted_files(
    current,
    baseline
)

all_events = (
    modified +
    new_files +
    deleted
)

log_changes(all_events)

generate_report(
    modified,
    new_files,
    deleted
)

print("Scan completed.")

import time

while True:

    current = check_integrity(
        "test_data",
        baseline
    )

    # analysis

    time.sleep(60)
