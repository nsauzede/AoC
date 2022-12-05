def prio(c:str)->int:
    n=0
    if c>='a' and c<='z':
        n+=ord(c)-ord('a')+1
    elif c>='A' and c<='Z':
        n+=ord(c)-ord('A')+1+26
    return n

def commons(l:str,r:str)->list:
    return list(set(l).intersection(r))
def common(l:str,r:str)->int:
    return commons(l,r)[0]

def spl(s:str)->int:
    half=len(s)//2
    l,r=s[:half],s[half:]
    return l,r

def run1(inp:str)->int:
    s=0
    for l in inp.splitlines():
        l,r=spl(l)
        s+=prio(common(l,r))
    return s

def run2(inp:str)->int:
    s=0
    n=0
    lines=[]
    for l in inp.splitlines():
        lines+=[l]
        n+=1
        if n<3:continue
        c1="".join(commons(lines[0],lines[1]))
        c2="".join(commons(lines[1],lines[2]))
        s+=prio(common(c1,c2))
        lines=[]
        n=0
    return s

import unittest
def load(name)->str:
    f=open(name,"rt")
    return f.read()
res0 = 157
res1 = 8515
res0_2 = 70
res1_2 = 2434
class T0(unittest.TestCase):
    def test_conv_a(self):
        self.assertEqual(1, prio('a'))
    def test_conv_z(self):
        self.assertEqual(26, prio('z'))
    def test_conv_A(self):
        self.assertEqual(27, prio('A'))
    def test_conv_Z(self):
        self.assertEqual(52, prio('Z'))

    def test_common_a_a(self):
        self.assertEqual('a', common('a', 'a'))
    def test_common_inp0_1(self):
        s="vJrwpWtwJgWrhcsFMMfFFhFp"
        l,r=spl(s)
        self.assertEqual('p', common(l,r))
    def test_common_inp0_2(self):
        self.assertEqual('L', common("jqHRNqRjqzjGDLGL","rsFMfFZSrLrFZsSL"))

    def test_common_multi1(self):
        c1="".join(commons("vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"))
        c2="".join(commons("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"))
        self.assertEqual('r', common(c1,c2))
    def test_common_multi2(self):
        c1="".join(commons("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT"))
        c2="".join(commons("ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"))
        self.assertEqual('Z', common(c1,c2))

class T(unittest.TestCase):
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inp1ReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
