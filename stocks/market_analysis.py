import datetime

from sklearn.linear_model import LinearRegression
import yfinance as yf
from sklearn.model_selection import train_test_split

# Define the stock symbol and date range
stock_symbol = 'AAPL'
start_date = '2021-01-01'
end_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

# Download historical stock price data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

# Drop missing values
stock_data.dropna(inplace=True)

# Features (X) and target (y)
X = stock_data[['Open', 'High', 'Low', 'Volume']]
y = stock_data['Adj Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model's performance (you can use various metrics here)
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")