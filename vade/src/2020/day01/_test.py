res0 = 514579
res1 = 1019571
res0_2 = 241861950
res1_2 = 100655544
def load(name):return open(name,"rt").read()
def process(s):
    lines=[int(l) for l in s.splitlines()]
    for l in lines:
        for m in lines:
            add=l+m
            if add==2020:
                return l*m
    return 0
def process2(s):
    lines=[int(l) for l in s.splitlines()]
    for l in lines:
        for m in lines:
            for n in lines:
                add=l+m+n
                if add==2020:
                    return l*m*n
    return 0
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res0,process(load("input0")))
    def test_100(self):
        self.assertEqual(res1,process(load("input1")))
    def test_200(self):
        self.assertEqual(res0_2,process2(load("input0")))
    def test_210(self):
        self.assertEqual(res1_2,process2(load("input1")))
