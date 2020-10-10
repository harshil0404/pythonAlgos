def makeClstr(r,c,g,tf):
    clstr = []
    for i in range(r):
        cl = []
        for j in range(c):
            if tf == True :
                if(g[i][j]==1):
                    cl.append([i,j])
                else:
                    if(cl):
                        clstr.append(cl)
                        cl = []
            elif tf == False :
                if(g[j][i] == 1):
                    cl.append([j,i])
                else:
                    if(cl):
                        clstr.append(cl)
                        cl = []
        if(cl):
            clstr.append(cl)
    return clstr

def merge_clusters(z):
    for i in range(len(z)-1,-1,-1):
        for j in range(len(z)-1,-1,-1):
            if(z[i] == z[j]):
                continue
            elif(len(z[i]) > len(z[j])):
                for a in range(len(z[j])-1,-1,-1):
                    if(z[j][a] in z[i]):
                        z[i] += z[j]
                        z.remove(z[j])
                        z.append([])
                        break
            elif(len(z[i]) <= len(z[j])):
                for a in range(len(z[i])-1,-1,-1):
                    if(z[i][a] in z[j]):
                        z[j]+=z[i]
                        z.remove(z[i])
                        z.append([])
                        break
    for k in range(z.count([])):
        z.remove([])
    main = []
    [main.append(x) for x in z if x not in main]
    return(main)

rows = 5
columns = 4
grid = [
   [ 1, 1, 0, 0 ],
   [ 0, 1, 0, 1 ],
   [ 1, 0, 1, 1 ],
   [ 0, 1, 1, 1 ],
   [ 1, 0, 1, 1 ]
]
cluster_row = makeClstr(rows,columns,grid,True)
cluster_column = makeClstr(columns,rows,grid,False)
merged = merge_clusters(cluster_row+cluster_column)
print(len(merged))