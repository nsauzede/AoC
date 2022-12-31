from Monitor import *
import inspect
def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):mat+=[row.copy()]
    return mat
def load(name):return open(name,"rt").read()
def rowstr(r:list, w=28)->str:return "".join(r)[:w]
def strmap(inp:str)->list:
    return [[c for c in s] for s in inp.split("\n")][:-1]

def mapstr(m:list,y0=0)->str:return "\n"+"\n".join(['|'+s+'|' for s in ["".join(str(i) for i in sublist) for sublist in m[y0:]]])+"\n"+f"+{'-'*ww}+"

def set(m:list,x:int,y:int,ch:str):m[y][x] = ch
def get(m:list,x:int,y:int):return m[y][x]

def grow(m:list,x:int,y:int):
    while y<0:
        m.insert(0,['.']*ww)
        y+=1
    return m,x,y

def putshape(m:list,s:list,x:int,y:int,ch='@')->(list,int,int):
    for j,r in enumerate(s):
        for i,c in enumerate(r):
            if c=='#':
                if ch=='#'or 1==1:set(m,x+i,y+j,ch)
    return m,x,y

def draw(m:list,y0=0,s=None,x=None,y=None)->str:
    if s:m=copy.deepcopy(m);putshape(m,s,x,y)
    st=mapstr(m,y0)
    print(st)
    return st

def firstrock(m:list)->int:
    for y,r in enumerate(m):
        if '#' in r:y-=1;break
    return y

def shapefits(m:list,s:list,x:int,y:int)->int:
    monitor.enter(inspect.currentframe().f_code.co_name)
    h=len(m)
    for j,r in enumerate(s):
        for i,c in enumerate(r):
            if c=='#':
                if x+i<0 or x+i>=ww:
                    monitor.exit(inspect.currentframe().f_code.co_name)
                    return 1
                if y+j>=h:
                    monitor.exit(inspect.currentframe().f_code.co_name)
                    return 2
                if get(m,x+i,y+j)!='.':
                    monitor.exit(inspect.currentframe().f_code.co_name)
                    return 3
    monitor.exit(inspect.currentframe().f_code.co_name)
    return 0

def mkgame()->list:
    return mkmat(['.']*ww,hh)

def findtop(m:list,s:list)->int:return firstrock(m)-3-len(s)+1
def countunits(m:list)->int:return len(m)-firstrock(m)-1

def newshape(m0:list,s:list)->(list,int,int):       # returns enlarged map and x&y coords where the shape has been added
    monitor.enter(inspect.currentframe().f_code.co_name)
    y=findtop(m0,s)
    monitor.exit(inspect.currentframe().f_code.co_name)
    return grow(m0,x00,y)

def pushright(m:list,s:list,x:int,y:int)->(list,int,int):
    monitor.enter(inspect.currentframe().f_code.co_name)
    if shapefits(m,s,x+1,y)==0:x+=1
    monitor.exit(inspect.currentframe().f_code.co_name)
    return m,x,y

def pushleft(m:list,s:list,x:int,y:int)->(list,int,int):
    monitor.enter(inspect.currentframe().f_code.co_name)
    if shapefits(m,s,x-1,y)==0:x-=1
    monitor.exit(inspect.currentframe().f_code.co_name)
    return m,x,y

def falldown(m:list,s:list,x:int,y:int)->(list,int,int,bool):
    monitor.enter(inspect.currentframe().f_code.co_name)
    ch='@'
    ret=shapefits(m,s,x,y+1)
    if ret==0:y+=1
    elif ret>=2:
        ch='#'
        putshape(m,s,x,y,ch)
    monitor.exit(inspect.currentframe().f_code.co_name)
    return m,x,y,ch=='#'

