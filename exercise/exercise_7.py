s1='aaaaxxxxbbb'
l1=list(s1)
finals = ''
for a in set(l1):
    finals = finals + '%s%s' % (a, l1.count(a))
print finals