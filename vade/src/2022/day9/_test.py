def apply_(k:list, i=1):
    if i>=len(k):return
    if k[i-1][0]>k[i][0]+1:# T->H RIGHT
        k[i][0]+=1
        if k[i-1][1]<k[i][1]:# UP
            k[i][1]-=1
        elif k[i-1][1]>k[i][1]:# DOWN
            k[i][1]+=1
    elif k[i-1][0]<k[i][0]-1:# H<-T LEFT
        k[i][0]-=1
        if k[i-1][1]<k[i][1]:# UP
            k[i][1]-=1
        elif k[i-1][1]>k[i][1]:# DOWN
            k[i][1]+=1
    elif k[i-1][1]<k[i][1]-1:# H^-T UP
        k[i][1]-=1
        if k[i-1][0]>k[i][0]:# RIGHT
            k[i][0]+=1
        elif k[i-1][0]<k[i][0]:# LEFT
            k[i][0]-=1
    elif k[i-1][1]>k[i][1]+1:# Hv-T DOWN
        k[i][1]+=1
        if k[i-1][0]<k[i][0]:# LEFT
            k[i][0]-=1
        elif k[i-1][0]>k[i][0]:# RIGHT
            k[i][0]+=1
    apply_(k,i+1)

def move_(p:dict,k:list,c:int,d:list):
    for i in range(c):
        k[0]=[sum(x) for x in zip(k[0], d)]
        apply_(k)
        p[tuple(k[-1])]=1

def moveright(p:dict,k:list,c:int): move_(p, k, c, [1,0])
def moveup(p:dict,k:list,c:int): move_(p, k, c, [0,-1])
def moveleft(p:dict,k:list,c:int): move_(p, k, c, [-1,0])
def movedown(p:dict,k:list,c:int): move_(p, k, c, [0,1])

def parse(inp:str)->dict:
    m=[]
    for l in inp.splitlines():
        n,v=l.split(" ")
        m+=[[n,int(v)]]
    return m

def draw(knots,dims):
    w,h=dims
    for r in range(h):
        for c in range(w):
            if knots[0]==[c,r]:print('H',end='');continue
            if len(knots)==2 and knots[1]==[c,r]:print('T',end='');continue
            cont=False
            for i in range(1,len(knots)):
                if knots[i]==[c,r]:print(f"{i}",end='');cont=True;break
            if cont:continue
            if (0,4)==(c,r):print('s',end='');continue
            print('.',end='')
        print('')
    print('')

def drawtail(p:list,dims:list):
    w,h=dims
    for r in range(h):
        for c in range(w):
            if (c,r) in p:
                print('#',end='')
            else:
                print('.',end='')
        print('')
    print('')

def calc(m:list,n=2,dims=[6,5],start=[0,4])->int:
    p={}
    k=mkmat(start,n)
    print(f"== Initial State ==")
    print()
    draw(k, dims)
    for t,c in m:
        print(f"== {t} {c} == len(p)={len(p)}")
        if t=='R':moveright(p,k,c)
        if t=='U':moveup(p,k,c)
        if t=='L':moveleft(p,k,c)
        if t=='D':movedown(p,k,c)
        #draw(k, dims)
    drawtail(p,dims)
    return len(p)

def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):
        mat+=[row.copy()]
    return mat
def load(name):return open(name,"rt").read()
import unittest
res0=13
res1=5735
res0_2=1
res2=2478
class TestPart2(unittest.TestCase):
    def test_part2_input0(self):
        inp=load("input0")
        m=parse(inp)
        res=calc(m,n=10)
        self.assertEqual(res0_2+1000*0, res)
    def test_part2_input1(self):
        inp=load("input1")
        m=parse(inp)
        res=calc(m,n=10)
        self.assertEqual(res2+1000*0, res)

class TestPart1(unittest.TestCase):
    def test_part1_input0(self):
        inp=load("input0")
        m=parse(inp)
        res=calc(m)
        self.assertEqual(res0+1000*0, res)
    def test_part1_input1(self):
        inp=load("input1")
        m=parse(inp)
        res=calc(m)
        self.assertEqual(res1, res)

