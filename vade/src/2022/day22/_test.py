R=0;D=1;L=2;U=3
def load(name):return open(name,"rt").read()
def parse(s:str)->tuple:
    m={};p=[]
    ispath=False
    y=1
    for line in s.splitlines():
        if not ispath:
            if line=='':
                ispath=True
                continue
            x=1
            for c in line:
                if c==' ':
                    pass
                elif c=='.' or '#':
                    m[(x,y)]=c
                else:
                    raise Exception(f"Unknown char '{c}'")
                x+=1
            y+=1
        else:
            aprint(f"line={line}")
            l=line.split("R")
            l1=[i for s in list(zip(l,[R]*len(l))) for i in s][:-1]
            aprint(f"l1={l1}")
            for e in l1:
                if 'L' in str(e):
                    l2=e.split('L')
                    aprint(f"l2={l2}")
                    p+=[int(i) for s in list(zip(l2,[L]*len(l2))) for i in s][:-1]
                else:
                    aprint(f"e={e}")
                    p+=[int(e)]
            break
    return m,p
def fparse(name):return parse(load(name))
def wrap_right(m:dict,p:tuple)->tuple:
    x,y=p
    while (x,y) in m:x-=1
    return (x+1,y)
def wrap_left(m:dict,p:tuple)->tuple:
    x,y=p
    while (x,y) in m:x+=1
    return (x-1,y)
def wrap_down(m:dict,p:tuple)->tuple:
    x,y=p
    while (x,y) in m:y-=1
    return (x,y+1)
def wrap_up(m:dict,p:tuple)->tuple:
    x,y=p
    while (x,y) in m:y+=1
    return (x,y-1)
def orig(m:dict)->tuple:
    y=1;x=1
    while True:
        if (x,y) in m:
            break
        x+=1
    return x,y
def rotate(facing:int,turn:int)->int:
    if facing==R:return D if turn==R else U
    if facing==D:return L if turn==R else R
    if facing==U:return R if turn==R else L
    if facing==L:return U if turn==R else D
    else:
        raise Exception(f"Kaboom facing={facing} turn={turn}")
def walk(m:dict,o:tuple,facing:int,n:int,d={})->tuple:
    x,y=o
    aprint(f"Walking n={n} from o={o} with facing={facing}")
    while n>0:
        if facing==R:
            d[(x,y)]='>'
            if (x+1,y) in m:
                if m[(x+1,y)]!='.':break
                x+=1
            else:
                np=wrap_right(m,(x,y))
                if m[np]!='.':break
                x,y=np
        elif facing==L:
            d[(x,y)]='<'
            if (x-1,y) in m:
                if m[(x-1,y)]!='.':break
                x-=1
            else:
                np=wrap_left(m,(x,y))
                if m[np]!='.':break
                x,y=np
        elif facing==D:
            d[(x,y)]='v'
            if (x,y+1) in m:
                if m[(x,y+1)]!='.':break
                y+=1
            else:
                np=wrap_down(m,(x,y))
                if m[np]!='.':break
                x,y=np
        elif facing==U:
            d[(x,y)]='^'
            if (x,y-1) in m:
                if m[(x,y-1)]!='.':break
                y-=1
            else:
                np=wrap_up(m,(x,y))
                if m[np]!='.':break
                x,y=np
        else:raise Exception(f"Kaboom facing={facing}")
        n-=1
    return x,y
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
def draw(d:dict):
    aprint(f"d={d}")
    aprint(f"box={box(d)}")
    x1,y1,x2,y2=box(d)
    print('')
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            p=(x,y)
            if p not in d:print(' ',end='');continue
            print(d[p],end='')
        print('')
def wander(m:dict,p:list,o=None,facing=R)->(tuple,int):
    if o==None:o=orig(m)
    d={}
    for k,v in m.items():
        d[k]=v
    o=walk(m,o,facing,p.pop(0),d)
    aprint(f"o={o}")
    while len(p)>0:
        facing=rotate(facing,p.pop(0))
        aprint(f"Popped facing={facing}")
        aprint(f"facing={facing}")
        o=walk(m,o,facing,p.pop(0),d)
        aprint(f"o={o}")
    draw(d)
    return o,facing
