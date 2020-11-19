def toPPings(t,n,c,mem):
    if n < 0 or c == 0: 
        return 0
    key = str(t[n])+':'+str(n)+':'+str(c)
    if key in mem :
        return mem[key]
    else:
        if c >= t[n] :
            case1 = toPPings(t,n-1,c-t[n],mem) + t[n]
            case2 = toPPings(t,n-1,c,mem)
            mem[key] =  max(case1,case2)
        else :
            mem[key] = toPPings(t,n-1,c,mem)
    return mem[key]

p = [400,450,600,500]
t = [50,70,120,30]
cash = 770 # 500+50+70+120+30 = 770,  so result will be 770
# cash = 760 # 760 is not possible, so result will be 600+120+30 = 750 and etc other ways if possible
maxi = 0
mem = dict()
# foreach pizza we want to add any number of toppings to spend as much as we can
for i in range(len(p)):
    c = cash
    # below 'c' is the amount of cash remaining after buying a pizza. this 'c' can e utilized to add toppings
    c -= p[i]
    # checking if the prize of pizza is not greater then available original cash
    if c > 0:
        # this function the maximum cost of toppings we can add after buying a pizza, the returned 
        # value is stored in 'top'...
        # similar function as knapsack (MEMOIZED VERSION)
        top = toPPings(t,len(t)-1,c,mem)
        # below 'c' is cash remaining after buying pizza, 'cash' is the original amount to spend.
        # Please understand this mathematical equation on your own..
        # to understand it please get variable definations of cash, c, top chear in your mind...
        maxi = max(cash - (c - top),maxi)
print(maxi)
# https://leetcode.com/discuss/interview-question/356935/