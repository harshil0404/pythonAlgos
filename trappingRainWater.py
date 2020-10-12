def makeGrid(d):
    grid = []
    rows = max(d)
    col = len(d)
    for i in range(rows):
        g = []
        for j in range(col):
            if(d[j] > 0):
                g.append(1)
                d[j] -= 1
            else:
                g.append(0)
        grid.append(g)
    return grid

def calculateTrappedWater(g):
    sum = 0
    for i in range(len(g)):
        oneCount = g[i].count(1)
        tf = True
        flag = 0
        for j in range(len(g[i])):
            if(g[i][j] == 1):
                flag = 1
                oneCount -= 1
                if(oneCount == 0):
                    tf = False
            elif(g[i][j] == 0 and tf == True and flag == 1):
                sum += 1
    print(sum)

dam_struct = [4,0,0,3,0,2,5]
grid = makeGrid(dam_struct)
# print(grid)
calculateTrappedWater(grid)