res0 = 3068
res1 = 3235
res0_2 = 0
res1_2 = 0
import copy
import unittest
#@unittest.skip
class T310(unittest.TestCase):
    def test_015inp_example0(self):
        m0=mkgame()
        nc=0
        global monitor
        monitor = Monitor()
        #monitor.enter(inspect.currentframe().f_code.co_name)
        for n in range(2022):
            shape=shapes[n % len(shapes)]
            m,x,y=newshape(m0,shape)
            rest = False
            while not rest:
                ch=inp00[nc % len(inp00)]
                nc+=1
                if ch=='>':
                    m,x,y=pushright(m0,shape,x,y)
                elif ch=='<':
                    m,x,y=pushleft(m0,shape,x,y)
                m,x,y,rest=falldown(m0,shape,x,y)
                if rest:break
            #draw(m)
            #ji=nc % len(inp00)
            #print(f"Rock {n} count={countunits(m)} ji={ji}")
            #if n==15:break
            m0=m
        #monitor.exit(inspect.currentframe().f_code.co_name)
        monitor.print_all()
        self.assertEqual(res0,countunits(m))
@unittest.skip
class T320(unittest.TestCase):
    def test_015inp_example0(self):
        m0=mkgame()
        nc=0
        for n in range(2022):
            shape=shapes[n % len(shapes)]
            m,x,y=newshape(m0,shape)
            rest = False
            while not rest:
                ch=inp10[nc % len(inp10)]
                nc+=1
                if ch=='>':
                    m,x,y=pushright(m0,shape,x,y)
                elif ch=='<':
                    m,x,y=pushleft(m0,shape,x,y)
                m,x,y,rest=falldown(m0,shape,x,y)
                if rest:break
            #print(f"Rock {n} count={countunits(m)}")
            m0=m
        self.assertEqual(res1,countunits(m))
