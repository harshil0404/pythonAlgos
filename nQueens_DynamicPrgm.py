import math
p = list()
def safe(r,c,p) :
    for i in range(len(p)-1):
        cr,cc = p[i]
        if cc==c :
            return False
        if math.fabs(r-cr) == math.fabs(c-cc):
            return False
    return True
def nQueens(p,n,r) :
    if r >= n :
        return True
    c = 0
    while c < n :
        p.append([r,c])
        if safe(r,c,p) and nQueens(p,n,r+1) :
            return True
        p.pop()
        c+=1
    return False
# n = 4 # true : [[0, 1], [1, 3], [2, 0], [3, 2]]
# n = 1 # true :[[0,0]] 
n = 2 # false : NotPossible
if(nQueens(p,n,0)):
    print(p)
else :
    print('NotPossible')
