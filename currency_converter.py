# === Simple Currency Converter ===

def currency_converter():
    # Example exchange rates
    rates = {"USD": 1, "EUR": 0.9, "NGN": 460, "GBP": 0.8}
    print("Available currencies:", ", ".join(rates.keys()))
    amount = float(input("Enter amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    if from_currency in rates and to_currency in rates:
        converted = amount / rates[from_currency] * rates[to_currency]
        print(amount, from_currency, "=", converted, to_currency)
    else:
        print("Invalid currency.")

currency_converter()
