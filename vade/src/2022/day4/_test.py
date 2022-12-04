def torange(inp:str)->list:
    l,r=[int(e) for e in inp.split("-")]
    return [l,r]

def topair(inp:str)->str:
    l,r=inp.split(",")
    return (torange(l),torange(r))

def overlap(inp:str)->int:
    l,r=topair(inp)
    n=0
    if l[0] <= r[0]:
        if r[1] <= l[1]:
                n+=1
        elif l[0] == r[0]:
            if l[1] <= r[1]:
                n+=1
    elif r[0] <= l[0]:
        if l[1] <= r[1]:
            n+=1
    #print(f"{l},{r} => {n}")
    return n
"""
123..
.234.

..345
.234.

...45
.234.
"""
def overlap2(inp:str)->int:
    l,r=topair(inp)
    n=0
    if l[0] <= r[0]:
        if r[0] <= l[1]:
            n+=1
        elif r[1] <= l[1]:
                n+=1
        elif l[0] == r[0]:
            if l[1] <= r[1]:
                n+=1
    elif r[0] <= l[0]:
        if l[0] <= r[1]:
            n+=1
        elif l[1] <= r[1]:
            n+=1
    #print(f"{l},{r} => {n}")
    return n

def overlap_alt(s):
    pairs = [list(map(int, d.split("-"))) for d in s.split(",")]
    x1, x2, y1, y2 = pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1]
    return (x1 <= x2 and y1 >= y2) or (x1 >= x2 and y1 <= y2)

def run1(inp:str)->int:
    s=0
    for l in inp.splitlines():
        #print(f"l={l}")
        s+=overlap(l)
    return s

def run2(inp:str)->int:
    s=0
    for l in inp.splitlines():
        #print(f"l={l}")
        s+=overlap2(l)
    return s

import unittest
def load(name)->str:
    f=open(name,"rt")
    return f.read()
res0 = 2
res1 = 547
res0_2 = 4
res1_2 = 0
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

"""
123..
.234.

123..
1234.

1....
1234.

.2...
1234.

...4.
1234.

"""
inp00="""1-1,1-4
2-2,1-4
3-3,1-4
4-4,1-4
1-4,1-1
1-4,2-2
1-4,3-3
1-4,4-4
"""
inp02="""1-1,1-4
2-2,1-4
3-3,1-4
4-4,1-4
1-4,1-1
1-4,2-2
1-4,3-3
1-4,4-4
"""
res02_2 = 8
#class T(object):
class T(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inp00ReturnsRes00(self):
        self.assertEqual(8, run1(inp00))
    def test_inp1ReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_inp02ReturnsRes02_2(self):
        self.assertEqual(res02_2, run2(inp02))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
