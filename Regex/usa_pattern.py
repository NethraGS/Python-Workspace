import re

pattern = r'^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$'

def is_valid_phone(number):
    return bool(re.match(pattern, number))

phones = [
    "123-456-7890",
    "(123) 456-7890",
    "123 456 7890",
    "123.456.7890",
    "+1 123-456-7890",
    "1234567890"
]

for phone in phones:
    print(phone, is_valid_phone(phone))
