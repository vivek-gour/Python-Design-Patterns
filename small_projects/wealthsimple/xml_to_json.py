from bs4 import BeautifulSoup
import pandas as pd

file_number = '3'

with open(f'doc/file{file_number}.xml', 'r') as file:
    xml_data = file.read()

soup = BeautifulSoup(xml_data, 'html.parser')

activities = soup.find_all('button', {'data-qa': 'wstrade-activity-list-item'})

trade_dict = []

for activity in activities:
    # print(activity)

    stock_name = activity.select_one('.eOAPRI').get_text(strip=True)
    trade_type = activity.select_one('.ilLkHf').get_text(strip=True)
    account, date = activity.select_one('.gelSrG').get_text(strip=True).split(' | ')
    result_or_value = activity.select_one('.fZXeiw').get_text(strip=True)

    trade_dict.append({'Stock_Name': stock_name,
                       'Trade_Type': trade_type,
                       'Account': account,
                       'Date': date,
                       'Result_Value': result_or_value})
    # print(f"Stock Name: {stock_name} | Trade Type: {trade_type} | Account : {account} | "
    #       f"Date : {date} | Result or Value: {result_or_value}")
    # break
    # print('-' * 20)

# print(trade_dict)

# Create a DataFrame from the JSON data
df = pd.DataFrame(trade_dict)

# Specify the CSV file path
csv_file_path = f'output{file_number}.csv'

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)
