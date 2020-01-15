__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Nike'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'vivek.gour@nike.com'
__status__ = 'development'


class employee():
    pay = 1.06

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def empName(self):
        return "%s.%s@company.com" % (self.first, self.last)

    def salaryPayout(self, payout):
        return self.pay * payout
