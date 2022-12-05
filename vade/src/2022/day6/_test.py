def run1(inp:str)->str:
    return "TODO"

import unittest
def load(name):return open(name,"rt").read()
res0 = ""
res1 = ""
res0_2 = ""
res1_2 = ""
class T(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def Ztest_inpReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def Ztest_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run1(inp0, True))
    def Ztest_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run1(inp1, True))
