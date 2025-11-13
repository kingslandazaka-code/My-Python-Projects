# === Even or Odd Checker ===

def check_even_odd():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

check_even_odd()
