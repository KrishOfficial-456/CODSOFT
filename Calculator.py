# Simple Calculator Program

print("----- SIMPLE CALCULATOR -----")

# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Operation choice
print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Percentage (%)(where a = part and b = Total)")

choice = input("Enter choice (1/2/3/4/5): ")

# Perform calculation
if choice == '1':
    addition = a + b
    print("Result =", addition)

elif choice == '2':
    subtraction = a - b
    print("Result =", subtraction)

elif choice == '3':
    multiply = a * b
    print("Result =", multiply)

elif choice == '4':
    if b != 0:
        division = a / b
        print("Result =", division)
    else:
        print("Division by zero is not possible!")

elif choice == '5':
    if (b == 0):
        print("Total Can't be Zero")
    elif ( a > b):
        print("Part must be less than Total")
    else:
        percentage = (a/b)*100
        print("Percentage = ", percentage , "%")

else:
    print("Invalid Choice!")