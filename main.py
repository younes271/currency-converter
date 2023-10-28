import requests

def convert_currency(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    currency_rate = data["rates"][to_currency]
    converted_amount = amount * currency_rate
    return converted_amount

amount = float(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(f"{amount} {from_currency} is equal to {convert_currency(amount, from_currency, to_currency)} {to_currency}")
