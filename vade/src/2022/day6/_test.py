def dupes(a:list)->list:
    seen = set()
    return [x for x in a if x in seen or seen.add(x)]
def run1(inp:str, n=4)->int:
    l=[]
    i=0
    for c in inp:
        i+=1
        l.insert(0,c)
        if len(l) == n:
            if len(dupes(l))==0:
                break
            l.pop()
    return i

import unittest
def load(name):return open(name,"rt").read()
res0 = 7
res1 = 1802
res0_2 = 19
res1_2 = 3551
class T(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inp0ReturnsRes01(self):
        self.assertEqual(5, run1("bvwbjplbgvbhsrlpgdmjqwftvncz"))
    def test_inpReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run1(inp0, 14))
    def test_inp0ReturnsRes01_2(self):
        self.assertEqual(23, run1("bvwbjplbgvbhsrlpgdmjqwftvncz", 14))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run1(inp1, 14))
