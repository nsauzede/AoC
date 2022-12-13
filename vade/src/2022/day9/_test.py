def parse(inp:str)->dict:
    m=[]
    for l in inp.splitlines():
        #print(f"l={l}")
        n,v=l.split(" ")
        m+=[[n,int(v)]]
    return m

def mark(p:dict, i:int, j:int):
        if j not in p:p[j]={}
        p[j][i]=1

def draw(i,j,x,y,w,h):
    #return
    for r in range(h):
        for c in range(w):
            if (x,y)==(c,r):print('H',end='')
            elif (i,j)==(c,r):print('T',end='')
            elif (0,4)==(c,r):print('s',end='')
            else:print('.',end='')
        print('')
    print('')

def moveright(p:dict,i:int,j:int,x:int,y:int,c:int)->(int,int,int,int):
    for n in range(c):
        if i<x:
            i,j=x,y
        x+=1
        mark(p,i,j)
        draw(i,j,x,y,6,5)
    return i,j,x,y

def moveleft(p:dict,i:int,j:int,x:int,y:int,c:int)->(int,int,int,int):
    for n in range(c):
        if i>x:
            i,j=x,y
        x-=1
        mark(p,i,j)
        draw(i,j,x,y,6,5)
    return i,j,x,y

def moveup(p:dict,i:int,j:int,x:int,y:int,c:int)->(int,int,int,int):
    for n in range(c):
        if j>y:
            i,j=x,y
        y-=1
        mark(p,i,j)
        draw(i,j,x,y,6,5)
    return i,j,x,y

def movedown(p:dict,i:int,j:int,x:int,y:int,c:int)->(int,int,int,int):
    for n in range(c):
        if j<y:
            i,j=x,y
        y+=1
        mark(p,i,j)
        draw(i,j,x,y,6,5)
    return i,j,x,y

def calcp(m:list,x:int,y:int)->dict:
    p={}
    i=x;j=y
    draw(i,j,x,y,6,5)
    for t,c in m:
        print(f"== {t} {c} ==")
        if t=='R':i,j,x,y=moveright(p,i,j,x,y,c)
        if t=='U':i,j,x,y=moveup(p,i,j,x,y,c)
        if t=='L':i,j,x,y=moveleft(p,i,j,x,y,c)
        if t=='D':i,j,x,y=movedown(p,i,j,x,y,c)
    return p

def mark2(p:dict, knots:list):
    i,j=knots[-1]
    if j not in p:p[j]={}
    p[j][i]=1

def draw2(knots,w=6,h=5):
    #return
    for r in range(h):
        for c in range(w):
            #print(f"knots={knots} c,r={c,r}")
            if knots[0]==[c,r]:print('H',end='');continue
            cont=False
            for i in range(1,len(knots)):
                if knots[i]==[c,r]:print(f"{i}",end='');cont=True;break
            if cont:continue
            if (0,4)==(c,r):print('s',end='');continue
            print('.',end='')
        print('')
    print('')

def movehoriz(p:dict,knots:list,dir:int)->list:
    for n in range(1,len(knots)):
        #print(f"dir={dir} n={n}:{knots[n]} n-1={n-1}:{knots[n-1]}")
        if knots[n][0]*dir<knots[n-1][0]*dir:
            #print(f"set n={n}")
            knots[n]=knots[n-1].copy()
            #print(f"n={n}:{knots[n]} n-1={n-1}:{knots[n-1]}")
            break
    knots[0][0]+=dir

def movevert(p:dict,knots:list,dir:int)->list:
    for n in range(1,len(knots)):
        #print(f"dir={dir} n={n}:{knots[n]} n-1={n-1}:{knots[n-1]}")
        if knots[n][1]*dir<knots[n-1][1]*dir:
            #print(f"set n={n}")
            knots[n]=knots[n-1].copy()
            #print(f"n={n}:{knots[n]} n-1={n-1}:{knots[n-1]}")
            break
    knots[0][1]+=dir

def moveright2(p:dict,knots:list,c:int):
    for n in range(c):
        movehoriz(p,knots,1)
        mark2(p,knots)
        draw2(knots,6,5)

def moveleft2(p:dict,knots:list,c:int):
    for n in range(c):
        movehoriz(p,knots,-1)
        mark2(p,knots)
        draw2(knots,6,5)

def moveup2(p:dict,knots:list,c:int):
    for n in range(c):
        movevert(p,knots,-1)
        mark2(p,knots)
        draw2(knots,6,5)

def movedown2(p:dict,knots:list,c:int):
    for n in range(c):
        movevert(p,knots,1)
        mark2(p,knots)
        draw2(knots,6,5)

def calcp2(m:list,x:int,y:int,n=2)->dict:
    p={}
    knots=mkrope([0,4],n)
    draw2(knots,6,5)
    for t,c in m:
        print(f"== {t} {c} ==")
        if t=='R':moveright2(p,knots,c)
        if t=='U':moveup2(p,knots,c)
        if t=='L':moveleft2(p,knots,c)
        if t=='D':movedown2(p,knots,c)
    return p

