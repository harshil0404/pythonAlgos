a = ['abcd','aabc','bd']
b = ['aaa','aa']
res = list()
for i in range(len(b)):
    t = 0
    for j in range(len(a)):
        if a[j].count(min(a[j])) < b[i].count(min(b[i])):
            t+=1
    res.append(t)  
print(res)
# https://leetcode.com/discuss/interview-question/352458/