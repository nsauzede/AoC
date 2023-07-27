import copy
def process0(m:dict,s0:dict)->list:
    s=copy.deepcopy(s0)
    if s[rem]==0:
        return s
    
def process(m:dict,s0:dict)->list:
    return 
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def Ztest_000(self):
        s={rem:0,valve:A,opens:[],totals:[]}
        s=process(m0,s)
        self.assertEqual({rem:0,valve:A,opens:{A:1},totals:{A:3}},s)
    def test_900(self):
        s={rem:1,valve:A,opens:[],totals:[]}
        s=process({m1,s)
        self.assertEqual([{},{}],s)
T=4
"""
1 1
2 1 2
3 1 2 2 3 3 4

1: in A; rem=4; opens=[]; total=0; open A
2: in A; rem=3; opens=[A:1]; totals=[A:0]; move to A
3: in A: rem=2; opens=[A:1]; totals=[A:1]; move to A
4: in A: rem=1; opens=[A:1]; totals=[A:2]; move to A
5: in A: rem=0; opens=[A:1]; totals=[A:3]; move to A
"""
m0={
A:{rate:1,tunnels:[A]},
}
m1={
A:{rate:0,tunnels:[A,B]},
B:{rate:1,tunnels:[A,B]},
}
A='A';B='B';rate='rate';tunnels='tunnels'
rem='rem';valve='valve';opens='opens';totals='totals'