from math import sqrt
def facedim(m:dict):
    x1,y1,x2,y2=box(m)
    l=int(sqrt(len(m)//6))
    return l
def encode(o:tuple,facing:int)->int:
    x,y=o
    return y*1000+x*4+facing
verbose=False
def aprint(s:str):
    if verbose:
        print(s)
def wander2(m:dict,w:dict,p:list,o=None,facing=R)->(tuple,int):
    if o==None:o=orig(m)
    d={}
    for k,v in m.items():
        d[k]=v
    o,facing=walk2(m,w,o,facing,p.pop(0),d)
    aprint(f"o={o}")
    while len(p)>0:
        r=p.pop(0)
        facing=rotate(facing,r)
        aprint(f"Popped facing={facing}")
        c={R:"R",L:"L"}[r]
        aprint(f"facing={facing} {c}")
        o,facing=walk2(m,w,o,facing,p.pop(0),d)
        aprint(f"o={o}")
    #draw(d)
    return o,facing
def walk2(m:dict,w:dict,o:tuple,facing:int,n:int,d={})->tuple:
    x,y=o
    aprint(f"Walking n={n} from o={o} with facing={facing}")
    while n>0:
        if facing==R:
            d[(x,y)]='>'
            if (x+1,y) in m:
                if m[(x+1,y)]!='.':break
                x+=1
            else:
                np,f=w[(x+1,y,facing)]
                if m[np]!='.':break
                x,y=np;facing=f
        elif facing==L:
            d[(x,y)]='<'
            if (x-1,y) in m:
                if m[(x-1,y)]!='.':break
                x-=1
            else:
                np,f=w[(x-1,y,facing)]
                if m[np]!='.':break
                x,y=np;facing=f
        elif facing==D:
            d[(x,y)]='v'
            if (x,y+1) in m:
                if m[(x,y+1)]!='.':break
                y+=1
            else:
                np,f=w[(x,y+1,facing)]
                if m[np]!='.':break
                x,y=np;facing=f
        elif facing==U:
            d[(x,y)]='^'
            if (x,y-1) in m:
                if m[(x,y-1)]!='.':break
                y-=1
            else:
                np,f=w[(x,y-1,facing)]
                if m[np]!='.':break
                x,y=np;facing=f
        else:raise Exception(f"Kaboom facing={facing}")
        n-=1
        aprint(f"row={y-1} column={x-1}")
    aprint(f"facing={facing}")
    return (x,y),facing
"""
            1111111
   1234567890123456
 1         ...#
 2         .#..
 3         #...
 4         ....
 5 ...#.......#
 6 ........#..A
 7 ..#....#....
 8 .D........#.
 9         ...#..B.
10         .....#..
11         .#......
12         ..C...#.
"""
def mkw1(m:dict):
    l=facedim(m);w={}
    for i in range(l):
        w[(51+i,0,U)]=((1,151+i),R)#U face1=>face6
        w[(0,151+i,L)]=((51+i,1),D)#L face6=>face1
        w[(50,1+i,L)]=((1,150-i),R)#L face1=>face4
        w[(0,101+i,L)]=((51,50-i),R)#L face4=>face1
        w[(1+i,201,D)]=((101+i,1),D)#D face6=>face2
        w[(101+i,0,U)]=((1+i,200),U)#U face2=>face6
        w[(101,51+i,R)]=((101+i,50),U)#R face3=>face2
        w[(151,1+i,R)]=((100,150-i),L)#R face2=>face5
        w[(101,101+i,R)]=((150,50-i),L)#R face5=>face2
        w[(101+i,51,D)]=((100,51+i),L)#D face2=>face3
        w[(50,51+i,L)]=((1+i,101),D)#L face3=>face4
        w[(1+i,100,U)]=((51,51+i),R)#U face4=>face3

        w[(51,151+i,R)]=((51+i,150),U)#R face6=>face5
        w[(51+i,151,D)]=((50,151+i),L)#D face5=>face6
    return w
def mkw0(m:dict):
    l=facedim(m);w={}
    print(f"l={l} m={m}")
    for i in range(l):
        w[(13,5+i,R)]=((16-i,9),D)#R center face4
        w[(9+i,13,D)]=((4-i,8),U)#D center face5
        w[(5+i,4,U)]=((9,1+i),U)#U left face3
    return w
import unittest
#@unittest.skip
class T010(unittest.TestCase):
    def test_200_wander(self):
        m,p=fparse("input0");w=mkw0(m)
        o=orig(m)
        aprint(f"p={p} o={o}")
        #self.assertEqual((4,1),o)
        o,facing=wander2(m,w,p)
        print(f"o={o} facing={facing}")
        self.assertEqual(res0_2,encode(o,facing))
    def test_210_wander(self):
        m,p=fparse("input1");w=mkw1(m)
        o=orig(m)
        aprint(f"p={p} o={o}")
        #self.assertEqual((4,1),o)
        o,facing=wander2(m,w,p)
        print(f"o={o} facing={facing}")
        self.assertEqual(res1_2,encode(o,facing))
    def test_000(self):
        m,p=parse(inp000s)
        self.assertEqual((2,1),orig(m))
    def test_001_walks(self):
        m,p=parse(inp000s)
        self.assertEqual((3,1),walk(m,(2,1),R,3))
        self.assertEqual((2,2),walk(m,(2,1),D,3))
    def test_002_wander(self):
        m,p=parse(inp000s)
        self.assertEqual(((2,2),R),wander(m,p))
    def test_003_wander(self):
        m,p=fparse("input0")
        o,facing=wander(m,p)
        self.assertEqual(((8,6),R),(o,facing))
    def test_100_wander(self):
        m,p=fparse("input0")
        o,facing=wander(m,p)
        #print(f"o={o} facing={facing}")
        self.assertEqual(res0,encode(o,facing))
    def test_110_wander(self):
        m,p=fparse("input1")
        o=orig(m)
        aprint(f"p={p} o={o}")
        self.assertEqual((51,1),o)
        o,facing=wander(m,p)
        #print(f"o={o} facing={facing}")
        self.assertEqual(res1,encode(o,facing))
    def Ztest_201_wander(self):
        m,p=fparse("input0")
        self.assertEqual(4,facedim(m))
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        m,p=parse(inp000s)
        self.assertEqual((inp000m,inp000p),(m,p))
    def test_010_wrap_right(self):
        m,p=parse(inp000s)
        self.assertEqual((1,2),wrap_right(m,(2,2)))
    def test_011_wrap_left(self):
        m,p=parse(inp000s)
        self.assertEqual((3,1),wrap_left(m,(2,1)))
    def test_012_wrap_down(self):
        m,p=parse(inp000s)
        self.assertEqual((2,1),wrap_down(m,(2,2)))
    def test_012_wrap_up(self):
        m,p=parse(inp000s)
        self.assertEqual((2,2),wrap_up(m,(2,1)))

res0 = 6032
res1 = 43466
res0_2 = 5031
res1_2 = 162155
inp000s="""\
 ..
#.

10R5L5
"""
inp000m={
(2,1):'.',(3,1):'.',
(1,2):'#',(2,2):'.',
}
inp000p=[10,R,5,L,5]
inp00s="""\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
