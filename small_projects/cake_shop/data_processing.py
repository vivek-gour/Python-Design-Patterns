import json
import string
import os
import pandas as pd
from datetime import datetime, timedelta
import xlwings as xl

delivery_partner = ['zomato']

data = []


def get_s1_values(row):
    return {
        'payout_period': row[7].strip(),
        'total_payout': float(row[9].strip().replace('₹ ', '')),
        'store_name': row[1].strip(),
        'location': row[2].strip()
    }


def get_s2_values(row, year):
    return {
        'payout_on': f'{row[7].strip()} {year}',
        'total_orders': int(row[9].strip())
    }


def get_z_values(row):
    payout_period = row[1].strip()
    print(payout_period)
    payout_on = str(datetime.strptime(payout_period.split(' - ')[-1], '%d %b %Y') + timedelta(days=3))[:10]
    return {
        'payout_period': row[1].strip(),
        'total_payout': float(row[12]),
        'store_name': row[5].strip(),
        'location': row[6].strip(),
        'payout_on': payout_on,
        'total_orders': int(row[11])

    }


for del_part in delivery_partner:
    new_data = {'delivery_partner': '',
                'payout_period': '',
                'payout_on': '',
                'total_orders': '',
                'total_payout': '',
                'store_name': '',
                'location': '',
                'year': '',
                'file_name': ''}
    path = f'E:/Download_Folder/{del_part}'
    new_data['delivery_partner'] = del_part
    # year = '2021', '2022', '2023'
    for year in ['2022', '2023']:
        new_data['year'] = year
        for file_name in os.listdir(os.path.join(path, year)):
            new_data['file_name'] = file_name
            excel_file_path = os.path.join(path, year, file_name)
            print(excel_file_path)
            if '.xlsx' in file_name:
                book = xl.Book(excel_file_path)
                book.save()
                xls = pd.ExcelFile(excel_file_path)
            else:
                raise Exception('Xlsx file missing')
            df = pd.read_excel(xls, 'Summary')
            df.columns = [char for char in string.ascii_uppercase[:len(df.columns)]]
            df = df.fillna('').query('B != C').reset_index(drop=True)
            if del_part == 'swiggy':
                new_data.update(get_s1_values(df['B']))
                new_data.update(get_s2_values(df['C'], year))
            else:
                new_data.update(get_z_values(df['C']))

            data.append(new_data.copy())
final_df = pd.read_json(json.dumps(data)) 
final_df.to_csv('outputz.csv', index=False, sep='|')
# print(final_df)

# df = pd.read_excel(xls, 'Payout Invoice')
# print(df)
# df = pd.read_excel(xls, 'All Orders')
# print(df)
# df = pd.read_excel(xls, 'Discounts P&L')
# print(df)
