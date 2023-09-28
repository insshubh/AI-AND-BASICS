import requests
list_currency = {
    "AUD": "Australian Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Renminbi Yuan",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "GBP": "British Pound",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "ISK": "Icelandic Króna",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Złoty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "USD": "United States Dollar",
    "ZAR": "South African Rand"
}


all_values = list(list_currency.values())

for j, i in enumerate(all_values):
    print(j + 1, i)

print(end="\n\n")

# Define the indices you want to access
while(True):
   try:
      index_to_access = int(input("Select the Number From You Want To Convert The Currency: ")) - 1
      index_to_accessag = int(input("Select the Number You Want To Convert The Currency: ")) - 1
      break;
   except ValueError:
    print("Enter the Valid Input: ")
  

# Use the indices to access the corresponding keys
if 0 <= index_to_access < len(all_values) and 0 <= index_to_accessag < len(all_values):
    key_at_index = list(list_currency.keys())[index_to_access]
    key_at_indexag = list(list_currency.keys())[index_to_accessag]
else:
    print("Index out of range.")

amount = float(input("Enter the amount of money: "))

# Make sure to handle potential request errors
try:
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={key_at_index}&to={key_at_indexag}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data.get("rates", {}).get(key_at_indexag)
        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            print(f"{amount} {key_at_index} is {converted_amount} {key_at_indexag}")
            print(f"Exchanged Rate : {exchange_rate}")
        else:
            print("Exchange rate not found in the response.")
    else:
        print(f"Error: Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")




