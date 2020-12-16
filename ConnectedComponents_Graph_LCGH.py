e = [[0, 1], [1, 2], [3, 4], [3,5],[6,1]]
cnt = 0
def bfs(v) :
    for i in range(len(e)-1,-1,-1) :
        x,y = e[i]
        if x in v or y in v :
            v.append(x)
            v.append(y)
            e.remove(e[i])
    return
while e :
    x,y = e[0]
    e.pop(0)
    vi = []
    vi.append(x)
    vi.append(y)
    bfs(vi)
    cnt+=1
print(cnt)
