import random
import string

# Function to generate a random password
def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

# Function to store and retrieve passwords
def password_manager():
    while True:
        # Ask the user what they want to do
        action = input("Do you want to (g)enerate a new password or (r)etrieve a stored password? ")

        # Generate a new password
        if action.lower() == 'g':
            length = int(input("Enter the desired length of the password: "))
            website = input("Enter the website/service the password is for: ")
            password = generate_password(length)
            print("The generated password is:", password)
            # Store the password in a dictionary
            passwords[website] = password
            print("Password stored for website/service:", website)

        # Retrieve a stored password
        elif action.lower() == 'r':
            website = input("Enter the website/service you want the password for: ")
            if website in passwords:
                print("The password for", website, "is:", passwords[website])
            else:
                print("No password found for website/service:", website)

        # Exit the program
        else:
            break

# Dictionary to store passwords
passwords = {}
password_manager()
