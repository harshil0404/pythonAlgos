main = []
def ans(a):
    print(max(a))
    return max(a)

def hourglass(h,x=0,y=3,x1=0,y1=3):
    sum1 = sum2 = sum3 = 0
    for i in range(x,y):
        if i == x :
            for j in range(x1,y1):
                sum1 += h[i][j]
        elif i == x+1 :
            sum2 = h[i][y1-2]
        elif i == x+2 :
            for j in range(x1,y1):
                sum3 += h[i][j]
    main.append(sum1+sum2+sum3)
    if x1 == 3 and x < 3 :
        hourglass(h,x+1,y+1,0,3)
    elif x1 < 3 :
        hourglass(h,x,y,x1+1,y1+1)
    return max(main) if len(main) == 16 else hourglass(h,x,y,x1+1,y1+1)
        

arr=[[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],
     [0, 0, 0, 2, 0, 0],
     [0, 0, 1, 2, 4, 0]]

harshil = hourglass(arr)
print(harshil)