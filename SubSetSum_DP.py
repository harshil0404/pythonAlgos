a = [6,2,5,8]
x = 10
mem = dict()
def sss(s,i):
    key = str(s)+":"+str(i)
    if key in mem:
        return mem[key]
    if s == 0:
        return 1
    elif i < 0:
        return 0
    elif s < 0 :
        return 0
    elif s < a[i]:
        mem[key] = sss(s,i-1)
    else:
        mem[key] = sss(s,i-1)+sss(s-a[i],i-1)
    return mem[key]

print(sss(x,len(a)-1))
