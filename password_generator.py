import random
import string

def generate_password(length, lowercase, uppercase, numbers, symbols):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase  # Adding uppercase characters
    if lowercase:
        characters += string.ascii_lowercase  # Adding lowercase characters
    if numbers:
        characters += string.digits  # Adding digits
    if symbols:
        characters += string.punctuation  # Adding punctuation (symbols)

    # Debugging: Print available characters including symbols
    print(f"Available characters: {characters}")
    
    if not characters:
        print("Error: No characters selected.")
        return None  # Return None if no characters are selected
    
    # Generate password by randomly choosing characters
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Input validation for length
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length must be a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Get user input for character types
uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Generate the password
password = generate_password(length, lowercase, uppercase, numbers, symbols)

# Display the generated password
if password:
    print(f"Generated password: {password}")
