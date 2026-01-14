
import re

def validate_user_details(email, mobile, password):

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mobile_pattern = r'^[6-9]\d{9}$'
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if not re.match(email_pattern, email):
        raise ValueError("Invalid email address")

    if not re.match(mobile_pattern, mobile):
        raise ValueError("Invalid Indian mobile number")

    if not re.match(password_pattern, password):
        raise ValueError("Password must be strong")

    return "All details are valid"


try:
    print("User Registration Validation")

    email = input("Enter email: ")
    mobile = input("Enter mobile number: ")
    password = input("Enter password: ")

    result = validate_user_details(email, mobile, password)
    print(result)

except ValueError as ve:
    print("Validation Error:", ve)

else:
    print("User registered successfully")

finally:
    print("\n--- REGISTRATION PROCESS ENDED ---")



# import re

# text = input("Enter something: ")

# pattern = r'^\d+$'   # regex pattern

# if re.match(pattern, text):
#     print("Valid input: contains only digits")
# else:
#     print("Invalid input: contains letters or symbols")
