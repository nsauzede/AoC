import unittest
INP01=r"""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
OUT01={'m':[
['.','.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','#','#','#','.','#','.'],
['.','#','#','#','.','#','#','.','.','#','.'],
['.','.','#','.','#','.','.','.','#','.','.'],
['.','.','.','.','#','.','#','.','.','.','.'],
['.','#','#','.','.','.','#','#','#','#','.'],
['.','#','#','.','.','#','.','.','.','#','.'],
['.','.','.','.','.','.','.','#','#','.','.'],
['.','#','#','.','#','.','#','#','#','#','.'],
['.','#','#','.','.','#','#','.','#','#','.'],
['.','.','.','.','.','.','.','.','.','.','.'],
],
'start':(5,5),
}
RES01=16
#RES1=43        # not right
RES1=3689
RES02=0
RES2=0
def compute(d0:dict,n=6,part=0)->int:
    #print(f"d0={d0}")
    d=d0.copy()
    res=0
    m=d['m']
    h=len(m)
    w=len(m[0])
    res=0
    steps=[d['start']]
    for i in range(n):
        steps=compute0(m,w,h,steps,part)
        res=len(steps)
    return res
def compute0(m,w,h,steps,part=0)->list:
    res=[]
    for step in steps:
        x,y=step
        i=x
        j=y-1
        if j>=0 and (i,j) not in res:
            if m[j][i]=='.':
                res+=[(i,j)]
        j=y
        i=x-1
        if i>=0 and (i,j) not in res:
            if m[j][i]=='.':
                res+=[(i,j)]
        i=x+1
        if i<w and (i,j) not in res:
            if m[j][i]=='.':
                res+=[(i,j)]
        i=x
        j=y+1
        if j<h and (i,j) not in res:
            if m[j][i]=='.':
                res+=[(i,j)]
    return res
def calc(wfs:dict,x,m,a,s)->int:
    res = 0
    #print(f"x={x} m={m} a={a} s={s}")
    k='in'
    while True:
        break
    return res
def parse(inp:str,part=0)->dict:
    res={'m':[]}
    #print(f"inp={inp}")
    for j,s in enumerate(inp.splitlines()):
        l=list(s)
        if'S'in s:
            #print(f"s={s} l={l}")
            i=l.index('S')
            l[i]='.'
            res['start']=(i,j)
        res['m']+=[l]
    return res
def disp(d:dict,text="DISP"):
    print(f"\n{text} ==============")
    h=len(m)
    w=len(m[0])
    for j,r in enumerate(m):
        for i,c in enumerate(r):
            print(c,end='')
        print()
class T000(unittest.TestCase):
    def test_0110(self):
        res=parse(INP01)
        #print(f"\nres={res}")
        #print(f"OUT={OUT01}")
        self.assertEqual(OUT01,res)
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read()),n=64))
    def Ztest_2000(self):
        """
res=2772531 ons=0 offs=5 0.00028%
res=2772532 ons=0 offs=7 0.00028%
res=2772533 ons=0 offs=6 0.00028%
res=2772534 ons=0 offs=8 0.00028%
res=2772535 ons=0 offs=5 0.00028%
res=2772536 ons=0 offs=9 0.00028%
        """
        #start=0
        #n=1000000000000
        start=2772531
        n=4
        self.assertEqual(RES2+0*1000,compute2(parse(open("input1","rt").read()),start=start,n=n,part=1))
