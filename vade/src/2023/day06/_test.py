import unittest
INP01_="""Time:      7  15   30
Distance:  9  40  200"""
INP01=[[7,9],[15,40],[30,200]]
RES01=288
INP1_="""Time:        41     77     70     96
Distance:   249   1362   1127   1011"""
INP1=[[41,249],[77,1362],[70,1127],[96,1011]]
RES1=771628
INP02=[[71530,940200]]
INP2=[[41777096,249136211271011]]
RES02=71503
RES2=0
def compute(part:int, inp:dict)->int:
    res = 1
    wins=[]
    for (tt,drec) in inp:
        print(f"tt={tt} drec={drec}")
        w=0
        for th in range(tt):
            s=th
            d=s*(tt-th)
            if d>drec:
                w+=1
            #print(f"th={th} s={s} d={d}")
        wins+=[w]
        res*=w
    print(f"res={res} wins={wins}")
    return res
class T000(unittest.TestCase):
    def Ztest_2000(self):
        self.assertEqual(RES2,compute(0, INP2))
    def test_0200(self):
        self.assertEqual(RES02,compute(1, INP02))
    def test_0100(self):
        self.assertEqual(RES01,compute(0, INP01))
    def test_1000(self):
        self.assertEqual(RES1,compute(0, INP1))
