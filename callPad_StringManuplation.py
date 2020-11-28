t = '492743665378'
a = ['foo','bar','set','hat','old','was','qri','stm']
mem = '2abc3def4ghi5jkl6mno7pqrs8tuv9wxyz'
# or mem = '22233344455566677778889999' more eaiser
for i in range(len(a)):
    inti = ''
    temp = a[i]
    for j in range(len(a[i])):
        stri = max(mem.index(a[i][j])-4,0)
        x = ''.join(filter(str.isdigit,mem[stri : stri+4 : ]))
        inti += x
    if inti in t :
        print(temp)
# https://www.youtube.com/watch?v=PIeiiceWe_w