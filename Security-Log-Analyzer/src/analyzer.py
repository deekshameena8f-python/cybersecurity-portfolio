with open("logs/sample.log") as f:
    logs = f.readlines()

failed = 0

for line in logs:
    if "LOGIN_FAILED" in line:
        failed += 1

print("Failed Logins:", failed)
