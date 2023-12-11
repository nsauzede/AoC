import unittest
INP01="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
INP01_=[['.','.','.','#','.','.','.','.','.','.',],
['.','.','.','.','.','.','.','#','.','.',],
['#','.','.','.','.','.','.','.','.','.',],
['.','.','.','.','.','.','.','.','.','.',],
['.','.','.','.','.','.','#','.','.','.',],
['.','#','.','.','.','.','.','.','.','.',],
['.','.','.','.','.','.','.','.','.','#',],
['.','.','.','.','.','.','.','.','.','.',],
['.','.','.','.','.','.','.','#','.','.',],
['#','.','.','.','#','.','.','.','.','.',]]
RES01=374
RES1=10077850
RES11=1030
RES12=8410
RES2=504715068438
def disp(inp,text="inp"):
    print(f"{text}:")
    for r in inp:
        print(" ".join(r))
def expand1(inp:list,mult=2)->list:
    disp(inp, "INITIAL")
    erows=emptyrows(inp)
    print(f"erows={erows}")
    ecols=emptycols(inp)
    print(f"ecols={ecols}")
    gal=[]
    y=0
    for j,r in enumerate(inp):
        r0=[]
        if j in erows:
            y+=mult-1
        x=0
        for i,c in enumerate(r):
            if i in ecols:
                x+=mult-1
            if c=='#':
                gal+=[(y,x)]
            x+=1
        y+=1
    inp2=[]
    print(f"y={y} x={x}")
    disp(inp2,"FINAL")
    print(f"gal={gal}")
    return gal
def expand(inp:list)->list:
    disp(inp, "INITIAL")
    inp0=inp.copy()
    erows=emptyrows(inp)
    print(f"erows={erows}")
    ecols=emptycols(inp)
    lc=len(ecols)
    l=len(inp[0])
    erow=['.']*(l+lc)
    print(f"ecols={ecols}")
    inp=[]
    n=1
    gal=[]
    y=0
    for j,r in enumerate(inp0):
        if j in erows:
            y+=1
            inp+=[erow.copy()]
        x=0
        e=[]
        for i,c in enumerate(r):
            if i in ecols:
                e+=['.']
                x+=1
            if c=='#':
                c=f"{n}"
                n+=1
                gal+=[(y,x)]
            e+=[c]
            x+=1
        inp+=[e]
        y+=1
    disp(inp,"FINAL")
    print(f"gal={gal}")
    return gal
def manh(a,b):
    n=0
    if a!=b:
        #delta=b-a
        #step=delta//abs(delta)
        #for i in range(a,b,step):n+=1
        n+=abs(b-a)
    return n
# returns manhattan distance between coords
def manhattan(coord1:tuple, coord2=(0,0))->int:
    return manh(coord1[1],coord2[1])+manh(coord1[0],coord2[0])
def compute(inp:list,part=0,mult=2)->int:
    if part==1:
        gal=expand1(inp,mult)
    else:
        gal=expand(inp)
    res = 0
    for i,g1 in enumerate(gal):
        for g2 in gal[i+1:]:
            if g1==g2:continue
            l=manhattan(g1,g2)
            print(f"g1={g1} g2={g2} l={l}")
            res+=l
    return res
def emptyrows(inp)->list:
    res=[]
    for i,r in enumerate(inp):
        if all(e=='.' for e in r):
            res+=[i]
    return res
def emptycols(inp)->list:
    res=[]
    for i in range(len(inp)):
        if all(r[i]=='.' for r in inp):
            res+=[i]
    return res
def parse(inp):
    res=[]
    ll=inp.splitlines()
    for l in ll:
        l0=[]
        for c in(l):
            l0+=[c]
        res+=[l0]
    return res
class T000(unittest.TestCase):
    def test_01_0(self):
        self.assertEqual(RES01+0,compute(INP01_))
    def test_1100_(self):
        self.assertEqual(RES01+0,compute(INP01_, 1))
    def test_1100(self):
        self.assertEqual(RES11+0,compute(INP01_, 1, 10))
    def test_1200(self):
        self.assertEqual(RES12+0,compute(INP01_, 1, 100))
    def test_2000(self):
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read()), 1, 1000000))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES020+0,compute(parse(INP020),1))
    def Ztest_2000(self):
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read()),1))
