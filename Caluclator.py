# Simple Python Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculator():
    print("===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        else:
            result = divide(num1, num2)
            operator = "/"

        print(f"\n{num1} {operator} {num2} = {result}")


calculator()
