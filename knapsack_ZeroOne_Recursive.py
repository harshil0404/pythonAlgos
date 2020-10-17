def knapSack(val,wt,w,n):
    if(n == 0 or w == 0):
        return 0
    if(wt[n] > w):
        return knapSack(val,wt,w,n-1)
    else:
        case1 = knapSack(val,wt,w,n-1)
        case2 = val[n] + knapSack(val,wt,w - wt[n],n)
        # print(case1,"*",case2)
        return max(case1,case2)

val = [2,15,17,4]
wt =  [3,2,6,8]
w = 11
print(knapSack(val,wt,w,len(wt)-1))