import math

def calculator():
    while True:
        # Get the user's choice of operation
        operation = input("Enter the operation you would like to perform (+, -, *, /, sqrt, %): ")

        # Get the numbers to perform the operation on
        if operation != "sqrt":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        elif operation == 'sqrt':
            result = math.sqrt(float(input("Enter the number for square root: ")))
        elif operation == '%':
            result = (num1*num2)/100
        else:
            print("Invalid operator. Please enter a valid operator.")
            continue

        # Print the result
        print("The result is:", result)

        # Asking to perform another operation
        again = input("Do you want to perform another operation? (y/n): ")
        if again.lower() == 'n':
            break

calculator()
