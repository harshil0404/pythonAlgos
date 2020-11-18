import math
class node:
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None
class BT:
    def __init__(self,root):
        self.root = node(root)
    def insert(self,a):
        if self.root is None:
            self.root = node(a)
        else:
            self.ins(a,self.root)
    def ins(self,a,curr):
        if a < curr.data:
            if curr.l is None:
                curr.l = node(a)
            else:
                self.ins(a,curr.l)
        elif a > curr.data:
            if curr.r is None:
                curr.r = node(a)
            else:
                self.ins(a,curr.r)
        else:
            print('Value already present...')
    # def v(self):
    #     print(self.rec(self.root,""))
    # def rec(self,s,x):
    #     if s:
    #         # root->left->right search
    #         x += (str(s.data) + '-')
    #         x = self.rec(s.l,x)
    #         x = self.rec(s.r,x)
    #     return(x)
    def gcd(self,curr,g): # function to display gcd of the roots
        if curr.r :
            if curr.l :
                g.append(math.gcd(curr.l.data,curr.r.data))
                self.gcd(curr.l,g)
            return self.gcd(curr.r,g)
        if curr.l :
            if curr.r :
                g.append(math.gcd(curr.l.data,curr.r.data))
                self.gcd(curr.r,g)
            return self.gcd(curr.l,g)
        if not curr.l and not curr.r:
            return(g)
t = BT(5)
t.insert(15)
t.insert(20)
t.insert(32)
t.insert(16)
t.insert(10)
t.insert(3)
t.insert(4)
t.insert(2)
print(t.gcd(t.root,[]))
