# a, b = 125, 25
# bs = str(25)
# b1, b2 = b - int(bs[1]), int(bs[1])
#
# a1out = a * b1
# a2out = a * b2
#
# output = a1out + a2out
#
# print output


# remind = []
#
#
# def output(x, y):
#     out = int(x) * int(y)
#     if remind != []:
#         out = out + remind[0]
#     # remander, single digit
#     return int(str(out)[:-1]) if str(out)[:-1] else 0, int(str(out)[-1])
#
#
# final = []
# for uval in str(25)[::-1]:
#     out1 = []
#     for bval in str(125)[::-1]:
#         rem, out = output(uval, bval)
#         remind = []
#         if rem:
#             remind.append(rem)
#         out1.append(out)
#     remind = []
#     final.append(out1)
#
# print final


# import pandas as pd
#
# from collections import Counter
# a = "aaabbccc"
# print(set(list(a)))
# print(Counter(a))
# final_string = ''
# for s in set(list(a)):
#     final_string += '%s%s' % (s, str(Counter(a).get(s)))
#
# print(final_string)

# from PyPDF2 import PdfFileMerger
#
# merger = PdfFileMerger()
#
# filez = ['0_1_Offer letter Searce.pdf',
#          '0_2_searce releaving letter.pdf',
#          '1_5136_PAYSLIP_MAR_2018.PDF',
#          '2_5136_PAYSLIP_APR_2018.PDF',
#          '3_5136_PaySlip_May_2018.pdf',
#          'Citibank Account Statement_Mar 1 2018 to Mar 31 2018_1.pdf',
#          'Citibank Account Statement_Apr 1 2018 to Apr 30 2018_1.pdf',
#          'Citibank Account Statement_May 1 2018 to May 31 2018_1.pdf',
#          '4_5136_FORM16_MAR_2019_updated.pdf',
#          '5_Offer of Employment infosys.PDF',
#          '6_DOJ Addendum.PDF',
#          '7_Payslip_Nov-2020_1.pdf',
#          '8_Payslip_Dec-2020_1.pdf',
#          '9_Payslip_Jan-2021_1.pdf',
#          'Statement_2020MTH11_290561967_nov_icici_1.pdf',
#          'Statement_2020MTH12_290561967_dec_icici_1.pdf',
#          'OpTransactionHistory31-01-2021_jan_icici.pdf',
#          '10_infosys form 16 a.pdf',
#          '11_infosys form 16 b.pdf',
#          '12_Letter of reference.pdf']
# path = "C:/Users/viv30/Desktop/Visa Docs/Vivek/"
# for pdf in filez:
#     merger.append(path + pdf)
# merger.write(path + "offer letters relieving letter payslips and bank statement.pdf")
# merger.close()
#
# stringa = 'as_asf'
#
# print(stringa.split(' '))

# def asc():
#     return '' if 'sh' not in ['sh', ] else print('continue')
#     print('its present')
#
# asc()
# import time
# from datetime import datetime
# testtime = datetime.now().strftime("%d_%m_%H_%M")
# print(testtime)
# import os
# path = os.path.join(os.getcwd(), "images/Task3/1.png")
# print(path)

# import random
# for i in range(1000):
#     val = random.randrange(1, 11)
#     print(val)
#     if val == 11:
#         print(random.randrange(1, 11))

# name = 'vivek.flac'
# print(name.replace('flac', 'txt'))

text = """"Dear SuperMarket Manager,

I hope this letter finds you well. My name is Vivek Gour, and I am a regular customer at your esteemed supermarket. I am writing to bring to your attention an unfortunate accident that occurred recently during one of my visits and to offer some suggestions on how such incidents can be prevented in the future.

On my last visit while shopping in your store, I witnessed an incident that deeply concerned me. A customer slipped and fell near the entrance due to a wet floor, resulting in minor injuries. As an observant bystander, I immediately reported the incident to your staff, and they promptly attended to the injured individual, providing the necessary assistance.

While I understand that accidents can happen even with the utmost care, I believe there are measures that can be put in place to reduce the risk and ensure the safety of customers and staff alike. Here are some suggestions to prevent such incidents in the future:

Regular Floor Inspections: Implement a strict schedule for your staff to inspect and clean the floors at regular intervals throughout the day, especially during peak hours. This will help identify and address potential hazards promptly.

Cautionary Signage: Clearly display warning signs at areas where the floor might be wet or slippery, such as near the entrance during rainy weather or around spill-prone sections like the produce or beverage aisles.

I believe that implementing these preventive measures will not only improve the safety of your supermarket but also enhance the overall shopping experience for your valued customers. Additionally, it will demonstrate your commitment to providing a secure environment for all who enter your store.

I appreciate your attention to this matter and hope you will consider my suggestions seriously. If you would like to discuss this further or if there is anything else I can do to assist with this initiative, please do not hesitate to contact me.

Thank you for your time and dedication to ensuring the safety of your patrons. I look forward to witnessing positive changes in your supermarket and continuing to be a satisfied customer.

Sincerely,
Vivek
"""

# count = text.split(' ')
# print(count)
# print(len(count))
# import random
#
# num_list = ['11', '9', '10', '12', '4', '0', '3', '5', '9', '2', '8', '5', '6', '11', '6', '4', '8', '10', '3']
# # print(num_list[1])
# # random.shuffle(num_list)
# rule_book = {0: [1, 3, 4],
#              1: [2, 4, 5],
#              2: [5, 6],
#              3: [4, 7, 8],
#              4: [5, 8, 9],
#              5: [6, 9, 10],
#              6: [10, 11],
#              7: [8, 12],
#              8: [9, 12, 13],
#              9: [10, 13, 14],
#              10: [11, 14, 15],
#              11: [15],
#              12: [15, 16],
#              13: [14, 16, 17],
#              14: [15, 17, 18],
#              15: [18],
#              16: [17],
#              17: [18]
#              }
# safe_num_pos = []
# not_safe_num = []
# for key, val in rule_book.items():
#     tempList = [num_list[v] for v in val]
#     if num_list[key] in ['6', '8'] and ('6' in tempList or '8' in tempList):
#         not_safe_num.append(key)
#     else:
#         safe_num_pos.append(key)
# print(num_list, safe_num_pos, not_safe_num)

# def abc(x):
#     for z in range(10):
#         print('here')
#         if z == x:
#             return z
#     else:
#         print('There was no number that was matching to %d' % x)
#         return 'N/A'
#
#
# print(abc(15))

# print('.com.in'.replace('.com', 'comdone').replace('.in', 'indone'))

# new_data = {'delivery_partner': '',
#             'payout_period': '',
#             'payout_on': '',
#             'total_orders': '',
#             'total_payout': '',
#             'store_name': '',
#             'location': '',
#             'year': ''}
# new_data['delivery_partner'] = 'vivek'

# print(range('A', 'D'))


def addition(x, y):
    return x + y

