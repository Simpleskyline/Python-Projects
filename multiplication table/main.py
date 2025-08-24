num = int(input("Enter a number: "))

print(f"\nMultiplication table of {num}\n")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")