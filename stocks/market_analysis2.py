import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
import datetime

# Define the stock symbol and date range
stock_symbol = 'BBD.TO'
start_date = '2021-01-01'
end_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

# Download historical stock price data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Use only the 'Adj Close' prices for prediction
data = stock_data['Adj Close'].values.reshape(-1, 1)

# Normalize the data using MinMaxScaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Split data into training and testing sets
train_size = int(len(data_scaled) * 0.8)
train_data, test_data = data_scaled[:train_size], data_scaled[train_size:]


# Create sequences for LSTM input
def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length])
        y.append(data[i + sequence_length])
    return np.array(X), np.array(y)


sequence_length = 10  # Number of previous days' prices to consider
X_train, y_train = create_sequences(train_data, sequence_length)
X_test, y_test = create_sequences(test_data, sequence_length)

# Build and train the LSTM model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(sequence_length, 1)),
    Dense(1)
])
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=2)

# Make predictions
predictions = model.predict(X_test)

# Inverse transform the predictions and actual values to original scale
predictions_inv = scaler.inverse_transform(predictions)
y_test_inv = scaler.inverse_transform(y_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test_inv, predictions_inv)
print(f"Mean Squared Error: {mse}")

# Extend the last `sequence_length` days from the test data
extended_sequence = test_data[-sequence_length:]

# Predict stock prices for the next 10 days
predicted_prices = []
for _ in range(10):
    # Reshape the sequence for prediction
    sequence = extended_sequence[-sequence_length:].reshape(1, sequence_length, 1)

    # Predict the next day's price and invert the scaling
    next_day_prediction = model.predict(sequence)
    next_day_prediction_inv = scaler.inverse_transform(next_day_prediction)

    # Add the predicted price to the list
    predicted_prices.append(next_day_prediction_inv[0, 0])

    # Update the extended sequence with the predicted price
    extended_sequence = np.concatenate((extended_sequence, next_day_prediction), axis=0)

# Print the predicted prices for the next 10 days
print("Predicted Prices for the Next 10 Days:")
for day, price in enumerate(predicted_prices, start=1):
    print(f"Day {day}: Predicted Price = {price:.2f}")

# # Plot the results
# plt.figure(figsize=(12, 6))
# plt.plot(y_test_inv, label='True Values')
# plt.plot(predictions_inv, label='Predictions')
# plt.legend()
# plt.title(f'{stock_symbol} Stock Price Prediction')
# plt.xlabel('Time')
# plt.ylabel('Stock Price')
# plt.show()

plt.figure(figsize=(12, 6))
plt.plot(y_test_inv, label='True Values')
plt.plot(predictions_inv, label='Previous Predictions', linestyle='dashed')
plt.plot(range(len(y_test_inv), len(y_test_inv) + 10), predicted_prices, label='Predicted Next 10 Days', color='green',
         linestyle='dotted')
plt.legend()
plt.title(f'{stock_symbol} Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.show()

# # Plot the results
# plt.figure(figsize=(12, 6))
# plt.plot(y_test_inv, label='True Values')
# plt.plot(predictions_inv, label='Previous Predictions', linestyle='dashed')
# plt.plot(range(len(y_test_inv), len(y_test_inv) + 10), predicted_prices, label='Predicted Next 10 Days', color='green', linestyle='dotted')
#
# # Display price values on the chart
# all_prices = np.concatenate((y_test_inv, predictions_inv, predicted_prices))
# plt.xticks(range(len(all_prices))[::20], all_prices[::20], rotation=45)
# plt.xlabel('Time')
# plt.ylabel('Stock Price')
# plt.legend()
# plt.title(f'{stock_symbol} Stock Price Prediction')
# plt.show()
