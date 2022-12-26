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
res00 = 4890
res01 = "2=-1=0"
res1 = "2=-0=1-0012-=-2=0=01"
res0_2 = 0
res1_2 = 0
def dec(s:str)->int:
    d={'2':2,'1':1,'0':0,'-':-1,'=':-2}
    r=0
    l=len(s)
    for i,c in enumerate(s):
        n=pow(5,l-i-1)
        v=n*d[c]
        r+=v
        print(f"i={i} c={c} n={n} v={v}")
    return r
"""
0 0          0*5+0*1
1 1          0*5+1*1    1
2 2          0*5+2*1    1
3 1=         1*5-2*1    2
4 1-         1*5-1*1    2
5 10         1*5+0*1    2
6 11         1*5+1*1    2
7 12         1*5+2*1    2
8 2=         2*5-2*1    2
9 2-         2*5-1*1    2
10 20        2*5+0*1    2
11 21        2*5+1*1    2
12 22        2*5+2*1    2
13 1==  1*25-2*5-2*1    3
14 1=-  1*25-2*5-1*1    3
15 1=0  1*25-2*5+0*1    3
16 1=1  1*25-2*5+1*1    3
17 1=2  1*25-2*5+2*1    3
18 1-=  1*25-1*5-2*1    3
19 1--  1*25-1*5-1*1    3
20 1-0  1*25-1*5+0*1    3
21 1-1  1*25-1*5+1*1
22 1-2  1*25-1*5+2*1
23 10=  1*25+0*5-2*1
24 10-  1*25+0*5-1*1
25 100  1*25+0*5+0*1    3
26 101                  3
27 102
28 11=
29 11-
30 110
31 111
32 112
33 12=
34 12-
35 120
36 121
37 122                  3

62 222  2*25+2*5+2*1    3
63 1=== 1*125-2*25-2*5-2*1      4

i=5 t=3125 d=1
i=4 t=625 d=7
i=3 t=125 d=39
i=2 t=25 d=195
i=1 t=5 d=978
i=0 t=1 d=4890
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       20            1-0
"""
from math import log, ceil, floor
def enc(v:int)->str:
    if v==0:print(" 0");return "0"
    n=ceil(log(v*2)/log(5))
    print(f"v={v} n={n}: ",end='')
    r=0
    l=[]
    for i in range(n-1,-1,-1):
        t=pow(5,i)
        d=v-r
        q=0
        if d>1*t+floor(t/2):
            q=2
        elif d>floor(t/2):
            q=1
        elif d==0:
            q=0
        elif d<0:
            if d<-1*t-floor(t/2):
                q=-2
            elif d<-floor(t/2):
                q=-1
            else:
                q=0
        r+=q*t
        l+=[q]
        #print(f" sup i={i} t={t} d={d} q={q} r={r} l={l}")
    di={2:'2',1:'1',0:'0',-1:'-',-2:'='}
    s=""
    for e in l:
        s+=di[e]
    print(f" s: {s}")
    return s
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(976,dec("2=-01"))
        self.assertEqual(314159265,dec("1121-1110-1=0"))
        #self.assertEqual("2=-1=0",enc(4890))
    def test_010(self):
        ls=load("input0")
        r=0
        for l in ls.splitlines():
            r+=dec(l)
        self.assertEqual(res00, r)
    def test_110(self):
        ls=load("input1")
        r=0
        for l in ls.splitlines():
            r+=dec(l)
        self.assertEqual(res1, enc(r))
#@unittest.skip
class T001(unittest.TestCase):
    def test__0(self):
        self.assertEqual("0",enc(0))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__2(self):
        self.assertEqual("2",enc(2))
    def test__3(self):
        self.assertEqual("1=",enc(3))
    def test__4(self):
        self.assertEqual("1-",enc(4))
    def test__5(self):
        self.assertEqual("10",enc(5))
    def test__6(self):
        self.assertEqual("11",enc(6))
@unittest.skip
class T002(unittest.TestCase):
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
    def test__1(self):
        self.assertEqual("1",enc(1))
#@unittest.skip
class T003(unittest.TestCase):
    def test__1747(self):
        self.assertEqual("1=-0-2",enc(1747))
    def test__906(self):
        self.assertEqual("12111",enc(906))
    def test__198(self):
        self.assertEqual("2=0=",enc(198))
    def test__11(self):
        self.assertEqual("21",enc(11))
    def test__201(self):
        self.assertEqual("2=01",enc(201))
    def test__31(self):
        self.assertEqual("111",enc(31))
    def test__1257(self):
        self.assertEqual("20012",enc(1257))
    def test__32(self):
        self.assertEqual("112",enc(32))
    def test__353(self):
        self.assertEqual("1=-1=",enc(353))
    def test__107(self):
        self.assertEqual("1-12",enc(107))
    def test__7(self):
        self.assertEqual("12",enc(7))
    def test__3(self):
        self.assertEqual("1=",enc(3))
    def test__37(self):
        self.assertEqual("122",enc(37))
