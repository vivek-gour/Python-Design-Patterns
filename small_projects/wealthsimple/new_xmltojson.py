from bs4 import BeautifulSoup

file_number = '3'

with open(f'doc/file{file_number}.xml', 'r') as file:
    xml_data = file.read()

soup = BeautifulSoup(xml_data, 'html.parser')

# Extracting values
values = []
for button in soup.find_all('button', {'type': 'button'}):
    company = button.find('p', class_='eyUkKu').text
    action = button.find('p', class_='yYvqz').text
    amount = button.find('p', class_='krkzdy').text
    status = button.find('span', class_='kXIyZE').text
    values.append({'company': company, 'action': action, 'amount': amount, 'status': status})

# Printing extracted values
for value in values:
    print(value)
