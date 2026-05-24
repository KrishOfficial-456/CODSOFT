import random

print("----- PASSWORD GENERATOR -----")

# User input
length = int(input("Enter password length: "))

# Characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "@#$%&*"

password = random.choice(letters)
password += random.choice(numbers)
password += random.choice(special)

all_characters = letters + numbers + special

# Remaining characters
for i in range(length - 3):
    password += random.choice(all_characters)

print("\nGenerated Password:", password)