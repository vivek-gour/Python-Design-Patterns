# create function which add suffix for missing length
# suppose i want 8 len of string and if 5 len string come i make it 8 len


def convertString(string, length, char):
    if len(string) < length:
        return "%s%s" % (char * (length - len(string)), string)


a = 'Vivek'
b = 'Gour'


# print convertString(a, 8, '*')
# print convertString(b, 8, '*')

print a.rjust(8, '*')