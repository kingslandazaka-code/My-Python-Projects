# import our libraries
import math

is_running = True

opt = ("add","subtraction","divide","multiplication","sqr","sqrt")
y_n = ("yes","no")

def add(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiplication(a,b):
    return a * b

def sqr(a):
    return a ** 2

def sqrt(a):
    return math.sqrt(a)
while is_running:
    operation = input(f"Enter the operation that you would like to perform {opt}:")

    while operation not in opt:
        print("invalid input")
        operation = input(f"Enter the operation that you would like to perform {opt}:")
    else:
        if operation == opt[0]:
            a1 = float(input("Enter your first figure: "))
            b1 = float(input("Enter your second figure: "))
            result_add = add(a1,b1)
            print(f"Your final answer is {result_add}")
        elif operation == opt[1]:
            a2 = float(input("Enter your first figure: "))
            b2 = float(input("Enter your second figure: "))
            subtraction(a2,b2)
            result_sub = subtraction(a2, b2)
            print(f"Your final answer is {result_sub}")
        elif operation == opt[2]:
            a3 = float(input("Enter your first figure: "))
            b3 = float(input("Enter your second figure: "))
            result_divide = divide(a3,b3)
            print(f"Your final answer is {result_divide}")
        elif operation == opt[3]:
            a4 = float(input("Enter your first figure: "))
            b4 = float(input("Enter your second figure: "))
            result_mult = multiplication(a4,b4)
            print(f"Your final answer is {result_mult}")
        elif operation == opt[4]:
            a_sqr = float(input("Enter the value that you want to square: "))
            result_sqr = sqr(a_sqr)
            print(f"Your final answer is {result_sqr}")
        else:
            a_sqrt = float(input("Enter the value that you want to square-root: "))
            result_sqrt = sqrt(a_sqrt)
            print(f"Your final answer is {result_sqrt}")

        do_you_wanna_go_again = input("Enter if you want to calculate(yes or no): ")
        while do_you_wanna_go_again not in y_n:
            print("ERROR")
            do_you_wanna_go_again = input("Identify if you want to calculate another somthing else(yes or no): ")

        else:
            if  do_you_wanna_go_again == y_n[1]:
                print("Thanks for using my calculator")
                is_running = False
            else:
                is_running = True

