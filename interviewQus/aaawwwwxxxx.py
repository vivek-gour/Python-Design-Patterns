import re

a = "aaaawwwwwxxxxx"
b = set(a)
string = ''
for i in b:
    x, y = re.subn(i, i, a)
    string += '%s%s' % (i, y)

print(string)

# ---------------------------

string_a = 'aaaabbcdddd'
res = ""
for item in string_a:
    if item not in res:
        res += '%s%s' % (item, string_a.count(item))
print(res)
