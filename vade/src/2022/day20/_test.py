import copy
def load(name):return open(name,"rt").read()
def parse(name):
    f= open(name,"rt")
    res=[]
    for line in f.readlines():
        res+=[int(line)]
    return res

verbose=False
def aprint(s:str):
    if verbose:
        print(s)

class Game:
    def __init__(self):
        self.m={}
        self.air={}
    def load(self,l:list):
        for e in l:
            self.m[tuple(e)]=1
    def rotate0(self,l:list,e):
        sz=len(l)
        old=l.index(e)
        new=(old+e)%sz
        aprint(f"old={old} new={new}")
        print(f"{e} moves between ")
        res=[]
        for i in range(sz):
            if i==old:
                aprint(f"Skip old {l[i]} at {i}")
                continue
            aprint(f"Keep existing {l[i]}")
            if e>0:res+=[l[i]]
            if i==new:
                aprint(f"Add new {e} at {i}")
                res+=[e]
            if e<0:res+=[l[i]]
        return res
    def rotate(self,l0:list,e):
        l=copy.deepcopy(l0)
        sz=len(l)
        old=l.index(e)
        if e==0:
            #aprint("0 does not move:")
            pass
        else:
            if e>0:
                new=(old+e)%sz
                if old+e>=sz:
                    #aprint(f"OVERFLOW ? {new}")
                    new=(old+e+1)%sz
            else:
                #if old+e-1<0:raise Exception(f"Kaboom ")
                new=(old+e-1)%sz
            #aprint(f"{e} moves between {l[new]} and {l[(new+1)%sz]}")
            l.remove(e)
            l.insert(new,e)
        aprint(f"{l}")
        #aprint('')
        return l
    def nth(self,l:list,e,ofs:int):
        ind=l.index(e)
        sz=len(l)
        n=l[(ind+ofs)%sz]
        return n

inp00=[1,2,-3,3,-2,0,4,]

res0 = 3
res1 = 12571
res0_2 = 0
res1_2 = 0
# -8685 for input1 not good

import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        g=Game()
        self.assertEqual([4, 5, 6, 7, 1, 8, 9],g.rotate([4, 5, 6, 1, 7, 8, 9],1))
    def test_001(self):
        g=Game()
        self.assertEqual([4, 5, 6, 7, 8, -2, 9],g.rotate([4, -2, 5, 6, 7, 8, 9],-2))
    def test_010(self):
        g=Game()
        self.assertEqual([2, 1, -3, 3, -2, 0, 4],g.rotate(inp00,1))
#@unittest.skip
class T010(unittest.TestCase):
    def test_000(self):
        g=Game()
        r=copy.deepcopy(inp00)
        print(f"Initial arrangement:")
        print(f"{r}")
        print()
        for el in inp00:
            r=g.rotate(r,el)
            #print(f"r={r}")
        self.assertEqual([1, 2, -3, 4, 0, 3, -2],r)
        self.assertEqual(4,g.nth(r,0,1000))
        self.assertEqual(-3,g.nth(r,0,2000))
        self.assertEqual(2,g.nth(r,0,3000))
    def test_100(self):
        g=Game()
        l=parse("input0")
        r=copy.deepcopy(l)
        print(f"Initial arrangement:")
        print(f"{r}")
        print()
        for el in l:
            r=g.rotate(r,el)
        self.assertEqual([1, 2, -3, 4, 0, 3, -2],r)
        a=g.nth(r,0,1000)
        b=g.nth(r,0,2000)
        c=g.nth(r,0,3000)
        self.assertEqual(4,a)
        self.assertEqual(-3,b)
        self.assertEqual(2,c)
        self.assertEqual(res0,a+b+c)
    def Ztest_110(self):
        g=Game()
        l=parse("input1")
        print(f"len={len(l)}")
        r=copy.deepcopy(l)
        print("rotating")
        for i,el in enumerate(l):
            print(f"el={el} i={i}")
            r=g.rotate(r,el)
        print("rotating done")
        print(r.index(0))
        a=g.nth(r,0,1000)
        b=g.nth(r,0,2000)
        c=g.nth(r,0,3000)
        print(f"{a,b,c}")
        self.assertEqual(res1,a+b+c)
    def Ztest_910(self):
        g=Game()
        l=[1,-1,2,0]
        print(f"len={len(l)}")
        r=copy.deepcopy(l)
        for el in l:
            r=g.rotate(r,el)
        print(r)
        print(r.index(0))
        a=g.nth(r,0,1000)
        b=g.nth(r,0,2000)
        c=g.nth(r,0,3000)
        print(f"{a,b,c}")
        self.assertEqual(res1,a+b+c)
    def test_911(self):
        g=Game()
        l=[-3,0,2]
        l=[
2115,
3713,
4975,
-7020,
-3949,
0,
-603,
-5596,
9212,
1244,
-559,
        ]
        print(f"len={len(l)}")
        r=copy.deepcopy(l)
        global verbose
        verbose=True
        print(f"{r}")
        print()
        for el in l:
            r=g.rotate(r,el)
        verbose=False
        print(r.index(0))
        print(r)
        a=g.nth(r,0,1000)
        b=g.nth(r,0,2000)
        c=g.nth(r,0,3000)
        print(f"{a,b,c}")
        self.assertEqual(res1,a+b+c)