def ddif0(a:dict, b:dict)->int:
    ret=0
    #print(f"a={a}")
    #print(f"b={b}")
    for y in a:
        if y not in b:ret+=1;print(f"y={y} not in b");break
        #for x in a[y]:if x not in b[y]:ret+=1;print(f"y={y} x={x} not in b");break
        if a[y]!=b[y]:ret+=1;print(f"y={y} different");break
        if ret>0:break
    return ret

def ddif(a:dict, b:dict)->int:
    return ddif0(a,b)+ddif0(b,a)

def calc(p:dict)->int:
    c=0
    #print(f"p={p}")
    for d in p.values():
        c+=sum(d.values())
    return c

def run1(inp:str)->int:
    m=parse(inp)
    p=calcp(m,0,4)
    c=calc(p)
    return c

def run2(inp:str)->int:
    m=parse(inp)
    p=calcp2(m,0,4,10)
    c=calc(p)
    return c

import unittest
def load(name):return open(name,"rt").read()
m0=[
['R',4],
['U',4],
['L',3],
['D',1],
['R',4],
['D',1],
['L',5],
['R',2],
]
res0 = 13
res1 = 5735
res0_2 = 1
#res0_2 = 13
res1_2 = 0
def mkrope(k:list,c:int)->list:
    l=[]
    for i in range(c):
        l+=[k.copy()]
    return l
class T1(unittest.TestCase):
#class T1():
    def test_00(self):
        p={}
        knots=[[0,4],[0,4]]
        movehoriz(p,knots,1)
        self.assertEqual([[1,4],[0,4]],knots)
    def test_01(self):
        p={}
        knots=[[0,4],[0,4]]
        movehoriz(p,knots,1)
        self.assertEqual([[1,4],[0,4]],knots)
        movehoriz(p,knots,1)
        self.assertEqual([[2,4],[1,4]],knots)
    def test_02(self):
        p={}
        knots=mkrope([0,4],2)
        movehoriz(p,knots,1)
        self.assertEqual([[1,4],[0,4]],knots)
        movehoriz(p,knots,1)
        self.assertEqual([[2,4],[1,4]],knots)
    def test_12(self):
        p={}
        knots=mkrope([0,4],3)
        movehoriz(p,knots,1)
        self.assertEqual([[1,4],[0,4],[0,4]],knots)
    def test_121(self):
        p={}
        knots=mkrope([0,4],3)
        movehoriz(p,knots,1)
        self.assertEqual([[1,4],[0,4],[0,4]],knots)
        movehoriz(p,knots,1)
        self.assertEqual([[2,4],[1,4],[0,4]],knots)
    def test_13(self):
        p={}
        knots=mkrope([0,4],3)
        c=1
        moveright2(p,knots,c)
        self.assertEqual([[1,4],[0,4],[0,4]],knots)
    def test_14(self):
        p={}
        knots=mkrope([0,4],3)
        c=2
        moveright2(p,knots,c)
        self.assertEqual([[2,4],[1,4],[0,4]],knots)
    def test_15(self):
        p={}
        knots=mkrope([2,4],3)
        c=2
        moveleft2(p,knots,c)
        self.assertEqual([[0,4],[1,4],[2,4]],knots)
    def test_15(self):
        p={}
        knots=mkrope([2,4],3)
        c=2
        moveup2(p,knots,c)
        self.assertEqual([[2,2],[2,3],[2,4]],knots)
    def test_16(self):
        p={}
        knots=mkrope([2,2],3)
        c=2
        movedown2(p,knots,c)
        self.assertEqual([[2,4],[2,3],[2,2]],knots)
    def test_03(self):
        p={}
        knots=mkrope([0,4],2)
        c=1
        moveright2(p,knots,c)
        self.assertEqual([[1,4],[0,4]],knots)
    def test_04(self):
        p={}
        knots=mkrope([0,4],2)
        c=2
        moveright2(p,knots,c)
        self.assertEqual([[2,4],[1,4]],knots)
    def test_05(self):
        p={}
        knots=mkrope([0,4],2)
        c=3
        moveright2(p,knots,c)
        self.assertEqual([[3,4],[2,4]],knots)
    def Ztest_04(self):
        p={}
        knots=[[1,4],[0,4]]
        c=1
        moveleft2(p,knots,c)
        self.assertEqual([[0,4],[0,4]],knots)
    def Ztest_05(self):
        p={}
        knots=mkrope([0,4],2)
        draw2(knots)
        moveright2(p,knots,1)
        draw2(knots)
    def Ztest_20(self):
        self.assertEqual(0, ddif({0: {1:1, 2:1}, 1:{3:1} }, {1: {3:1}, 0: {2:1, 1:1}}))
    def Ztest_50(self):
        inp0=load("input0")
        m0=parse(inp0)
        self.assertEqual(res0, calc(calcp(m0,0,4)))
    def test_60(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_70(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def Ztest_80(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
class T2(unittest.TestCase):
#class T2():
    def Ztest_020(self):
        inp0=load("input0")
        Zself.assertEqual(4, calc2_(parse(inp0),1,2))
    def Ztest_021(self):
        inp0=load("input0")
        self.assertEqual(8, calc2_(parse(inp0),3,2))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def Ztest_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
