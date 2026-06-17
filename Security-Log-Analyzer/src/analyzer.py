# Security Log Analyzer
# Feature 1: Count failed login attempts
# Feature 2: Track failed login attempts by user
# Feature 3: Detect brute force attacks
# Feature 4: Generate security reports

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

# Display total failures
print("Failed Logins:", failed)

print("\nFailed Login Attempts By User")

for user, count in attempts.items():
    print(user, count)

for user, count in attempts.items():

    if count >= 5:

        print("=" * 40)
        print("POTENTIAL BRUTE FORCE DETECTED")
        print("=" * 40)

        print("User:", user)
        print("Failed Attempts:", count)

# Create report
report = open("reports/report.txt", "w")

report.write("SECURITY REPORT\n")
report.write("----------------------\n\n")

report.write(f"Total Failed Logins: {failed}\n\n")

for user in suspicious_users:

    report.write(f"Suspicious User: {user}\n")

report.close()

print("\nReport Generated Successfully")



