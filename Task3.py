import random
import string

def generate_password(length, include_digits=True, include_symbols=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("--- Password Generator ---")

while True:
    length = int(input("Enter the desired length of the password: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if length <= 0:
        print("Invalid password length. Please enter a positive integer.")
    else:
        password = generate_password(length, include_digits, include_symbols)
        print(f"\nGenerated Password: {password}\n")

    choice = input("Generate another password? (y/n): ").lower()
    if choice != 'y':
        break

print("Thank you for using the Password Generator!")