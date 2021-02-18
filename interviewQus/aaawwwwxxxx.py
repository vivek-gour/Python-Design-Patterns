import re

a = "aaaawwwwwxxxxx"
b = set(a)
print(b)
string = ''
for i in b:
    x, y = re.subn(i, i, a)
    string = string + '%s%s' % (i, str(y))

print(string)
