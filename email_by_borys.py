from itertools import count


def check_if_valid_email(email):
    is_valid = False
    if email.strip() == "":
        is_valid = False
        print("Your email is empty")
    elif len(email.strip()) < 10:
        is_valid = False
        print("Your email is too short")
    elif "@" not in email:
        print("Your email is missing @")
    elif "." not in email:
        print("Your email has no dots")
    elif " " in email:
        print("Your email has spaces")
    elif not email.rindex(".") > email.index("@"):
        print("Your email is invalid")
    elif  not email.isascii():
        print("Your email contains non English characters")
    elif "." not in email.split("@")[1]:
        print("Your domain has no dots")
    elif ".." in email:
        print("Your email can not have consecutive dots")
    elif email.count(".") < 3:
        print("Your emails looks not valid due to small amount of dots")
    else:
        is_valid = True
        print("Your email is valid")

    return is_valid


user_input = input("Enter your email: ")

res = check_if_valid_email(user_input)
