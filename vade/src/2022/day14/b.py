def load(name):return open(name,"rt").read()
def parse(s:str)->list:
    res=[]
    for line in s.splitlines():
        res+=[[list(eval(x)) for x in line.split(" -> ")]]
    return res
def scan(paths:list)->dict:
    d={}
    for path in paths:
        p0=path[0]
        for p in path[1:]:
            if p0[0]==p[0]:#vline
                x=p0[0]
                y1,y2=p0[1],p[1]
                delta=y2-y1
                step=delta//abs(delta)
                for y in range(y1,y2+step,step):
                    d[(x,y)]='#'
            elif p0[1]==p[1]:#hline
                y=p0[1]
                x1,x2=p0[0],p[0]
                delta=x2-x1
                step=delta//abs(delta)
                for x in range(x1,x2+step,step):
                    d[(x,y)]='#'
            p0=p
    return d
def box(d:dict)->tuple:#returns box comprising walls plus dropsource at (500,0)
    INF=999999999
    x1=500;y1=0
    x2=-INF;y2=-INF
    for e in d:
        x,y=e
        if x<x1:x1=x
        if x>x2:x2=x
        if y<y1:y1=y
        if y>y2:y2=y
    return x1,y1,x2,y2
def flow(d:dict,p0:tuple,b=None)->tuple:
    if b==None:b=box(d)
    x1,y1,x2,y2=b
    x,y=p0
    p=(x,y+1)
    if p not in d:# straight flow
        return p
    p=(x-1,y+1)
    if x==x1:#free fall left
        return p
    if p not in d:# diag left
        return p
    p=(x+1,y+1)
    if x+1>x2:#free fall right
        return p
    if p not in d:#diag right
        return p
    return p0 # rest
def drop(d:dict,b=None,p=(500,0))->tuple:
    if b==None:b=box(d)
    x1,y1,x2,y2=b
    while True:
        p0=p
        p=flow(d,p,b)
        x,y=p
        if p==p0:#rest
            d[p]='o'
            if y==0:print(f"WE REACHED Y==0!!! X={x}")
            return p
        if y>y2 or x<x1 or x>x2:#free fall
            return p
    return 0,0
def pour(d:dict)->int:
    b=box(d)
    x1,y1,x2,y2=b
    n=0
    while True:
        p=drop(d,b)
        x,y=p
        if y>y2 or x<x1 or x>x2:
            break
        n+=1
    return n
def flow2(d:dict,p0:tuple,b=None)->tuple:
    if b==None:b=box(d)
    x1,y1,x2,y2=b
    x,y=p0
    if y==y2+1:#bedrock
        return p0
    p=(x,y+1)
    if p not in d:# straight flow
        return p
    p=(x-1,y+1)
    if p not in d:# diag left
        return p
    p=(x+1,y+1)
    if p not in d:#diag right
        return p
    return p0 # rest
def drop2(d:dict,b=None,p=(500,0))->tuple:
    if b==None:b=box(d)
    x1,y1,x2,y2=b
    while True:
        p0=p
        p=flow2(d,p,b)
        x,y=p
        if p==p0:#rest
            d[p]='o'
            return p
    return 0,0
def pour2(d:dict)->int:
    b=box(d)
    x1,y1,x2,y2=b
    n=1
    while True:
        p=drop2(d,b)
        x,y=p
        if y==0:
            break
        n+=1
    return n
res0 = 24
res1 = 1068
res0_2 = 93
res1_2 = 27936
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        l=parse(inp00s)
        self.assertEqual([[[498,4],[498,6],[496,6]],[[503,4],[502,4],[502,9],[494,9]]],l)
        self.assertEqual(res00,scan(l))
        self.assertEqual(res00,scan(parse(load("input0"))))
    def test_100(self):
        d=scan(parse(load("input0")))
        self.assertEqual((494,0,503,9),box(d))
        self.assertEqual((500,8),drop(d))
        self.assertEqual((499,8),drop(d))
    def test_101(self):
        d=scan(parse(load("input0")))
        self.assertEqual(res0,pour(d))
    def test_110(self):
        d=scan(parse(load("input1")))
        self.assertEqual(res1,pour(d))
    def test_200(self):
        d=scan(parse(load("input0")))
        self.assertEqual(res0_2,pour2(d))
    def test_210(self):
        d=scan(parse(load("input1")))
        self.assertEqual(res1_2,pour2(d))
inp00s="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
res00={
                        (498,4):'#',       (502,4):'#',(503,4):'#',
                        (498,5):'#',       (502,5):'#',
(496,6):'#',(497,6):'#',(498,6):'#',       (502,6):'#',
                                           (502,7):'#',
                                           (502,8):'#',
(494,9):'#',(495,9):'#',(496,9):'#',(497,9):'#',(498,9):'#',(499,9):'#',(500,9):'#',(501,9):'#',(502,9):'#',
}
