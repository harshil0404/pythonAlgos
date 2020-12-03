# ----------> RECURSIVE : ITTERATIVE METHOD FOLLOWS...
def minjumps(a,n) :
    if n > len(a)-1 or n == len(a) - 1: 
        return 0
    j = []
    for i in range(1,a[n]+1) :
        x = 1 + minjumps(a,n+i)
        j.append(x)
    mini = min(j)
    return mini
a = [3,3,1,2,4,2,1] # 3
# a = [2,5,3,1,2,4,1] # 2
# a = [4,3,2,1] # 1
# a = [1,2,3,2,1,2,1,2,1,1,2,1,2,3,3,2,1,1,3,2,1,2,1,1,2,1,2,3,1,1,2,3,3,1,2,1,1,2,3,2,1,1,2,1,1,3,1,2,3,2,1,3,2,1,3,1,3,1,1,3,1,3,1,3,2,1,2,1,3,1,2,3,1,1,2,3,1,2] # checks TIMECOMLEXITY
# a = [1,2,3,2,1,2,1,2,1,1,2,1,2,3,3,2,1,1,3,2,1,2,1,1,2,1,2,3,1,1,2,3,3] # time complexity check
print(minjumps(a,0))

#-----------> ITTERATIVE ADVANCED :

# import sys
# a = [3,1,3,2,4,3,1] # 3
# 3 -> 3 -> 3 -> 1 | 3 3 4 1 | 3 2 4 1 | 3 2 3 1 | ... values path
# 0 -> 2 -> 5 -> 6 indices path
# a = [2,5,3,1,2,4,1] # 2
# a = [4,3,2,1] # 1
# a = [1,2,3,2,1,2,1,2,1,1,2,1,2,3,3,2,1,1,3,2,1,2,1,1,2,1,2,3,1,1,2,3,3,1,2,1,1,2,3,2,1,1,2,1,1,3,1,2,3,2,1,3,2,1,3,1,3,1,1,3,1,3,1,3,2,1,2,1,3,1,2,3,1,1,2,3,1,2] # checks TIMECOMLEXITY
# a = [1,2,3,2,1,2,1,2,1,1,2,1,2,3,3,2,1,1,3,2,1,2,1,1,2,1,2,3,1,1,2,3,3] # time complexity check
# t = [sys.maxsize for _ in range(len(a))] # MINIMUM JUMP ARRAY
# t[0] = 0
# p = [sys.maxsize for i in range(len(a))] #PATH ARRAY
# p[0] = 0
# for i in range(len(a)) : 
#     for j in range(0,i) :
#         if j + a[j] >= i :
#             t[i] = min(t[i],t[j]+1)
#             p[i] = min(p[i],j)
# print(t[-1] , 'JUMPS')
# # path ='PATH : ' + ' -> '.join(sorted(set(list(map(str,p[::-1]))))) + ' -> ' + str(len(a)-1)
# print(set(p))

# https://www.youtube.com/watch?v=jH_5ypQggWg