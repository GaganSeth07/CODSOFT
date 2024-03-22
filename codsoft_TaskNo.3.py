print("Welcome to Password Generator!!")

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    special_characters = "!@#$%&?/"
    characters += special_characters
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    
    length = int(input("Enter the desired length of the password: "))

    if length <= 0:
        print("Error: Password length must be a positive integer.")
        return

    password = generate_password(length)
    print("Generated Password:", password)

main()
