res0 = -3
res1 = 280
res0_2 = 0
res1_2 = 1797
def cnt2(s):
    floor=0
    first=0
    for i,c in enumerate(s):
        floor+=1 if c=='(' else -1
        if first==0 and floor==-1:first=i+1
    return floor,first
def cnt(s):return cnt2(s)[0]
def load(name):return open(name,"rt").read()
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res0,cnt(")())())"))
    def test_001(self):
        self.assertEqual(res0,cnt(load("input0")))
    def test_110(self):
        self.assertEqual(res1,cnt(load("input1")))
    def test_210(self):
        self.assertEqual(res1_2,cnt2(load("input1"))[1])
