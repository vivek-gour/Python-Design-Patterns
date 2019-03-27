__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@gmail.com'
__status__ = 'Learning'


try:
    "some code"
except NameError:
    print("error in name")
except Exception as e:
    print(e.message)
except (ValueError, AttributeError) as e:
    print(e.message)
else:
    print("If no error in try")
finally:
    print("always get call")

