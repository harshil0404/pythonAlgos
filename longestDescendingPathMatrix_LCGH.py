def doLess(a,i,j,ce,x) :
    li = len(a)-1
    lj = len(a[0])-1
    if i < 0 or i > li or j < 0 or j > lj:
        return 0
    if x < 0 :
        return 0
    tf = c1 = c2 = c3 = c4 = 0
    if j != lj :
        c1 = 1 + doLess(a,i,j+1,a[i][j+1],ce-a[i][j+1] )
        tf = max(tf, c1)
    if j != 0 :
        c2 = 1 + doLess(a,i,j-1,a[i][j-1],ce-a[i][j-1])
        tf = max(tf, c2)
    if i != li :
        c3 = 1 + doLess(a,i+1,j,a[i+1][j],ce-a[i+1][j])
        tf = max(tf, c3)
    if i != 0 :
        c4 = 1 + doLess(a,i-1,j,a[i-1][j],ce-a[i-1][j])
        tf = max(tf, c4)
    return tf
    

a = [
    [100,40,60,50],
    [80,101,10,40], # 5 : 101 - 40 - 38 - 35 - 30 - 20 (PATH)
    [30,20,70,50],
    [35,38,40,101]
]
# a = [
#     [10,40,60,50],
#     [80,100,101,40], # 7 : 101 - 100 - 80 - 65 - 60 - 55 - 50 - 10 (PATH)
#     [65,60,55,50],
#     [35,38,200,10]
# ]

path = list()
for i in range(len(a)):
    for j in range(len(a[0])) :
        path.append(doLess(a,i,j,a[i][j],1)-1)
print(max(path))