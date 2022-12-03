def run(inp:str, top=1)->int:
    count=0
    totals=[]
    for l in inp.splitlines():
        #print(f"l={l}")
        if l == "":
            totals+=[count]
            count = 0
            continue
        count+=int(l)
    totals+=[count]
    max=sum(sorted(totals,reverse=True)[0:top])
    #print(f"max={max}")
    return max

import unittest

def load(name)->str:
    f=open(name,"rt")
    return f.read()
res0 = 24000
res1 = 67016
res0_2 = 45000
res1_2 = 200116
class TestDay1(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run(inp0))
    def test_inp1ReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run(inp1))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run(inp0, top=3))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run(inp1, top=3))
