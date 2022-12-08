def parse(inp:str)->dict:
    m=[]
    for l in inp.splitlines():
        t=[]
        for c in l:
            t+=[c]
        m+=[t]
    return m

def calc(m:list)->int:
    if len(m) < 3 or len(m[0]) < 3:
        return -1
    n=0
    rows=len(m)
    cols=len(m[0])
    for j in range(rows-2):
        j+=1
        for i in range(cols-2):
            i+=1
            e=m[j][i]
            visible=True
            for y in range(rows):
                if y==j:
                    if visible:
                        break
                    else:
                        visible=True
                        continue
                if not visible:
                    continue
                if m[y][i] >= e:
                    visible=False
                    continue
                else:
                    pass
            if visible:
                n+=1
                continue
            visible=True
            for x in range(cols):
                if x==i:
                    if visible:
                        break
                    else:
                        visible = True
                        continue
                if not visible:
                    continue
                if m[j][x] >= e:
                    visible=False
                    continue
                else:
                    pass
            if visible:
                n+=1
                continue
    return n+rows*2+(cols-2)*2

def vert_vis(m:list, i:int, e:int, rng:range)->int:
    visible=True
    vis=0
    for y in rng:
        if not visible:
            break
        vis+=1
        if m[y][i] >= e:
            visible=False
            break
    return vis

def hori_vis(m:list, j:int, e:int, rng:range)->int:
    visible=True
    vis=0
    for x in rng:
        if not visible:
            break
        vis+=1
        if m[j][x] >= e:
            visible=False
            break
    return vis

def calc2_(m:list,j,i)->int:
    if len(m) < 3 or len(m[0]) < 3:
        return -1
    n=1
    rows=len(m)
    cols=len(m[0])
    e=m[j][i]
    n*=vert_vis(m, i, e, range(j-1,-1,-1))
    n*=vert_vis(m, i, e, range(j+1,rows))
    n*=hori_vis(m, j, e, range(i-1,-1,-1))
    n*=hori_vis(m, j, e, range(i+1,cols))
    return n

def calc2(m:list)->int:
    if len(m) < 3 or len(m[0]) < 3:
        return -1
    n=0
    rows=len(m)
    cols=len(m[0])
    max=0
    for j in range(rows-2):
        j+=1
        for i in range(cols-2):
            i+=1
            n=calc2_(m,j,i)
            if n > max:
                max = n
    return max

def run1(inp:str)->int:
    p=parse(inp)
    c=calc(p)
    return c

def run2(inp:str)->int:
    p=parse(inp)
    c=calc2(p)
    return c

import unittest
def load(name):return open(name,"rt").read()
res0 = 21
res1 = 1672
res0_2 = 8
res1_2 = 327180
class T1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(-1, calc([]))
    def test_2(self):
        self.assertEqual(-1, calc([[1]]))
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inpReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
class T2(unittest.TestCase):
    def test_020(self):
        inp0=load("input0")
        self.assertEqual(4, calc2_(parse(inp0),1,2))
    def test_021(self):
        inp0=load("input0")
        self.assertEqual(8, calc2_(parse(inp0),3,2))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
