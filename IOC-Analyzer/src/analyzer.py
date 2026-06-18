import re

with open("data/iocs.txt") as f:
iocs = [line.strip() for line in f]

ip_pattern = r"^\d+.\d+.\d+.\d+$"
hash_pattern = r"^[a-fA-F0-9]{32}$"
email_pattern = r"^[^@]+@[^@]+.[^@]+$"

counts = {
"IP": 0,
"Domain": 0,
"Hash": 0,
"Email": 0,
"Unknown": 0
}

for ioc in iocs:

```
if re.match(ip_pattern, ioc):
    counts["IP"] += 1

elif re.match(hash_pattern, ioc):
    counts["Hash"] += 1

elif re.match(email_pattern, ioc):
    counts["Email"] += 1

elif "." in ioc:
    counts["Domain"] += 1

else:
    counts["Unknown"] += 1
```

print("IOC Statistics")
print("=" * 40)

for category, count in counts.items():
print(category, ":", count)

