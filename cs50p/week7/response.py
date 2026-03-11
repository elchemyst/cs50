from validator_collection import validators, errors

email = input("Email: ")

try:
    email_address = validators.email(email)
    print("Valid", end="")
except errors.EmptyValueError:
    print("Invalid", end="")
except errors.InvalidEmailError:
    print("Invalid", end="")