import re

with open("data/iocs.txt") as f:
iocs = [line.strip() for line in f]

ip_pattern = r"^\d+.\d+.\d+.\d+$"
hash_pattern = r"^[a-fA-F0-9]{32}$"
email_pattern = r"^[^@]+@[^@]+.[^@]+$"

print("IOC Risk Assessment")
print("=" * 50)

for ioc in iocs:

if re.match(hash_pattern, ioc):
    risk = "HIGH"

elif re.match(ip_pattern, ioc):
    risk = "MEDIUM"

elif re.match(email_pattern, ioc):
    risk = "MEDIUM"

elif "." in ioc:
    risk = "HIGH"

else:
    risk = "LOW"

print(f"{ioc} -> {risk}")



