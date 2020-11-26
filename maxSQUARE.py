sq = [
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]
s = [[0 for _ in range(len(sq[0])+1)] for _ in range(len(sq)+1)]
large = 0 
for i in range(1,len(s)):
    for j in range(1,len(s[0])):
        if sq[i-1][j-1] == 1 :
            s[i][j] = 1 + min(s[i-1][j-1],s[i][j-1],s[i-1][j])
            if large < s[i][j] :
                large = s[i][j]
print(large**2)

