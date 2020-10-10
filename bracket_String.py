def convertTuple(strr):
    bracket = []
    for i in range(len(strr)):
        bracket.append(strr[i])
    cnt = 0
    # print(bracket)
    for k in range(len(bracket)):
        if(bracket[k] == ')'):
            for j in range(k,-1,-1):
                if(bracket[j] == '('):
                    cnt+=1
                    bracket[j] = '*'
                    break
    return cnt*2

strr = "(()())(()((()"
print(convertTuple(strr)/2)

#https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/