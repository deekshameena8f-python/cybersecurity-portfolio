print("Password Security Auditor")
password = input("Enter a password: ")
length = len(password)
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

has_special = False
has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in special_characters:
        has_special = True

print("Password Length:", length)
print("Contains Uppercase:", has_upper)
print("Contains Lowercase:", has_lower)
print("Contains Digit:", has_digit)
print("Contains Special Character:", has_special)

