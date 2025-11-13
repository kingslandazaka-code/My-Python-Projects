# === Simple Calculator ===

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation: +, -, *, /")
    op = input("Enter operation: ")

    if op == '+':
        print("Result:", add(num1, num2))
    elif op == '-':
        print("Result:", subtract(num1, num2))
    elif op == '*':
        print("Result:", multiply(num1, num2))
    elif op == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")

calculator()
