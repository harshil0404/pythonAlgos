a = 'bbcbbbc' # 13 ['b', 'b', 'c', 'b', 'b', 'b', 'c', 'bb', 'bbcbb', 'bcb', 'bb', 'bbb', 'bb']
# a = 'asasd' # 7
# a = 'abcbaba' # 10 ['a', 'b', 'c', 'b', 'a', 'b', 'a', 'bcb', 'bab', 'aba']
# a = 'aaaa' # 10 UNIQUE EDGE CASE...
res = list(a)
i = 0
j = min(1,len(a)-1)
tf = True
ind = []
while tf and j > 0 and j < len(a) : 
    if a[i] != a[j] :
        if ind :
            simi = len(ind)+1
            ele = a[ind[0]]
            if simi == a.count(ele,j,j+simi+1) :
                res.append(a[ind[0]-1 : j+simi+1])
            ind = []
        elif a[i] == a[min(j+1,len(a)-1)] : 
            res.append(a[i: j+2])
        j = i + 2
        i+=1
    elif a[i] == a[j]:
        res.append(a[i : j+1]) 
        ind.append(j)
        j+=1
    if j > len(a) :
        tf = False
x = 2
cnt = 0
while len(ind) >= x :
    cnt += (len(ind) - x + 1)
    x+=1
print(res,len(res)+cnt)
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
