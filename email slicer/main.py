email = input("Enter your email: ")

index = email.index(@)

username = email[:index]
domain = email[index + 1:]

print(f"Username: {username} \nDomain  :  {domain}")