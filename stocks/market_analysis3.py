import yfinance as yf
import numpy as np
import datetime


# Define the stock symbol and date range
stock_symbol = 'SHOP.TO'
start_date = '2023-12-01'
end_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

# Download historical stock price data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

print(stock_data)