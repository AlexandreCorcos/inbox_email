# Color text to better result :)
YELLOW = "\033[93m"
LIGHT_BLUE = "\033[94m"
LIGHT_GREEN = "\033[92m"
LIGHT_PURPLE = "\033[95m"
RESET = "\033[0m"


# Created Email class (PEP8 say to not use parentheses in classes)
class Email:
    """Email class"""

    def __init__(self, email_address, subject_line, email_content):
        """
        Init an Email object.
        Args:
            email_address (str): The email address.
            subject_line (str): The subject line of the email.
            email_content (str): The content of the email.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """Marks the email as read."""
        self.has_been_read = True


# Empty list variable
inbox = []


def populate_inbox():
    """Populate the inbox with initial emails."""
    initial_list = [
        Email("hyperiondev@hyperiondev.com",
              "Welcome to HyperionDev!",
              "Hi there,\n\nWelcome to HyperionDev! We're thrilled "
              "to have you on board.\n\nBest regards,\nThe HyperionDev Team"),

        Email("john.smith@hyperiondev.com",
              "Great work on the bootcamp!",
              "Hello,\n\nCongratulations on your progress and "
              "completing the bootcamp!\n\nBest regards,\nJohn Smith"),

        Email("jane.doe@hyperiondev.com",
              "Your excellent marks!",
              "Dear student,\n\nCongratulations on achieving such "
              "outstanding marks in your courses!\n\nWarm regards,\nJane Doe")
    ]

    # Add sample emails to inbox
    inbox.extend(initial_list)


def list_emails():
    """List all email in the inbox."""
    unread_text = "All emails: "
    box_unread = len(unread_text) + 4
    print(f"\n{LIGHT_BLUE}{'-' * box_unread}")
    print(f"- {unread_text} -")
    print(f"{'-' * box_unread}{RESET}")
    if not inbox:
        print("Inbox is empty.")
    else:
        for k, email in enumerate(inbox):
            print(f"{k + 1}. {email.subject_line} {'(Unread)' if not email.has_been_read else ''}")


def details_email(email):
    """Show a specific email

    Args:
        email: The email object to shows details.
        """
    details_email = email.email_address
    details_subject = email.subject_line
    details_content = email.email_content

    print(f"\n{LIGHT_BLUE}{'-' * 50}")
    print(f"From: {details_email}")
    print(f"Subject: {details_subject}")
    print(f"{'-' * 50}")
    print(f"{details_content}")
    print(f"{'-' * 50}{RESET}")


def read_email(i):
    """
    Read an email and marks it as read if the user wants to

    Args:
        i (int): Email index to be read in the inbox
    """
    if 0 <= i < len(inbox):
        email = inbox[i]
        if not email.has_been_read:
            details_email(email)
            mark_read = input(f"{YELLOW}Do you want mark this email "
                              f"as read (Y/N)? {RESET}").strip().lower()
            if mark_read == "y":
                email.mark_as_read()
                print(f"\n>>> Email from {email.email_address} marked as read.\n")
            elif mark_read == "n":
                print(f"\n>>> Email not marked as read.\n")
            else:
                print("\nInvalid input. Email status unchanged.\n")
        else:
            details_email(email)
    else:
        print("Wrong number.")


populate_inbox()
while True:
    menu = input(f'''{LIGHT_PURPLE}\nSelect one of the following Options below:
    {YELLOW}1. {LIGHT_GREEN}List Emails
    {YELLOW}2. {LIGHT_GREEN}Read an Email
    {YELLOW}3. {LIGHT_GREEN}View Unread Emails
    {YELLOW}4. {LIGHT_GREEN}Quit the program
    : {RESET}''')

    if menu == "1":
        list_emails()
    elif menu == "2":
        try:
            list_emails()
            user_email_choose = int(input("Please choose which email you want to read: ")) - 1
            read_email(user_email_choose)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif menu == "3":
        unread_text = "Unread emails: "
        box_unread = len(unread_text) + 4
        print(f"\n{LIGHT_BLUE}{'-' * box_unread}")
        print(f"- {unread_text} -")
        print(f"{'-' * box_unread}{RESET}")
        for k, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{k + 1}. {email.subject_line}")
    elif menu == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please try again.")
