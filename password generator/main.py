import random
import string

#ask user for password length
length = int(input("Enter the desired password length: "))

#define the characters we can use
characters = string.ascii_letters + string.digits + string.punctuation

#generate the password
password = ''.join(random.choice(characters) for _ in range(length))

#show the password
print("Your generated password is:", password)