a = [4,9,9]
for i in range(len(a)-1,-1,-1):
    a[i] += 1
    if a[i] < 10 :
        break
    else:
        a[i] = 0
        if i == 0 :
            a.insert(0,1)
print(a)