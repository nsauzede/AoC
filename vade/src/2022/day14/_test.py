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
def flow(d:dict,p0:tuple,b=None,bedrock=False)->tuple:
    if b==None:b=box(d)
    x1,y1,x2,y2=b
    x,y=p0
    if bedrock:
        if y==y2+1:return p0
    p=(x,y+1)
    if p not in d:# straight flow
        return p
    p=(x-1,y+1)
    if not bedrock:
        if x==x1:#free fall left
            return p
    if p not in d:# diag left
        return p
    p=(x+1,y+1)
    if not bedrock:
        if x+1>x2:#free fall right
            return p
    if p not in d:#diag right
        return p
    return p0 # rest
def drop(d:dict,b=None,bedrock=False,p=(500,0))->tuple:
    if b==None:b=box(d)
    x1,y1,x2,y2=b
    while True:
        p0=p
        p=flow(d,p,b,bedrock)
        x,y=p
        if p==p0:#rest
            d[p]='o'
            return p
        if not bedrock:
            if y>y2 or x<x1 or x>x2:#free fall
                return p
    return 0,0
def pour(d:dict,bedrock=False)->int:
    b=box(d)
    x1,y1,x2,y2=b
    n=0
    while True:
        p=drop(d,b,bedrock)
        x,y=p
        if bedrock:
            if y==0:break
        else:
            if y>y2 or x<x1 or x>x2:break
        n+=1
    if bedrock:n+=1
    return n

import unittest
res0 = 24
res1 = 1068
res0_2 = 93
res1_2 = 27936

#@unittest.skip
class T000(unittest.TestCase):
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
        self.assertEqual(res0_2,pour(d,bedrock=True))
    def test_210(self):
        d=scan(parse(load("input1")))
        self.assertEqual(res1_2,pour(d,bedrock=True))
