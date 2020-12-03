def minjumps(a,n) :
    if n > len(a)-1 or n == len(a) - 1: 
        return 0
    j = []
    for i in range(1,a[n]+1) :
        x = 1 + minjumps(a,n+i)
        j.append(x)
    mini = min(j)
    return mini
    

# a = [3,3,1,2,4,2,1]
a = [2,4,3,1,2,4,1]
print(minjumps(a,0))