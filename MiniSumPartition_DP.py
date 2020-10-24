a = [5,5.5,5,1]
memo = dict()
def minSumPart(n,setsum1 = 0, setsum2 = 0):
    if n < 0 :
        return abs(setsum1-setsum2)

    key = str(n)+":"+str(setsum1)

    if key not in memo:
        addin1 = minSumPart(n-1,setsum1+a[n],setsum2)
        addin2 = minSumPart(n-1,setsum1,setsum2+a[n])
        memo[key] =  min(addin1,addin2)

    return memo[key]

print(minSumPart(len(a)-1))
# minimum sum partition problem DP. Memoiztion Approach...