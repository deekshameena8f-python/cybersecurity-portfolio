# Security Log Analyzer
# Feature 1: Count failed login attempts
# Feature 2: Track failed login attempts by user
# Feature 3: Detect brute force attacks
# Feature 4: Generate security reports
#Final version

# Open the log file
with open("logs/sample.log") as f:
    logs = f.readlines()

# Counter for failed logins
failed = 0

# Dictionary to store user failures
attempts = {}

# Process each line
for line in logs:

    if "LOGIN_FAILED" in line:

        failed += 1

        # Username is last item in line
        user = line.split()[-1]

        attempts[user] = attempts.get(user, 0) + 1

suspicious_users = []

for user, count in attempts.items():

    if count >= 5:
        suspicious_users.append(user)

print("=" * 50)
print("SECURITY LOG ANALYZER")
print("=" * 50)

# Display total failures
print("Total Failed Logins:", failed)

print("\nFailed Login Attempts By User")

for user, count in attempts.items():
    print(user,':', count)

print("\nSuspicious Users")

if suspicious_users:

    for user in suspicious_users:
        print(user)

else:
    print("None")

with open("reports/report.txt", "w") as report:

    report.write("SECURITY REPORT\n")
    report.write("====================\n\n")

    report.write(f"Total Failed Logins: {failed}\n\n")

    report.write("Failed Attempts By User\n")

    for user, count in attempts.items():
        report.write(f"{user}: {count}\n")

    report.write("\nSuspicious Users\n")

    if suspicious_users:

        for user in suspicious_users:
            report.write(f"{user}\n")

    else:
        report.write("None\n")

print("\nReport saved to reports/report.txt")
