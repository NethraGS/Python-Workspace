import re

text = input("Enter something: ")

pattern = r'^\d+$'   # regex pattern

if re.match(pattern, text):
    print("Valid input: contains only digits")
else:
    print("Invalid input: contains letters or symbols")