def load(name):return open(name,"rt").read()
def parse(s:str)->dict:
    d={}
    y=0
    for line in s.splitlines():
        x=0
        for c in line:
            if c=='#':
                d[(x,y)]=1
            x+=1
        y+=1
    return d
def fparse(name):return parse(load(name))
verbose=False
def aprint(s:str):
    if verbose:
        print(s)
def neighbours(d:dict,e:tuple)->list:
    x,y=e;r=[]
    for pos in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
        if pos in d:r+=[pos]
    return r
def scan(d:dict,dirs:list)->int:
    props={}
    totn=0
    for e in d:
        x,y=e
        N=(x,y-1);NE=(x+1,y-1);NW=(x-1,y-1)
        S=(x,y+1);SE=(x+1,y+1);SW=(x-1,y+1)
        W=(x-1,y);E=(x+1,y)
        n=neighbours(d,e)
        r=len(n)
        totn+=r
        aprint(f"{e}: r={r}")
        if r<=0:continue
        for dir in dirs:
            if dir=='N':
                if N not in n and NE not in n and NW not in n:
                    if N not in props:props[N]=[]
                    props[N]+=[e]
                    break
            elif dir=='S':
                if S not in n and SE not in n and SW not in n:
                    if S not in props:props[S]=[]
                    props[S]+=[e]
                    break
            elif dir=='W':
                if W not in n and NW not in n and SW not in n:
                    if W not in props:props[W]=[]
                    props[W]+=[e]
                    break
            elif dir=='E':
                if E not in n and NE not in n and SE not in n:
                    if E not in props:props[E]=[]
                    props[E]+=[e]
                    break
    for k,v in props.items():
        if len(v)==1:
            aprint(f"k={k} v={v} candidate to move")
            del d[v[0]]
            d[k]=1
    dirs+=[dirs.pop(0)]
    return totn
def box(d:dict)->tuple:
    INF=999999999
    x1=INF;y1=INF
    x2=-INF;y2=-INF
    for e in d:
        x,y=e
        if x<x1:x1=x
        if x>x2:x2=x
        if y<y1:y1=y
        if y>y2:y2=y
    return x1,y1,x2,y2
def cnt(d:dict)->int:
    x1,y1,x2,y2=box(d)
    r=0
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if (x,y) not in d:r+=1
    return r
res0 = 110
res1 = 3757
res0_2 = 20
res1_2 = 918
inp000s=""".....\n..##.\n..#..\n.....\n..##.\n"""
inp000={(2, 1): 1, (2, 2): 1, (2, 4): 1, (3, 1): 1, (3, 4): 1}
res001={(2, 0): 1, (2, 2): 1, (2, 4): 1, (3, 0): 1, (3, 3): 1}
inp00={(0, 2): 1,(0, 4): 1,(0, 5): 1,(1, 3): 1,(1, 5): 1,(1, 6): 1,(2, 1): 1,(2, 4): 1,(3, 1): 1,(3, 4): 1,(3, 5): 1,(4, 0): 1,(4, 1): 1,(4, 2): 1,(4, 4): 1,(4, 6): 1,(5, 3): 1,(5, 5): 1,(6, 1): 1,(6, 2): 1,(6, 3): 1,(6, 5): 1}

import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(inp000,parse(inp000s))
    def test_001(self):
        d=parse(inp000s)
        dirs=['N','S','W','E']
        aprint(inp000s)
        scan(d,dirs)
        self.assertEqual(['S','W','E','N'],dirs)
        self.assertEqual(res001,d)
        scan(d,dirs)
        self.assertEqual(parse(""".....
..##.
.#...
....#
.....
..#.."""),d)
        scan(d,dirs)
        self.assertEqual(parse("""..#..
....#
#....
....#
.....
..#.."""),d)
        self.assertEqual((0,0,4,5), box(d))
        self.assertEqual(25, cnt(d))
    def test_100(self):
        d=fparse("input0")
        self.assertEqual(inp00,d)
        dirs=['N','S','W','E']
        for i in range(10):
            scan(d,dirs)
        self.assertEqual(res0, cnt(d))
    def test_110(self):
        d=fparse("input1")
        dirs=['N','S','W','E']
        for i in range(10):
            scan(d,dirs)
        self.assertEqual(res1, cnt(d))
    def test_200(self):
        d=fparse("input0")
        dirs=['N','S','W','E']
        totn=0
        for i in range(1,10000):
            totn=scan(d,dirs)
            if totn==0:break
        self.assertEqual(res0_2, i)
    def test_210(self):
        d=fparse("input1")
        dirs=['N','S','W','E']
        totn=0
        for i in range(1,10000):
            totn=scan(d,dirs)
            if totn==0:break
        self.assertEqual(res1_2, i)
