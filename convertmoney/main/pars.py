import requests

url = 'https://v6.exchangerate-api.com/v6/d5c1360a20a1eb5fbaeafade/latest/USD'
response = requests.get(url)

def check_status():
    if response.status_code == 200:
        return True
    else:
        return False

def get_curr():
    if response.status_code == 200:
        data = response.json()
        conversion_rates = data.get('conversion_rates', {})
        
        currencies = list(conversion_rates.keys())
        choices = [(currency, currency) for currency in currencies]
        return choices
    else:
        return [("Currencies are not available", "Currencies are not available")]
    
def get_curr_value(curr):
    data = response.json()
    conversion_rates = data.get('conversion_rates', {})
        
    if curr in conversion_rates:
        return conversion_rates[curr]
    else:
        return 0  
