#prompt the user to key in value
num = int(input("Enter a number: "))

print(f"\nMultiplication table of {num}\n")

#for loop to repeat code 10 times
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")