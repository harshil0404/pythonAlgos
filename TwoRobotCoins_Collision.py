import sys

def coins(g,summ,i,j,j2,mem):
    li = len(g)-1
    lj = len(g[0])-1
    key = str(i)+str(j)+str(j2)
    # Memoized version
    if key in mem :
        return mem[key]
    # defining the end situation
    if i == li and j == 0 and j2 == lj :
        return g[i][j] + g[i][j2]
    # when indices out of range ( BASE CASE )
    if i > li or j > lj or i < 0 or j < 0 or j2 < 0 or j2 > lj :
        return -sys.maxsize-1 

    # collision case :- 
    # if the collision happens then 'if' condition will only return g[i][j] and 'else' will return g[i][j]+g[i][j2]
    # so else part will always be greater than if part... so as we are maximizing the result only else part counts
    # here else part is non colliding
    if j == j2 :
        res = g[i][j]
    else :
        res = g[i][j] + g[i][j2]

    # 3 ways robot_1 can move and 3 ways robot_2 can move, so total number of waus are 3*3 = 9, which are as follow
    # 1st case = j+1, 2nd case = j-1 & 3rd case = j (combine them all) and i+1 is constant for both of them...
    # finding maximum from all of them...
    summ1 = max(coins(g,summ,i+1,j+1,j2,mem),coins(g,summ,i+1,j-1,j2,mem),coins(g,summ,i+1,j,j2,mem))
    summ2 = max(coins(g,summ,i+1,j,j2+1,mem),coins(g,summ,i+1,j,j2-1,mem),coins(g,summ,i+1,j+1,j2+1,mem))
    summ3 = max(coins(g,summ,i+1,j-1,j2+1,mem),coins(g,summ,i+1,j+1,j2-1,mem),coins(g,summ,i+1,j-1,j2-1,mem))
    summ = max(summ1,summ2,summ3)
    res += summ
    mem[key] = res
    return mem[key]

# c = [[9 , 10, 15, 12, 11],
#      [7 , 5 , 11, 6 , 8 ],
#      [4 , 1 , 27, 13, 17],
#      [2 , 4 , 18, 2 , 1 ], # result = 130
#      [15, 3 , 22, 6 , 10],
#      [8 , 2 , 5 , 9 , 6 ]
#     ] 
# c = [[3, 6, 8,  2],
# 	   [5, 2, 4,  3],
# 	   [1, 1, 20, 10], # r1+r2 = 73 ::: r1 = 3+2+20+1+1 r2 = 2+4+10+20+10
# 	   [1, 1, 20, 10],
# 	   [1, 1, 20, 10]]
c = [[10,20,30,40,50],
     [5 ,10,15,20,25],
     [10,20,30,40,10], # r1+r2 = 260 ::: r1 = 10+10+30+45+10, r2 = 50,25,40,30,10
     [30,45,20,25,30],
     [10,10,10,10,10]
     ]
j2 = len(c[0])-1
mem = dict()
print(coins(c,0,0,0,j2,mem))
