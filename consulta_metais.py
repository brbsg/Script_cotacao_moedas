import requests

def consulta_ouro():
    api_key = "goldapi-4w65grlk0gl5jx-io"
    symbol = "XAU"
    curr = "USD"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        gold_price = data['price']
        return gold_price
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
    
    return None

def converte_dolar_peso_ouro(get_gold_price, dollars):
    gold_price = get_gold_price()
    grams_per_ounce = 31.1035
    ounces = dollars / gold_price
    grams = ounces * grams_per_ounce
    kilograms = grams / 1000
    return kilograms
