a = [5,1,2,3,4,5]
#    0 1 2 3 4 5 6 
start = 0
end = len(a)-1
res = -1
while start <= end :
    mid = (start+end)//2
    prv = (mid + len(a) - 1)%len(a)
    nxt = (mid+1)%len(a) 
    if a[mid] < a[prv] and a[mid] < a[nxt] :
        res = mid
        break
    if a[0] <= a[mid]:
        start = mid+1
    elif a[mid] <= a[end]:
        end = mid-1
if res == -1 :
    res = len(a)
print(len(a)- res)
