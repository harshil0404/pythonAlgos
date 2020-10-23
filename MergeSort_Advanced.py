a = [6,8,7,2,5,4]
h = len(a)-1
l = 0
print(a)
def mergesort(l,h):
    if l<h:
        m = int((l+h)/2)
        mergesort(l,m)
        mergesort(m+1,h)
        merge(a[l:m+1],a[m+1:h+1],l,h)
def merge(x,y,l,h):
    i = 0
    j = 0
    z = []
    while i<len(x) and j<len(y):
        if x[i] < y[j]:
            z.append(x[i])
            i+=1
        else:
            z.append(y[j])
            j+=1
    for i1 in range(i,len(x)):
        z.append(x[i1])
    for j1 in range(j,len(y)):
        z.append(y[j1])
    a[l:h+1] = z
mergesort(l,h)
print(a)
