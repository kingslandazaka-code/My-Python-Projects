# === Temperature Converter ===

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def converter():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        c = float(input("Enter Celsius: "))
        print("In Fahrenheit:", c_to_f(c))

    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        print("In Celsius:", f_to_c(f))

    elif choice == '3':
        c = float(input("Enter Celsius: "))
        print("In Kelvin:", c_to_k(c))

    elif choice == '4':
        k = float(input("Enter Kelvin: "))
        print("In Celsius:", k_to_c(k))

    else:
        print("Invalid choice!")

converter()