@unittest.skip
class T010(unittest.TestCase):
    def test_001newShape(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        self.assertEqual((x00,hh-y00-1),(x,y))
        s=draw(m,y,shape,x,y)
        s0="\n|..@@@@.|\n|.......|\n|.......|\n|.......|\n+-------+"
        self.assertEqual(s0,s)
    def test_002pushRight1(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        s=draw(m,y,shape,x,y)
        s0="\n|...@@@@|\n|.......|\n|.......|\n|.......|\n+-------+"
        self.assertEqual(s0,s)
    def test_003fallDown(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        s=draw(m,y,shape,x,y)
        s0="\n|...@@@@|\n|.......|\n|.......|\n+-------+"
        self.assertEqual(s0,s)
    def test_004pushRight2(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        s=draw(m,y,shape,x,y)
        s0="\n|...@@@@|\n|.......|\n|.......|\n+-------+"
        self.assertEqual(s0,s)
    def test_005fallDown2(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        s=draw(m,y,shape,x,y)
        s0="\n|...@@@@|\n|.......|\n+-------+"
        self.assertEqual(s0,s)
    def test_006pushRight3(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        s=draw(m,y,shape,x,y)
        s0="\n|...@@@@|\n|.......|\n+-------+"
        self.assertEqual(s0,s)
    def test_007fallDown3(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        s=draw(m,y,shape,x,y)
        s0="\n|...@@@@|\n+-------+"
        self.assertEqual(s0,s)
    def test_008pushLeft(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushleft(m0,shape,x,y)
        s=draw(m,y,shape,x,y)
        s0="\n|..@@@@.|\n+-------+"
        self.assertEqual(s0,s)
    def test_009fallDown4(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushright(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(False,rest)
        m,x,y=pushleft(m0,shape,x,y)
        m,x,y,rest=falldown(m0,shape,x,y)
        self.assertEqual(True,rest)
        s=draw(m,y)
        s0="\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
    def test_010inp_basic(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        for ch in ">>><":
            if ch=='>':m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        s=draw(m,y)
        s0="\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
    def test_011inp_basic2(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        for ch in ">>><":
            if ch=='>':m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        s=mapstr(m,y)
        s0="\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
        m0=m
        shape=shapes[1]
        m,x,y=newshape(m,shape)
        for ch in "<><>":
            if ch=='>':
                m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':
                m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        s=draw(m,y)
        s0="\n|...#...|\n|..###..|\n|...#...|\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
    def test_012inp_basic3(self):
        m0=mkgame()
        shape=shapes[0]
        m,x,y=newshape(m0,shape)
        for ch in ">>><":
            if ch=='>':m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        s=mapstr(m,y)
        s0="\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
        m0=m
        shape=shapes[1]
        m,x,y=newshape(m,shape)
        for ch in "<><>":
            if ch=='>':
                m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':
                m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        s=draw(m,y)
        s0="\n|...#...|\n|..###..|\n|...#...|\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
        self.assertEqual(4,countunits(m))

        m0=m
        shape=shapes[2]
        m,x,y=newshape(m,shape)
        s=draw(m,y,shape,x,y)
        s0="\n|....@..|\n|....@..|\n|..@@@..|\n|.......|\n|.......|\n|.......|\n|...#...|\n|..###..|\n|...#...|\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
        for ch in "><<<>":
            if ch=='>':
                m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':
                m,x,y=pushleft(m0,shape,x,y)
            s=draw(m,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            s=draw(m,y)
            if rest:break
        self.assertEqual(True,rest)
        s=draw(m,y)
        self.assertEqual(6,countunits(m))

        m0=m
        shape=shapes[3]
        m,x,y=newshape(m,shape)
        s=draw(m,y,shape,x,y)
        s0="\n|..@....|\n|..@....|\n|..@....|\n|..@....|\n|.......|\n|.......|\n|.......|\n|..#....|\n|..#....|\n|####...|\n|..###..|\n|...#...|\n|..####.|\n+-------+"
        self.assertEqual(s0,s)
        for ch in "><>>><<":
            if ch=='>':
                m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':
                m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        self.assertEqual(7,countunits(m))

        m0=m
        shape=shapes[4]
        m,x,y=newshape(m,shape)
        s=draw(m,y)
        for ch in "<>>>":
            if ch=='>':
                m,x,y=pushright(m0,shape,x,y)
            elif ch=='<':
                m,x,y=pushleft(m0,shape,x,y)
            m,x,y,rest=falldown(m0,shape,x,y)
            if rest:break
        self.assertEqual(True,rest)
        self.assertEqual(9,countunits(m))

    def test_013inp_adv1(self):
        m0=mkgame()
        for n in range(2):
            shape=shapes[n % len(shapes)]
            m,x,y=newshape(m0,shape)
            s=draw(m,y)
            rest = False
            nc=0
            while not rest:
                ch=inp00[nc % len(inp00)]
                if ch=='>':
                    m,x,y=pushright(m0,shape,x,y)
                elif ch=='<':
                    m,x,y=pushleft(m0,shape,x,y)
                m,x,y,rest=falldown(m0,shape,x,y)
                if rest:break
                nc+=1
            m0=m
        self.assertEqual(4,countunits(m))

    def test_014inp_adv2(self):
        m0=mkgame()
        nc=0
        for n in range(5):
            shape=shapes[n % len(shapes)]
            m,x,y=newshape(m0,shape)
            rest = False
            while not rest:
                ch=inp00[nc % len(inp00)]
                nc+=1
                if ch=='>':
                    m,x,y=pushright(m0,shape,x,y)
                elif ch=='<':
                    m,x,y=pushleft(m0,shape,x,y)
                m,x,y,rest=falldown(m0,shape,x,y)
                if rest:break
            m0=m
        self.assertEqual(9,countunits(m))

    def test_015inp_adv3(self):
        m0=mkgame()
        nc=0
        for n in range(10):
            shape=shapes[n % len(shapes)]
            m,x,y=newshape(m0,shape)
            rest = False
            while not rest:
                ch=inp00[nc % len(inp00)]
                nc+=1
                if ch=='>':
                    m,x,y=pushright(m0,shape,x,y)
                elif ch=='<':
                    m,x,y=pushleft(m0,shape,x,y)
                m,x,y,rest=falldown(m0,shape,x,y)
                if rest:break
            m0=m
        self.assertEqual(17,countunits(m))

def parse(s:str)->list:
    scan=[]
    for line in s.splitlines():
        pass
    return scan
ww=7
hh=6
x00=2
y00=3
inp00=">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
inp10="><<<>>>><<<>>>><>><<><<>>>><<<<>><<>><<<>>>><<<>>>><<<<>>><>>><<>>><<>>>><<>>>><>><>><<>>>><><<<<>>>><><>>><>>>><>>>><<>>>><><<<>>><<<<>><<<><<<<>>>><<>>><<<>>><><<>>><<<<>>><<<<>>><<<<>>>><<<><<<<>><>><<<>>>><><<<<><><><<>>><><>>><>>>><<<<><>>>><<>><<>>>><<>><<<>>>><<>>>><<>><<<>>>><<<<>>><<><<<<>>><<<>><><<<<>><<>><><<><<><>>>><<><<<>><<>>>><<<><<<>>><<<<>>><<<>>>><<<<><<>><<>>><>><<<>>><<<>>><<>><>><<>>>><<>>><<<<>><<<<>>><>>><>>>><<<>>><<<><>><<<>><<<>>>><<<><<<<><<>><>><<<>><>>><<>>><<<><<><><>>><<<<><<<<><<><<><<<<>><<<>>><<<>><<>><<<>><>>><<<>>><<>><<<<><<<<>><<<><>><<>><><<>><<<>><<>>><<<<><><>><<>>>><<<<><<<>><<<><<<<>>>><<<<><<<>>><<><<<<><<<<>>><<><<<>>>><>>>><<>>><><<>><<<<>><>>><<<>>>><<><<<><<<>><<>>><<<>><<<>>>><<<<>>>><>><><>>><<<>>><<<>>>><<<><<<<>>>><<><<<<>>>><<<<>>><<<>><><<><<<<><><<>>>><<<<>><>>><<<>><<<<><>>><><<>>><>>><<>>>><>><<>>><>>>><><<>>><<<>>>><<<>>><>>><<<>>>><<>>>><<<<>>><>><<<><<><>>>><<<>>><<>><<<<>>><<><<<<>>><<<>>><<<>>><>>><<><<<>><<<<>>>><>>><<<>>>><<>>><<<<><<<>><<<><<<<><<>>>><<>><>>><<>>>><<<<>>>><<<>>><<>>><<<>><<><>>>><<>>>><<>>>><>>><<>>>><<>><<><<>><<<<>><<<><<>>>><<>><<<<>>>><<<<>>>><<<>><>>><<<>>><>>>><<<<><<<>><>>><<<<><<<<><<<>><>>>><>><<<<><<>>>><<<<>>><<<<>><<<>>>><<>>>><>><<>>>><<<<>>><<>>><>>><<<<>><>>><<<<>>><<>>>><<>>><<><>>><<<<>>><<<><<<<>>>><<>>><><>>><<>>>><<>>>><<>><><>>>><<<<>>>><>><>>>><<<>>>><>>>><<>>><<<<>>><<<>><><<<><<><<<<>>><<><<>><<<<>><><><<<>>>><<<<>><><<<>>>><><<<>>>><>>>><<<<>><<<><<>>><<<<>>><<>>>><<<<>>><>><<<><<>><<>>>><>>>><<>>><<>>>><<<>><>><<<>>><<<<>>>><<>><<<<>>><<<<>><<>>><<<>>>><>>><<<<>>>><<>>>><<>>><><<<><>><<>>>><<<>>>><<<>><>><<<>><<><<<>>>><<><<>><<<<><<>><<<><><<<<>>><<>>>><<><<<><<<<>>><<<>>><<>><><<<><<>><<>><<<><>>><<<<>>>><<>>><><<<<>>><<>><<<>>>><><<<<><<<>>><>>><<<<><<<<>>><<<<>><<<<><<><<>><<<><<<>><<<><><<>>><>><<<<>>><<>><<>><<<>>>><<<<>><<<<><>>>><<><>><<<<><<<>>><<<<><<><<<>>><<<><><>>>><<>>>><>><<<<><<<>><<<><>>><<>><<<><<<<>>><>>><<<>><<<<><>><<<><<<>>><>>>><>>><<><<>>><<>><<><<<<>>>><<>><<>>>><>>>><<><<<><<<<>>>><<<>>><<<>>><<<<>><<<>>>><>>><<><<<<>>>><<<>>>><<><<<<>>><<<>><><<<<>>>><<<<>>><>>><<>>><>>>><<<<>>><<<>><<>><<<>><<<>>><>>><><<>><<<>><<><<<>><><<>>><<><<>>><<><<<<>>>><>>>><<>>>><<<<>>><<<<><>><<><<<>><>><<>><<>>><<<>><<>><>>><<<<><<<><<<<><>>>><<><<>><<>>><<<>><<<<>>><<<<><<<>>>><<><<>><<<<><<<<>><>>><<><<<>><<<>><<<>>><><<><><<<<>>>><<<>><<<><<<<>>>><<<>>>><<<<>>>><<<<>><<<>>>><>><<<><><<<><<<<><><<<<><<<<><<<<><<<<>>>><<>>><<<<>>><><<<>>><<<>><<<<>>><<<>><>>>><<<<>>>><<<>><<<>>>><<<>><>>><>>>><<<<>><<<>>><<>><<<<>>><<<<>>>><>>><<<<><>>>><<<>>>><<<>><<<>>><<><<>><<<<>>><<<<>><<<>>><<>><<>>><<<>><<>>>><<<>><<<>>><<>>><<<<>>><>>>><><<<<>>><>>>><<<>>><>><<<<>>><<<>><<<>>>><<>>>><<><<<<>>>><<<<>>>><<>>>><<<><<>>>><<><<>>>><>>><<<<><<>>>><>>>><<<<><<<>>>><<<>><>>><<<<>>><<><<<<>><>>><<<<>>>><><<<>>><<<<>><>><>><<<<>>><<<<>>>><<>>>><<<>>>><>>><<<>>><<<<>><<<><<<>><<<><>><<<>>>><<<><>>>><>><<<<>><>>><><<<<>>>><<>>><<<<>>>><<<>>><<<>><<<>>><><>><<<>><<>>><<<<><<><<<>>>><<<<><<><<<<>>><<>>>><>><<>>><<<<>>><<>>><<>>><<<<>>><>><<<>>><<>>>><<<>><<<<>><<>>>><<<><>>>><<>>><<><<<<><>>><>>><<<>>><>>>><<<<>>>><<<<>>><<<>>>><>>>><<>>>><<<>>><<<<><<>>><<>>>><<<>>>><<<<>><<<<>><<><>><<<<>><>>>><<><<<>>><>><>>><<<<>><<<><<<>>><<<<><>>><<>>>><>>><<<<>>><>><<>><>>><<>>>><<>><<<<>><<>>><<<>>>><<<><<<><<>>><<<<>>>><<>><<<><<>><<>><<<<>>><<<<>>><<<<>>><>>><><<><<<<><<<<>>><<<>>>><<<>>><>>>><<<<>><<><>>>><<<<><<<<><<<<>>><<<<>>>><<<<>>><<<<><<<<>><<<<>><>><<<<>><<<>>><<>><<<>><<<<>>><<<>>><<>>><<<>><<><<<>>><<><<<<>>>><<<<>>><<<>><>><>>>><<>>>><<<<>>><<><<<<>><<<><<<<>>>><><<<<>>>><<<<>><<>>>><>>>><<>>><<<>>>><<<<>>>><<>><<>>><<<<>>><<><><>>><>>>><<<<>>><>>>><<<<>><<<<><<<>><<<<>><<>>><><<><<>><<<<>>>><<<>><<>><<<>>>><>>><<<>>>><><>>>><<<>>>><<><<<<><<<<>>>><>>>><<<>>><>>>><<<<>><>><>><<<<><<>>><<<<>>>><<><<<>>>><<>><<>>><<<><<<><<<<><><<>>><<>><<<>>>><<<<><>>><><><><<<>>>><<<><<<<><>><><<<<><<<>>>><<><>><<>>><<<<>>>><<>><<<>><<<<>><<<<><<>>><>><<<<>>>><>>><><>><>><<>>><>><<<>>><<<<>>>><<><<<<>>>><<<<>>>><><<>>>><<>>>><>><<>><<<<>>>><>><<<<>>><<>><<<>>><<<<><<><<>>>><><>>>><<<<>>><>><<<<>><<<>><<<>>><<<<>>><<>><<<>>><<<<>>><<<<><<>>>><><<>>>><<<><<<<>>>><>><<<<>><<<<>>><<>><<<<>>>><<>>><>>><<<>>><<<<>>><<<<><<<>><>>>><><<><<><<><<>>><<<>>>><<<<>><<<<>>>><<>>>><>>><>>><>><<><<<>>>><>>><<<>><>>>><>>><>>>><<<<>><>>><<<<>>>><><<<><<<>>><<<>>>><<<<>><>><<<<>>><<<<><<>><<><<><<>>><<>>>><<<<>>>><<><<><<<>><<<>><<>>><<<><><>>>><>>><<<<>>><<>><<>>><<<<>>><<<><<>><<<>><<<<>>>><>>>><<><>>>><<<<>>>><<<<>>><<>>><<>>><><>><><<<<><<>>>><<><>><<<><<<<>><<>><<>>><><>>><<><<<<>>>><>>>><><<<><<<>><<<>>><>>>><<<<>><<>>>><>>>><>><<>>><<<><<>>>><>><>><><<<><>><<>>><<<><>>><<<>>>><<<><<>>><<<>><<<>><<>><<<<><<<<>><>><<<>>>><><<<>>>><<<<>>>><<<<>>><<<><<<<>>>><<><<<>>><<<>>><>>>><>>><<<<><<<<>>><><<>>>><<<><<>><<<<>><<>>>><<><<<<><<><<>>>><<<>>><>>><>>>><<<>>>><<<>><><<<>><<<>><<><<>>><><<<<>>>><>>><>>><<<><<>>>><<<>>>><<>><>>>><<<<>>><><><<<<><<<<>>>><<<>><>>>><>>><<<<>>><<<<>>><><<>>><<>>><<<<><<>>><>><<<>>><<<><<<<>>>><><<<><<><><<<>>><<>>><<<<><<<>>><<<><>><<><<>>><<<<>>>><>>>><<><<<>><>>>><<><<>>>><<<<><>>><>>>><<>>>><<<<>>><<<<>>><<><<><<<<>><<>>><<<<>><<<<>><<<>>>><<<<>>><<>>>><<<>>><<<><<<<>>><<<>>><>><<<>><<>>>><>>>><<<<>>><>>>><<<>>>><<<<>>>><<<>><<>><<<<><<<<><<<<><<<>>><<><<<<>>>><<><>><<<<>>><<>><><<<>>><<<><>>><<<<><<>>>><<<>>>><><><<<>><<<<>>><<>><<>>><<<>><<<>><<>>>><<<><><<><<<>><><>><<<>><<>>>><<><<<<>><<><<<<>><>>><<>>>><<>><>>>><<<>>><<>>><>>>><<>>><<<>>><><<>><>>><<<<>>>><<<>>><<<<>>>><<>>><<<<><<<>>>><>><<<><>>><<>><<<>>><<<><<<<>><<>>><<>><><<>><<<>><<<>>>><<<<>><><<<<><>>>><<>>>><<><<>><<>><<<><<>>>><<<>><<>>><<<>><>>>><<<>><<<<>><<>><<<<>>>><><<>>><<><>>><<<>>>><<>>><>>><<<<><<<>>><<>><<>><<>><<<>>>><<<>><<>>><<<<>>>><><<<>>>><<<<>><>>><<>><<<<><<<>>>><>><>><<<>><>>><<<>>><<<<>><<>>>><><<<>>>><<<>><<<>>>><<>>>><<>><<<>>>><>>>><>>><>>>><><>>>><<<<>><<<>>>><>><<<>>><<<><<<<><<<><<<><<<<>>>><<>>>><><<<>><<>>>><<><<<<>>>><>>><><<<<>>><<<>><<<<>><<<<>>>><<<>>><>><<<<>>>><<>><<><<>>><<<<>>>><<<<><<>><<<>><<<<>><<>>><><<>>><>>><<<<>>><<><<>>><<<<>><><<<>><<<<><<>><<><<<>><<<<>>><<<<>>><<<<><<>><>>><<>>><>>>><>><<<<>><<<<>><<<>><>>>><>><<<>>>><<<<>>><<<>>>><<><><><<<<>>>><<<>>><<<<>>>><<<<>><<>><<<>>>><<>><<><<>><<<<>>><<<>>><<<>>>><<<><<><>>><<<>>><<<>><<<><<>><<<<>><>><<<>><<<<>>><><<<><>><><<<<>>>><<>>>><<<>>><<<<>>><<<<><>><<>>>><>>><<<>>>><><<>>><<<>>>><<<>>>><<<<>>>><<<<>>><<<<>>>><<><<<<><<<>><>>>><<<<><><<>>><<>>>><<<<>><<<<>>><<<><><><>><<<>>><<<<><>><<<>>>><<<>><>><<<<>>><<><>>>><><<<><>><<<>>><<<<>><<>>><>>><<>><<>>><>>><<<><><<<<><<<><<><<<><<>><>>><>><<<<><<<>><>><<><<>>>><>>><>>>><>>>><<<<>>><>>>><<>>><<>>>><<<>><<<<>><<><<>><<<<>><<><<<>>><>><<>><<<<>><>><><<<>>>><<<>>><<>>>><>><<<<>><>>>><<>>><<>>><<<>><<<>>><<<<><<><<>><<<<>>>><<<<>><<>><>>>><<<<>>><<<<>>><<<><<<<>>>><<<<>><<<<>><>>><<<<>>><<<><<<<>>><<<<>><<<<>>>><<<<>>>><<<<>>>><<><>>>><<>>><<><>><<>>>><<><>><<>>>><<>>>><<>>>><<<<>><><>>>><<>>><<>>>><<<>>>><<<<>><<>><<>><<<><<<>>>><<<><>>><<<<>><<<<>>>><<<<>>>><<<><<<<><<<<>>>><>>>><>>>><<<<>><><<<><<<<>>><<><<<>><<<>>>><<<<>>>><<<>><<>>>><<>>>><<<<>><<<<>>><<<>>><<<>><<<>><>>><<<>>>><<<<>>>><<<>>>><>>><<<<>>>><<<<>>><<<>>><>><<<>><<<>><<<<>>><<<>>>><<><<><<<>>><<>>>><<<>>><<<>>><<>><<<<>>>><<><<><<>>><>>>><<>>>><<>>>><<<<>>>><<<<><<<<>>><>>>><<><>>><><<<><<<>><>><>>><<<>><<<<>>>><<<><><>>>><<>>><<>>>><<<>>>><><>>>><<<>><<<><<<>>>><<>>>><<>>>><<><<>>><>><<<>>><<<<>><<<<><><<<<>>>><<><>><<<>>>><><<<<>><>>>><<<>>><<<>><>><<<>><<><<<>>><<<>>><<><<>>><<<><<<>>>><<>>>><><<<<><<<<>>><><<<>>><<>>><<>><>><>>><<>>><<<>>>><<><<>>>><<<<>><<<><>><<<<><<<><><<>><<<<><<<>><<<<>>><<<<><<<<>>>><<<>><><>><<><<>>>><<><<<<>><<<>>><<<><<<>>>><<>><<<>>><>>><<>><<><<<<><>><<<<>><>><<<<><<<<><<<><>>>><<>>>><>><<>>>><<>><<>>><>>><<<>>>><<>>>><>><>>><<><<<>>><<><<><><<<<><>><<<>>><<>><<<>>><<<<>>><<<<>>><<<><><<<>>>><<<>>>><>><<>>>><>><>>>><<<>><<<<>>><<>>><<<>>><<<<>>><<<<><<>><><<<<>>>><<>><<<<>><<<><>>><<><>><>>>><<>><<<<>><<<>>><<<>>><<<<><<<<>><<<<>>>><<<>>><<><<<><<<<>><><<>><<<<>>><<><>>><<<<>>><<>><<>>>><<<<>>>><<<<>>>><>>>><<>>>><>>>><<><<><>>>><<><<<<>>>><<<><<<>>>><<>>>><<<<>>>><<<>>>><<<<>>><>>><<<><<<>><<>><<<<>><<>>><<>>><<>>><<<<><>>>><<>><<><<<<>>><<<<>>><<<<><<<<>>><<<>>>><>>>><<>>>><>>>><<>><<>>>><<<><<<<><>><<<<><<>>>><>>>><<<<>>><<>><<<<>>>><<>>><<>>>><<<<>>><<<<>>><<<<>><<<<>>>><<><<<<>><<<<>>>><<><><<<<><<<>>><<<<><<<>>><<<>><<<><<>>>><<<<>><<<<><<<<><<<<>>>><<><<>>>><<>><<<>>><<<>>>><<<>><<<>>><<>><>><<<<><<<<>><<<<><<>>>><<<<>><<<<>>>><<><<<<>>>><<><<<<><<>>><<><<<>>><<><<<<>>><<>><<<<><<<<><<<<><<><<<<>>>><<<<><<>>>><<<<>>>><>><<<<>>><>>><<<>>>><>>>><>>>><<<><>>><>><<<<>>>><<<<>><<<>>>><<<<>><<<<>>>><<<<>>>><><<<<>>>><<<>><<>>>><>>>><>>>><><<>>>><<><><<<><>>>><>>>><<<><<<>>>><<<<>>>><<<>>><<<<><<<><<>>>><<>>>><<>>><<<>><>><<<><<<<><<>>>><<<>><<>><>>>><>>>><<>>>><<<>>><>>><>>><<>><<><<<>><<>><<<<>>>><<>><<>>>><<<>><<<<>>><<<><<<<><<<<>>><>><<>><><<>><<<>><<<<>>>><<<><<>><>><<<><<>><<<<>>><<<>><<<<><<>>>><<>><<<<><<>>>><<<><>>><<><<<<>><<<<>><<>><<<<>>>><<><<<<>>><<<><<<>><<>>><<<<>>>><<><>>><<<>>><<>>><<<<>>><<<>><<<<>>><<<>>>><>>>><<>><<<<>><<>>>><<<<>>>><<>>>><<<<>><<>>>><>>>><>>><<<<>>><<<<><<<>>><<>><<<<>>><>><<<<><<<<><>>>><<<<>>>><>>>><<<<>>><<>><<<>>><<<>>><<<>>>><>>>><<<>>><<<<><<>>><<<<>>><<<<><<<<>>>><>><>>>><>>><>><<<<>>>><<>><<<>>>><<>><<>><<<<>><<<>>><<>>>><<<><<<>>><<<<>><<<<><>>>><<<<>><<<<><><<>>><<<>>>><<<<>>>><<<>>>><<>>>><<>><>><>>><<>><<<<>>>><<<>><<>><<<>>>><<<>><<<>><<<<>>><<<><<>><<<<>>>><<<<>><>>><<<>><<><<<>>><<<>>>><>>>><<<>>>><<<>><<>>>><>>>><><<<<>><<>><><>><<<<>>>><<>><<<<>>><<>><>>><<<>>><<<><<<>>><<<<>>><<>>>><<<>><<>><<>>><<<>>><>><<>><>><<<>>>><<<<>><>>><<>>><<<<>><<>><>>>><>><<<>>><<>>>><>>><><<>>>><<><<<<>>>><<<>>>><<<<><<>>><<<<><><<>>><>><>>>><<>><<<>>><<>>><<>>><<<<>><>>>><<<<>><<<<><<>>>><<<><<<<>>>><<>><<>>>><>>><<<><<<>>><<<<>>><<>>><<<<>><<<><<<<><<<>><<<<>><<>>><<<<><<<<><>>>><<<<>><<><>><<>><<>>>><><<<>>><<><>>>><<<><<<>><<<><<<>><<<<>>><<<>>>><<<>>><<>><<<"
shapes=[
["####"],
[".#.","###",".#."],
["..#","..#","###"],
["#","#","#","#"],
["##","##"],
]
