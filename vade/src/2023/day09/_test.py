import unittest
INP01="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
RES01=114
INP01_=[[0, 3, 6, 9, 12, 15],[1, 3, 6, 10, 15, 21],[10, 13, 16, 21, 30, 45],]
RES1=2005352194
RES02=2
RES2=1077
def compute(inp:list,part=0)->int:
    res = 0
    for l in inp:
        l0=l.copy();res0=0;s=1
        while not all(e==0 for e in l0):
            last=l0[0]
            first=last
            l1=[]
            for e in l0[1:]:
                l1+=[e-last]
                last=e
            l0=l1
            if part==1:res0+=s*first
            else:res0+=last
            s*=-1
        res+=res0
    return res
def parse(inp):
    res=[]
    ll=inp.splitlines()
    for l in ll:
        l0=[int(e) for e in l.split(' ')]
        res+=[l0]
    return res
class T000(unittest.TestCase):
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_0100_(self):
        self.assertEqual(RES01+0,compute(INP01_))
    def test_1000(self):
        self.assertEqual(RES1,compute(parse(open("input1","rt").read())))
    def test_0200(self):
        self.assertEqual(RES02+0,compute(parse(INP01),1))
    def test_2000(self):
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read()),1))
