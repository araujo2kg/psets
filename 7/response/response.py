import sys
from validator_collection import validators

def main():
    print(email_validation(input("What's your email?" )))

def email_validation(email):
    try:
        if email_check := validators.email(email):
            return "Valid"
        else:
            return "Invalid"
    except ValueError:
        print("Invalid")
        sys.exit()




if __name__ == "__main__":
    main()
