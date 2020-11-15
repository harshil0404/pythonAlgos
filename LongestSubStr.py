a = 'pwwkew'
s = ''
maxx = ''
s += a[0]
for i in range(1,len(a)):
    if a[i] in s :
        if len(s) > len(maxx):
            maxx = s
        s = a[i]
    else :
        s+=a[i]
print(maxx,' Length : ',len(maxx))
