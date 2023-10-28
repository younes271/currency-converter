# currency-converter
A new repository created via Python script


---

Sure, here's a simple Python script for a currency converter:

```python
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
```

This script uses the ExchangeRate API to get the currency conversion rates. You will need to install the `requests` module using pip if you haven't already. You can do this by running `pip install requests` in your command line.

Please replace `"YOUR-API-KEY"` with your API key from ExchangeRate API. If you don't have an API key, you will need to sign up for a free account on their website. 

Also, please be aware that this code does not have any error checking. If the API request fails or the user enters invalid input, the program will crash. If you're using this code in a real application, you'll want to add error checking to handle these situations gracefully.