class TestExample0Manually(unittest.TestCase):
    def test_MoveRightFour(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        self.assertEqual([[4,4],[3,4]],k)
    def test_MoveRight4Up4(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        moveup({},k,4)
        self.assertEqual([[4,0],[4,1]],k)
    def test_MoveR4U4L3(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        moveup({},k,4)
        moveleft({},k,3)
        self.assertEqual([[1,0],[2,0]],k)
    def test_MoveR4U4L3D1(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        moveup({},k,4)
        moveleft({},k,3)
        movedown({},k,1)
        self.assertEqual([[1,1],[2,0]],k)
    def test_MoveR4U4L3R4(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        moveup({},k,4)
        moveleft({},k,3)
        movedown({},k,1)
        moveright({},k,4)
        self.assertEqual([[5,1],[4,1]],k)
    def test_MoveR4U4L3R4D1(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        moveup({},k,4)
        moveleft({},k,3)
        movedown({},k,1)
        moveright({},k,4)
        movedown({},k,1)
        moveleft({},k,5)
        self.assertEqual([[0,2],[1,2]],k)
    def test_MoveR4U4L3R4D1R2(self):
        k=mkmat([0,4],2)
        dims=[6,5]
        moveright({},k,4)
        moveup({},k,4)
        moveleft({},k,3)
        movedown({},k,1)
        moveright({},k,4)
        movedown({},k,1)
        moveleft({},k,5)
        moveright({},k,2)
        self.assertEqual([[2,2],[1,2]],k)

class TestTouchingDoesntMove(unittest.TestCase):
    def test_leftTouchDoesntMove(self):
        k=[[1,1],[0,1]]
        dims=[3,3]
        apply_(k)
        self.assertEqual([[1,1],[0,1]],k)
    def test_rightTouchDoesntMove(self):
        k=[[1,1],[2,1]]
        dims=[3,3]
        apply_(k)
        self.assertEqual([[1,1],[2,1]],k)
    def test_upTouchDoesntMove(self):
        k=[[1,1],[1,0]]
        dims=[3,3]
        apply_(k)
        self.assertEqual([[1,1],[1,0]],k)
    def test_downTouchDoesntMove(self):
        k=[[1,1],[1,2]]
        dims=[3,3]
        apply_(k)
        self.assertEqual([[1,1],[1,2]],k)

class TestGapPullsTailOne(unittest.TestCase):
    def test_rightGapTwoPullsTailOne(self):
        k=[[3,1],[1,1]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[3,1],[2,1]],k)
    def test_leftGapTwoPullsTailOne(self):
        k=[[1,1],[3,1]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[1,1],[2,1]],k)
    def test_upGapTwoPullsTailOne(self):
        k=[[2,0],[2,2]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[2,0],[2,1]],k)
    def test_downGapTwoPullsTailOne(self):
        k=[[2,2],[2,0]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[2,2],[2,1]],k)

class TestDiagPullsDiag(unittest.TestCase):
    def test_diagUpRightPullsDiag(self):
        k=[[2,1],[1,3]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[2,1],[2,2]],k)
    def test_diagRightUpPullsDiag(self):
        k=[[3,2],[1,3]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[3,2],[2,2]],k)
    def test_diagUpLeftPullsDiag(self):
        k=[[1,1],[2,3]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[1,1],[1,2]],k)
    def test_diagLeftUpPullsDiag(self):
        k=[[1,2],[3,3]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[1,2],[2,2]],k)
    def test_diagLeftDownPullsDiag(self):
        k=[[1,3],[3,2]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[1,3],[2,3]],k)
    def test_diagDownLeftPullsDiag(self):
        k=[[1,3],[2,1]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[1,3],[1,2]],k)
    def test_diagDownRightPullsDiag(self):
        k=[[2,3],[1,1]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[2,3],[2,2]],k)
    def test_diagRightDownPullsDiag(self):
        k=[[3,3],[1,2]]
        dims=[5,3]
        apply_(k)
        self.assertEqual([[3,3],[2,3]],k)
