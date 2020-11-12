class node(object):
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None
class Btree(object):
    def __init__(self,root):
        self.root = node(root)
    def rec(self,s,x):
        if(s):
            # root->left->right search
            x += (str(s.data) + '-')
            x = self.rec(s.l,x)
            x = self.rec(s.r,x)
        return(x)
    def levelorder(self,start,tf=False):
        lst = []
        c = 0
        lst.append(start)
        res = ''
        while lst :
            t1 = False
            x = lst.pop(0)
            res += (str(x.data)+'-')
            if x.l:
                t1 = True
                c+=1
                lst.append(x.l)
            if x.r:
                if(not t1):
                    c+=1
                lst.append(x.r)
        if(tf == False):
            print(res)
        return c-1
    def rev_levelorder(self,start):
        lst = []
        sta = []
        res = ''
        lst.append(start)
        while lst :
            x = lst.pop(0)
            sta.append(x)
            if x.r :
                lst.append(x.r)
            if x.l : 
                lst.append(x.l)
        while sta :
            res+=(str(sta.pop().data) + '-')
        print(res)
    def height(self):

        print(self.levelorder(t.root,True))

t = Btree(5)
t.root.l = node(2)
t.root.r = node(3)
t.root.l.l = node(4)
t.root.l.r = node(10)
t.root.l.r.l = node(6)
t.root.l.r.l.l = node(10)
t.root.l.r.l.l.l = node(11)
t.root.l.r.l.l.l.l = node(12)
t.root.l.r.r = node(8)
t.root.l.l.r = node(555)
# print(t.rec(t.root,''))
# t.levelorder(t.root)
t.height()



