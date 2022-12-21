def mapstr(m:list)->str:return "\n".join(["".join(str(i) for i in sublist) for sublist in m])+"\n"
def strmap(inp:str)->list:
    #l=[s for s in inp.split("\n")]
    #return [[c] for c in l]
    #return [[] for s in ]
    return [[c for c in s] for s in inp.split("\n")][:-1]
def draw(m:list):print(mapstr(m))
# calculate flow of sand unit from input p into output
# if output=input => rest
# if output=y+1 => straight flow
# if output=x-1,y+1 => diag left flow
# if output=x+1,y+1 => diag right flow
# if output is either x<0 or x>=w or y>=h => free fall
def flow(m:list,p:list)->list:
    x,y=p
    w,h=len(m[0]),len(m)
    if y<0 or y>=h:raise Exception(f"Kaboom y={y}")
    if x<0 or x>=w:raise Exception(f"Kaboom x={x}")
    if y+1 >= h:return [x,y+1]
    c=m[y+1][x]
    if c=='.':                          # flow straight
        return [x,y+1]
    if c=='#' or c=='o':
        if x==0:                        # free fall left
            return [x-1,y+1]
        c=m[y+1][x-1]
        if c=='.':                      # diag left
            return [x-1,y+1]
        if c=='#' or c=='o':
            if x+1 == w:                # free fall right
                return [x+1,y+1]
            c=m[y+1][x+1]
            if c=='.':                  # diag right
                return [x+1,y+1]
            if c=='#' or c=='o':        # rest
                return [x,y]
            raise Exception(f"Kaboom x+1,y+1 c={c}")
    raise Exception(f"Kaboom x,y+1 c={c}")
def source(m:list,src='+')->list:
    return [[l.index(src),i] for i,l in enumerate(m) if src in l][0]
# compute drop of sand unit until it rests, or free fall
# if p input not provided (or None) then search for '+' in m
# if output is either x<0 or x>=w or y>=h => free fall
# if rest => update m at output p to be 'o'
def drop(m:list,p=None)->list:
    w,h=len(m[0]),len(m)
    try:
        if p==None:p=source(m)
    except:
        return [-1,0]
    while True:
        p0=p
        p=flow(m,p)
        x,y=p
        if p==p0:                       # rest
            m[y][x]='o'
            if y==0:
                print(f"WE REACHED Y==0!!! X={x}")
            return p
        if y>=h or x<0 or x>=w:         # free fall
            return p
def pour(m:list)->int:
    w,h=len(m[0]),len(m)
    n=0
    while True:
        p=drop(m)
        x,y=p
        if y>=h or x<0 or x>=w:
            break
        n+=1
    return n

def scan(m:list, s:str, bedrock=False)->int:
    for l in s.splitlines():
        path = [eval(x) for x in l.split(" -> ")]
        p0 = path[0]
        mx=0
        my=0
        for p in path[1:]:
            if p0[0]==p[0]:#vertical line
                x=p0[0]
                y1,y2=p0[1],p[1]
                delta=y2-y1
                step=delta//abs(delta)
                for y in range(y1,y2+step,step):
                    #print(f"x={x} y={y}")
                    m[y][x]='#'
                if x>mx:mx=x
                if y>my:my=y
            elif p0[1]==p[1]:#horizontal line
                y=p0[1]
                x1,x2=p0[0],p[0]
                delta=x2-x1
                step=delta//abs(delta)
                for x in range(x1,x2+step,step):
                    m[y][x]='#'
                if x>mx:mx=x
                if y>my:my=y
            p0 = p
    br=my+2
    print(f"mx={mx} my={my} br={br}")
    if bedrock:
        for x in range(len(m[0])):
            m[br][x]='#'
    return br

def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):mat+=[row.copy()]
    return mat
def load(name):return open(name,"rt").read()
def attrs(c:object,names:list)->dict:return dict({k: v for k, v in vars(c).items() if k in names})

import unittest
res0 = 24
res1 = 1068
res0_2 = 93
res1_2 = 0

#@unittest.skip
class TestPourWithInput1InPart2(unittest.TestCase):
# W=600 => 1470 too low
# W=800 => 23773 too low
    def test_pour(self):
        m=mkmat(['.']*900,200)
        m[0][500]='+'
        inp=load('input1')
        scan(m,inp, bedrock=True)
        n=pour(m)
        self.assertEqual(res0_2+10000*0,n)

class TestPourWithInput0InPart2(unittest.TestCase):
    def test_pour(self):
        m=mkmat(['.']*600,200)
        m[0][500]='+'
        inp=load('input0')
        scan(m,inp, bedrock=True)
        n=pour(m)
        self.assertEqual(res0_2+10000*0,n)

class TestBedrock(unittest.TestCase):
    def test_bedrock(self):
        m=mkmat(['.']*600,200)
        m[0][500]='+'
        inp=load('input0')
        br=scan(m,inp, bedrock=True)
        self.assertEqual('#', m[br][0])
        self.assertEqual('#', m[br][len(m[0])-1])

class TestOverflowSource(unittest.TestCase):
    def test_overflowSource(self):
        m=[['.','.','+','.','.'],['.','.','.','.','.'],['#','#','#','#','#']]
        p=drop(m)
        draw(m)
        p=drop(m)
        draw(m)
        p=drop(m)
        draw(m)
        p=drop(m)
        draw(m)
        self.assertEqual([2,0],p)

