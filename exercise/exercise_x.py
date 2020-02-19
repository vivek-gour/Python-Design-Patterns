__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Nike'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'vivek.gour@nike.com'
__status__ = 'development'


import ConfigParser
config = ConfigParser.RawConfigParser()

path = "D:/Users/vgour/PycharmProjects/python3_work/my_daggen/workflows/MyDAG_1/1_First_Job.sh"

config.read(path)
print(config.sections(), config.items('default'))
