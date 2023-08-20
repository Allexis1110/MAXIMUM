#def strcounter(s):
#    for sym in s:
#        counter = 0
#        for sub_sym in s:
#            if sym == sub_sym:
#                counter += 1
#        print(sym, counter)

#strcounter('abca')


def strcounter(s):
    mydict = {}
    for sym in s:
        mydict[sym] = mydict.get(sym, 0) + 1

    for sym, count in mydict.items():
        print(sym, count)

strcounter('abca')
