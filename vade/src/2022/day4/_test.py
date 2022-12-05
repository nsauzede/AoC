def torange(inp:str)->list:
    l,r=[int(e) for e in inp.split("-")]
    return [l,r]

def topair(inp:str)->str:
    l,r=inp.split(",")
    return (torange(l),torange(r))

def overlap(inp:str, strict=True)->int:
    l,r=topair(inp)
    n=0
    if l[0] <= r[0]:
        if not strict and r[0] <= l[1]:
            n+=1
        elif r[1] <= l[1]:
                n+=1
        elif l[0] == r[0]:
            if l[1] <= r[1]:
                n+=1
    elif r[0] <= l[0]:
        if not strict and l[0] <= r[1]:
            n+=1
        elif l[1] <= r[1]:
            n+=1
    return n

def run1(inp:str, strict=True)->int:
    s=0
    for l in inp.splitlines():
        s+=overlap(l,strict)
    return s

import unittest
def load(name):return open(name,"rt").read()
res0 = 2
res1 = 547
res0_2 = 4
res1_2 = 843
class T0(unittest.TestCase):
    def test_torange1(self):
        self.assertEqual([2,4], torange('2-4'))
    def test_torange2(self):
        self.assertEqual([6,8], torange('6-8'))
    def test_topair(self):
        self.assertEqual(([2,4],[6,8]), topair('2-4,6-8'))
    def test_overlap1(self):
        self.assertEqual(0, overlap('2-4,6-8'))
        self.assertEqual(0, overlap('2-3,4-5'))
        self.assertEqual(0, overlap('5-7,7-9'))
        self.assertEqual(0, overlap('2-6,4-8'))
    def test_overlap2(self):
        self.assertEqual(1, overlap('2-8,3-7'))
        self.assertEqual(1, overlap('6-6,4-6'))

res02_2 = 8
class T(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inp1ReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run1(inp0,False))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run1(inp1,False))
