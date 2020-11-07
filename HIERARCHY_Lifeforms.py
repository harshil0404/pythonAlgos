def makeobj(a):
    d = {}
    s = set()
    for i in range(len(a)):
        if(a[i][0] not in d.keys()):
            d[f'{a[i][0]}'] = []
            d[f'{a[i][0]}'].append(a[i][1])
            s.add(a[i][1])
        else:
            d[f'{a[i][0]}'].append(a[i][1])
            s.add(a[i][1])
    findroot(d,s)
def findroot(d,s):
    keys = list(d.keys())
    for i in range(len(keys)-1,-1,-1):
        if(keys[i] in s):
            keys.remove(keys[i])
    output(d,keys[0],0)
def output(d,r,l):
    for i in range(l):
        print('\t',end='')
    print(r)
    if(r in list(d.keys())):
        for i in range(len(d[r])):
            output(d,d[r][i],l+1)
    else:
        return 0

# a = [['animal','mammal'],['animal','birds'],['lifeform','animal'],
#      ['cat','lion'],['mammal','cat'],['animal','fish']]
a = []
n = ''
m = ''
while n != 'stop'  :
    print('enter new relation : ')
    n = input('parent : ').strip()
    m = input('child  : ').strip()
    a.append([n,m])
    makeobj(a)

