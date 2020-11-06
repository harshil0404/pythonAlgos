def stack(b):
    lst = []
    ob = ['(','[','{']
    cb = [')',']','}']
    for i in range(len(b)):
        if i==0:
            lst.append(b[i])
            continue
        else:
            x = b[i]
            if x in ob:
                lst.append(x)
            else:
                # print(ob.index(lst[-1]),x,cb.index(x))
                if ob.index(lst[-1]) == cb.index(x):
                    # print('ys',lst)
                    lst.pop()
                else:
                    break
    if not lst :
        print('yes')
    else:
        print('no')

brac = '([{(})])'
stack(brac)