def parse(inp:str)->(list,list):
    stacks=[]
    for l in inp.splitlines():
        if l.startswith(" 1"):
            st=l.split()
            for j in range(len(st)):
                stacks+=[[]]
            break
    moves=[]
    for l in inp.splitlines():
        if "[" in l:
            st=l.split()
            p=-1
            for e in st:
                p=l.find(e, p+1)
                pos=p//4
                c=e[1]
                stacks[pos].insert(0,c)
        elif l.startswith("move"):
            st=l.split()
            moves+=[(int(st[1]),int(st[3]),int(st[5]))]
    return stacks,moves

def move(stacks:list, moves:list, preserve=False)->list:
    for m in moves:
        n,f,t=m
        st=[]
        for i in range(n):
            e=stacks[f-1].pop()
            if preserve:
                st+=e
            else:
                stacks[t-1].append(e)
        if preserve:
            for i in range(n):
                stacks[t-1].append(st.pop())
    return stacks

def gettop(stacks:list)->str:
    ret=""
    for st in stacks:
        if len(st)>0:
            ret+=st[-1]
    return ret

def run1(inp:str, preserve=False)->int:
    stacks,moves=parse(inp)
    stacks=move(stacks, moves, preserve)
    return gettop(stacks)

import unittest
def load(name)->str:
    f=open(name,"rt")
    return f.read()
res0 = "CMZ"
res1 = "ZRLJGSCTR"
res0_2 = "MCD"
res1_2 = "PRTTGRFPB"
class T0(unittest.TestCase):
    def test_ld0(self):
        inp0=load("input0")
        stacks,moves=parse(inp0)
        stacks=move(stacks, moves)
        self.assertEqual(res0, gettop(stacks))
class T(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run1(inp0, True))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run1(inp1, True))
