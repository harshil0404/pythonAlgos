# t = '23:59'
t = '19:35'
mins = int(t[0:2])*60 + int(t[3:])
orig = [int(t[0]),int(t[1]),int(t[3]),int(t[4])]
while True :
    mins = (mins + 1) % (24*60)
    dupl = [int(mins/60/10),int(mins/60%10),int(mins%60/10),int(mins%60%10)]
    tf = True 
    for i in dupl :
        if i not in orig :
            tf = False
    if tf :
        print(int(mins/60/10),int(mins/60%10),':',int(mins%60/10),int(mins%60%10))
        break
