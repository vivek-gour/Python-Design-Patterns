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

from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

filez = ['0_1_Offer letter Searce.pdf',
         '0_2_searce releaving letter.pdf',
         '1_5136_PAYSLIP_MAR_2018.PDF',
         '2_5136_PAYSLIP_APR_2018.PDF',
         '3_5136_PaySlip_May_2018.pdf',
         'Citibank Account Statement_Mar 1 2018 to Mar 31 2018_1.pdf',
         'Citibank Account Statement_Apr 1 2018 to Apr 30 2018_1.pdf',
         'Citibank Account Statement_May 1 2018 to May 31 2018_1.pdf',
         '4_5136_FORM16_MAR_2019_updated.pdf',
         '5_Offer of Employment infosys.PDF',
         '6_DOJ Addendum.PDF',
         '7_Payslip_Nov-2020_1.pdf',
         '8_Payslip_Dec-2020_1.pdf',
         '9_Payslip_Jan-2021_1.pdf',
         'Statement_2020MTH11_290561967_nov_icici_1.pdf',
         'Statement_2020MTH12_290561967_dec_icici_1.pdf',
         'OpTransactionHistory31-01-2021_jan_icici.pdf',
         '10_infosys form 16 a.pdf',
         '11_infosys form 16 b.pdf',
         '12_Letter of reference.pdf']
path = "C:/Users/viv30/Desktop/Visa Docs/Vivek/"
for pdf in filez:
    merger.append(path + pdf)
merger.write(path + "offer letters relieving letter payslips and bank statement.pdf")
merger.close()
