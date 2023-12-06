import unittest
INP01=[[7,9],[15,40],[30,200]]
RES01=288
INP1=[[41,249],[77,1362],[70,1127],[96,1011]]
RES1=771628
INP02=[[71530,940200]]
INP2=[[41777096,249136211271011]]
RES02=71503
RES2=27363861
def compute(inp:dict)->int:
    res = 1
    for (tt,drec) in inp:
        w=0
        for th1 in range(tt):
            s=th1
            d=s*(tt-th1)
            if d>drec:
                break
        for th2 in range(tt-1,-1,-1):
            s=th2
            d=s*(tt-th2)
            if d>drec:
                break
        if th2>th1:
            w=th2-th1+1
        res*=w
    return res
class T000(unittest.TestCase):
    def test_2000(self):
        self.assertEqual(RES2,compute(INP2))
    def test_0200(self):
        self.assertEqual(RES02,compute(INP02))
    def test_0100(self):
        self.assertEqual(RES01,compute(INP01))
    def test_1000(self):
        self.assertEqual(RES1,compute(INP1))
