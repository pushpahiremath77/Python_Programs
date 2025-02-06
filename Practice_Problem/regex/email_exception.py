import re
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    if not re.match(pattern,email):
        raise InvalidEmailError(f"Invalid email:{email}")
    else:
        print(f"Valid email:{email}")

try:
    user_input = "test@invalid-email"
    validate_email(user_input)
except InvalidEmailError as e:
    print(f"Error:{e}")