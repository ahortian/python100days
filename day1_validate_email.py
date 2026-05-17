import re

def validate_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # If the email matches the regex, it's valid
    if re.match(regex, email):
        return True
    else:
        return False
    
if __name__ == "__main__":
    # Get user input for one or more email addresses
    user_input = input("Please enter email address(es), separated by commas or spaces: ")

    # Split on commas and whitespace, then remove empty entries
    emails = [email.strip() for email in re.split(r'[\s,]+', user_input) if email.strip()]

    if not emails:
        print("No email addresses were entered.")
    else:
        for email in emails:
            if validate_email(email):
                print(f"{email}: valid")
            else:
                print(f"{email}: invalid")