
weight = float(input(" Enter your weight: "))
unit = input("kilograms or pounds? (K or L)")

if unit == "k" :
    weight = weight * 2.205
    unit = "lbs."
elif unit == "L" :
    weight == weight / 2.205
    unit = "kgs."
else:
    print("{unit} is not valid")


print(f"Your weight is: {weight} {unit}")