class TestPourWithInput1InPart1(unittest.TestCase):
    def test_pour(self):
        m=mkmat(['.']*600,200)
        m[0][500]='+'
        inp=load('input1')
        scan(m,inp)
        n=pour(m)
        self.assertEqual(res1+10000*0,n)

class TestPourWithInput0InPart1(unittest.TestCase):
    def test_pour(self):
        m=mkmat(['.']*600,200)
        m[0][500]='+'
        #draw(m)
        inp=load('input0')
        scan(m,inp)
        #draw(m)
        n=pour(m)
        self.assertEqual(res0+10000*0,n)

class TestDropAndPourInExample00(unittest.TestCase):
    def test_dropFirstSandUnitInExample00(self):
        m=strmap(m00)
        p=drop(m)
        self.assertEqual([6,8],p)
        self.assertEqual('o',m[8][6])
    def test_pour(self):
        m=strmap(m00)
        n=pour(m)
        self.assertEqual(res0,n)

class TestStringMapConv(unittest.TestCase):
    def test_mapstr(self):
        self.assertEqual("12\n34\n",mapstr([[1,2],[3,4]]))
        self.assertEqual("+.\n#o\n",mapstr([['+','.'],['#','o']]))
    def test_strmap(self):
        self.assertEqual([['+','.'],['#','o']],strmap("+.\n#o\n"))

class TestDropRestingUnits(unittest.TestCase):
    def test_dropStraightLeavesRestingUnit(self):
        m=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['#','#','#','#']]
        drop(m,[2,0])
        self.assertEqual('o',m[2][2])
    def test_twoIdenticalDropsAddsDiagLeftUnit(self):
        m=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['#','#','#','#']]
        drop(m,[2,0])
        self.assertEqual('o',m[2][2])
        drop(m,[2,0])
        self.assertEqual('o',m[2][1])
    def test_FourIdenticalDropsMakeAPyramid(self):
        m=[['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['#','#','#','#','#']]
        drop(m,[2,0])
        drop(m,[2,0])
        drop(m,[2,0])
        drop(m,[2,0])
        self.assertEqual('o',m[1][2])

class TestDropFinalPos(unittest.TestCase):
    def test_dropStraightThenRest(self):
        m=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['#','#','#','#']]
        self.assertEqual([2,2],drop(m,[2,0]))
    def test_dropDiagLeftThenRest(self):
        m=[['.','.','.','.'],['.','.','.','.'],['.','.','#','.'],['#','#','#','#']]
        self.assertEqual([1,2],drop(m,[2,0]))
    def test_dropDiagRightThenRest(self):
        m=[['.','.','.','.'],['.','.','.','.'],['#','#','.','.'],['#','#','#','#']]
        self.assertEqual([2,2],drop(m,[1,0]))
    def test_dropStraightFall(self):
        m=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
        self.assertEqual([1,3],drop(m,[1,0]))
    def test_dropDiagLeftFall(self):
        m=[['.','.','.','.'],['.','.','.','.'],['#','.','.','.']]
        self.assertEqual([-1,2],drop(m,[0,0]))
    def test_dropDiagRightFall(self):
        m=[['.','.','.','.'],['.','.','.','.'],['.','.','#','#']]
        self.assertEqual([4,2],drop(m,[3,0]))

class TestFlow(unittest.TestCase):
    def test_canFlowStraightOne(self):
        m=mkmat(['.','.'],2)
        self.assertEqual([0,1],flow(m,[0,0]))
        self.assertEqual([1,1],flow(m,[1,0]))
    def test_canFallStraightOne(self):
        m=mkmat(['.','.'],2)
        self.assertEqual([0,2],flow(m,[0,1]))
        self.assertEqual([1,2],flow(m,[1,1]))
    def test_canRestOne(self):
        m=[['.','.','.'],['#','#','#'],]
        self.assertEqual([1,0],flow(m,[1,0]))
    def test_canFlowDiagLeftOne(self):
        m=[['.','.'],['.','#'],]
        self.assertEqual([0,1],flow(m,[1,0]))
    def test_canFallDiagLeftOne(self):
        m=[['.'],['#'],]
        self.assertEqual([-1,1],flow(m,[0,0]))
    def test_canRestDiagLeft(self):
        m=[['.','.','.'],['.','.','#'],['#','#','#']]
        self.assertEqual([1,1],flow(m,[2,0]))
        self.assertEqual([1,1],flow(m,[1,1]))
    def test_canFlowDiagRighttOne(self):
        m=[['.','.','.'],['#','#','.'],]
        self.assertEqual([2,1],flow(m,[1,0]))
    def test_canFallDiagRighttOne(self):
        m=[['.','.',],['#','#'],]
        self.assertEqual([2,1],flow(m,[1,0]))
    def test_canRestDiagRight(self):
        m=[['.','.','.','.'],['#','#','.','.'],['#','#','#','#']]
        self.assertEqual([2,1],flow(m,[1,0]))
        self.assertEqual([2,1],flow(m,[2,1]))

m00="""\
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
........#.
#########.
"""
