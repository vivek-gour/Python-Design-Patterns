import requests

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key
api_key = 'G7NM1585HLQO0UBG'

# Replace 'AAPL' with the stock symbol you want to get the current value for
stock_symbol = 'SHOP.TO'

# Endpoint URL for getting the stock quote
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=15min&apikey={api_key}'
# Send a GET request to the Alpha Vantage API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    # Extract the latest stock price from the response
    latest_data = data['Time Series (1min)']
    latest_time = max(latest_data.keys())  # Get the most recent time
    current_price = latest_data[latest_time]['1. open']
    print(f"Current price of {stock_symbol}: ${current_price}")
else:
    print("Failed to fetch stock data. Status code:", response.status_code)