remind = []


def output(x, y):
    out = int(x) * int(y)
    if remind != []:
        out = out + remind[0]
    # remander, single digit
    return int(str(out)[:-1]) if str(out)[:-1] else 0, int(str(out)[-1])


final = []
for uval in str(12)[::-1]:
    out1 = []
    for bval in str(13)[::-1]:
        rem, out = output(uval, bval)
        remind = []
        if rem:
            remind.append(rem)
        out1.append(out)
    remind = []
    final.append(out1)

print final
for val in final:
    pass
