import random
a = [1,2,3,4,5,6]
k = 3
tf = True
i = 0
j = len(a) - k # 3
req = list()
while tf :
    x = random.randint(i,j)
    req.append(a[x])
    rem = k - len(req)
    i = x+1
    j = len(a)-1-(rem-1)
    if len(req) == k:
        tf = False
print(req)