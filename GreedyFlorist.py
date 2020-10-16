def getMinimumCost(k, c):
    summ = 0
    c = sorted(c)
    lenC = len(c)
    for i in range(lenC // k):
        summ+=(sum(c[len(c)-k::1])*(i+1))
        c = c[: len(c)-k :1]
    summ+=(sum(c)*(i+2))
    return summ

nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
minimumCost = getMinimumCost(k, c)
print(minimumCost)