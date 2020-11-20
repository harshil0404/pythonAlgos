import sys
def coins(g,summ,i,j):
    li = len(g)-1
    lj = len(g[0])-1
    if i == li and j == 0 :
        return g[i][j]
    if i > li or j > lj or i < 0 or j < 0 :
        return -sys.maxsize-1
    summ = g[i][j] + max(coins(g,summ,i+1,j+1),coins(g,summ,i+1,j-1),coins(g,summ,i+1,j))
    return summ
c = [[9 , 10, 15, 12, 11],
     [7 , 5 , 11, 6 , 8 ],
     [4 , 1 , 27, 13, 17],
     [2 , 4 , 18, 2 , 1 ],
     [15, 3 , 22, 6 , 10],
     [8 , 2 , 5 , 9 , 6 ]
    ]

print(coins(c,0,0,0))
