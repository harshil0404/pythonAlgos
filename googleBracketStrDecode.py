s = "3[a2[c]]" # accaccacc
# s = '3[a]2[lk]' # aaalklk
# s = '10[leetcode]' # res = leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode
a = list()
for i in range(len(s)) :
    try :
        if int(s[i]) or int(s[i]) == 0 : 
            if i == 0 :
                a.append(int(s[i:s.index('[',i)]))
            if (type(a[-1]) is not int):
                a.append(int(s[i:s.index('[',i)]))
    except :
        a.append(s[i])
for i in range(len(a)-1,-1,-1) :
    if a[i] == '[':
        tstr = ''
        sind = i+1
        eind = a.index(']',i)
        fact = a[i-1]
        tstr = ''.join(a[sind : eind])
        tstr = tstr*fact
        del a[i-1 : eind+1]
        a[i-1:i-1] = list(tstr)
res = ''.join(a[::])
print(res)
# https://leetcode.com/problems/decode-string/submissions/