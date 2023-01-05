res0 = 33583
res1 = 3256599
res0_2 = 966
res1_2 = 4882038
def load(name):return open(name,"rt").read()
def compute(s):
    n=0
    lines=s.splitlines()
    for l in lines:
        #print(int(l))
        x=int(l)//3-2
        n+=x
    return n
def fuel(x0:int):
    x=x0//3-2
    #print(f"x={x}")
    return x+fuel(x) if x>0 else 0
def compute2(s):
    n=0
    lines=s.splitlines()
    for l in lines:
        #print(int(l))
        n+=fuel(int(l))
    return n
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res0,compute("100756\n"))
    def test_001(self):
        self.assertEqual(2,compute("12\n"))
    def test_002(self):
        self.assertEqual(2,compute("14\n"))
    def test_003(self):
        self.assertEqual(654,compute("1969\n"))
    def test_004(self):
        self.assertEqual(res0,compute(load("input0")))
    def test_100(self):
        self.assertEqual(res1,compute(load("input1")))
    def test_200(self):
        self.assertEqual(res0_2,compute2("1969\n"))
    def test_201(self):
        self.assertEqual(50346,compute2("100756\n"))
    def test_202(self):
        self.assertEqual(50346+966,compute2("1969\n100756\n"))
    def test_210(self):
        self.assertEqual(res1_2,compute2(load("input1")))
