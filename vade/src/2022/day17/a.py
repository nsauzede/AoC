from Monitor import *
import inspect
#monitor = Monitor()
D='.';F='-';H='#';L='<';R='>'
WW=7
verbose=False
def aprint(s:str,end='\n'):
    if verbose:print(s,end=end)
#verbose=True
def load(name):return open(name,"rt").read().strip()
import unittest
res0 = 3068
res1 = 3235
res0_2 = 0
res1_2 = 0

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
def startpos(m:dict,shape:list)->tuple:
    monitor.enter(inspect.currentframe().f_code.co_name)
    y2=sorted(m,key=lambda key:key[1],reverse=True)[0][1]
    y=len(shape)+y2+3
    monitor.exit(inspect.currentframe().f_code.co_name)
    return 2,y
def mkmap()->dict:
    return {(0,0):F,(1,0):F,(2,0):F,(3,0):F,(4,0):F,(5,0):F,(6,0):F}
def hit(m:dict,shape:list,x0:int,y0:int)->bool:
    monitor.enter(inspect.currentframe().f_code.co_name)
    for y,row in enumerate(shape):
        for x,c in enumerate(row):
            if c==H:
                #aprint(f"Checking {x0+x,y0-y}..")
                if (x0+x,y0-y) in m:
                    monitor.exit(inspect.currentframe().f_code.co_name)
                    return True
    monitor.exit(inspect.currentframe().f_code.co_name)
    return False
def rest(m:dict,shape:list,x0:int,y0:int)->bool:
    monitor.enter(inspect.currentframe().f_code.co_name)
    for y,row in enumerate(shape):
        for x,c in enumerate(row):
            if c==H:
                m[(x0+x,y0-y)]=H
    monitor.exit(inspect.currentframe().f_code.co_name)
    return False
def fall(m:dict,shapes:list,si:int,jets:str,ji:int)->tuple:
    monitor.enter(inspect.currentframe().f_code.co_name)
    monitor.enter('A0')
    nj=len(jets)
    ns=len(shapes)
    shape=shapes[si]
    x,y=startpos(m,shape)
    w=len(shape[0])
    monitor.exit('A0')
    monitor.enter('A1')
    while True:
        #monitor.enter('A0')
        c=jets[ji]
        ji=(ji+1)%nj
        if c==R and x+w<WW:
            if not hit(m,shape,x+1,y):
                x+=1
        elif c==L and x>0:
            if not hit(m,shape,x-1,y):
                x-=1
        #aprint(f"c={c} x,y={x,y} ji={ji}")
        if hit(m,shape,x,y-1):
            #monitor.exit('A0')
            break
        y-=1
        #monitor.exit('A0')
    monitor.exit('A1')
    monitor.enter('A2')
    #aprint(f"x,y={x,y}")
    rest(m,shape,x,y)
    si=(si+1)%ns
    monitor.exit('A2')
    monitor.exit(inspect.currentframe().f_code.co_name)
    return si,ji
def draw(m:dict):
    x1,y1,x2,y2=box(m)
    print('')
    for y in range(y2,y1-1,-1):
        for x in range(x1,x2+1):
            c=D
            if (x,y) in m:c=m[(x,y)]
            print(c,end='')
        print('')
def countunits(m:dict)->int:
    x1,y1,x2,y2=box(m)
    return y2
#@unittest.skip
class T000(unittest.TestCase):
    def test_fall10(self):
        m=mkmap()
        inp=load("input0")
        si,ji=0,0
        global monitor
        monitor=Monitor()
        #monitor.enter(inspect.currentframe().f_code.co_name)
        for n in range(2022):
            si,ji=fall(m,shapes,si,inp,ji)
            #draw(m)
            #print(f"Rock {n} count={countunits(m)} ji={ji}")
            #if n==15:break
        #monitor.exit(inspect.currentframe().f_code.co_name)
        monitor.print_all()
        self.assertEqual(res0,countunits(m))
@unittest.skip
class T9900(unittest.TestCase):
    def test_startpos0(self):
        m=mkmap()
        pos=startpos(m,shapes[0])
        self.assertEqual((2,4),pos)
    def test_startpos1(self):
        m=mkmap()
        inp=load("input0")
        self.assertEqual((1,4),fall(m,shapes,0,inp,0))
        pos=startpos(m,shapes[1])
        self.assertEqual((2,7),pos)
    def test_hit0(self):
        m=mkmap()
        self.assertEqual(False,hit(m,shapes[0],2,1))
        self.assertEqual(True,hit(m,shapes[0],2,0))
    def test_fall0(self):
        m=mkmap()
        inp=load("input0")
        si,ji=fall(m,shapes,0,inp,0)
        self.assertEqual(map001,m)
        self.assertEqual(1,si)
        self.assertEqual(4,ji)
        si,ji=fall(m,shapes,si,inp,ji)
        draw(m)
        self.assertEqual((2,8), (si,ji))
    def test_fall01(self):
        m=mkmap()
        inp=load("input0")
        si,ji=0,0
        ns=len(shapes)
        n,t=10,17
        for i in range(0,n):
            si,ji=fall(m,shapes,si,inp,ji)
        draw(m)
        x1,y1,x2,y2=box(m)
        self.assertEqual(t,y2)
        self.assertEqual(n%ns,si)
    def test_fall11(self):
        m=mkmap()
        inp=load("input1")
        si,ji=0,0
        for i in range(2022):
            si,ji=fall(m,shapes,si,inp,ji)
        x1,y1,x2,y2=box(m)
        self.assertEqual(res1,y2)
    def test_000(self):
        m=mkmap()
        self.assertEqual(map000,m)
    def test_box0(self):
        self.assertEqual((0,0,6,0),box(map000))
        self.assertEqual((0,0,6,1),box(map001))
map000={(0,0):F,(1,0):F,(2,0):F,(3,0):F,(4,0):F,(5,0):F,(6,0):F}
map001={
(2,1):H,(3,1):H,(4,1):H,(5,1):H,
(0,0):F,(1,0):F,(2,0):F,(3,0):F,(4,0):F,(5,0):F,(6,0):F,
}
shapes=[
["####"],
[".#.","###",".#."],
["..#","..#","###"],
["#","#","#","#"],
["##","##"],
]
