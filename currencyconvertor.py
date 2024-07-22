import requests

# Function to fetch exchange rates from fixer.io
def fetch_exchange_rates(base_currency, access_key):
    try:
        url = f"http://data.fixer.io/api/latest?access_key={access_key}&base={base_currency}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes

        data = response.json()
        if 'rates' in data:
            return data['rates']
        else:
            print(f"Error: 'rates' key not found in API response: {data}")
            return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None
    except Exception as err:
        print(f"Error occurred: {err}")
        return None

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency, access_key):
    try:
        rates = fetch_exchange_rates(from_currency, access_key)
        if rates and to_currency in rates:
            conversion_rate = rates[to_currency]
            converted_amount = amount * conversion_rate
            return converted_amount, conversion_rate
        else:
            print(f"Conversion rate not available for {from_currency} to {to_currency}")
            return None, None
    except Exception as err:
        print(f"Error occurred during conversion: {err}")
        return None, None

# Main function to handle user input and output
def main():
    access_key = 'YOUR_ACCESS_KEY'  # Replace with your fixer.io API access key
    print("Welcome to Currency Converter!")
    print("Available currencies: USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, and more...\n")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("From which currency (3-letter code, e.g., USD): ").upper()
    to_currency = input("To which currency (3-letter code, e.g., EUR): ").upper()

    converted_amount, conversion_rate = convert_currency(amount, from_currency, to_currency, access_key)

    if converted_amount is not None:
        print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        print(f"Conversion rate: 1 {from_currency} = {conversion_rate:.4f} {to_currency}")
    else:
        print(f"Sorry, the conversion from {from_currency} to {to_currency} is not available.")

if __name__ == "__main__":
    main()
