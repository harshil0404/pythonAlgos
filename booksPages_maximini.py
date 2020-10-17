def absSum(arr):
    maxi=[]
    for a in range(len(arr)-1):
        sum1 = sum2 = 0
        for j in range(0,a+1):
            sum1 = sum1 + arr[j]
        for k in range(a+1,len(arr)):
            sum2 = sum2 + arr[k]
        maxi.append(max(sum1,sum2))
    return min(maxi)
    
arr = [12, 34, 67, 90]
print(absSum(arr))

#https://www.geeksforgeeks.org/allocate-minimum-number-pages/