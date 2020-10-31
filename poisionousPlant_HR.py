p = [4 ,3, 7, 5, 6 ,4 ,2]
c = -1
x = -1
count = 0
print(p)
while c!=0:
    tf = True
    c = 0
    count+=1
    print("-=> ",count)
    for i in range(len(p)-1,0,-1):
        if(p[i]>p[i-1] and tf == True):
            c+=1
            x=p[i]
            del p[i:i+1]
            tf = False
            print(p,x,i)
        if x != p[i-1]:
            # print(x)
            tf = True
print(count-1)