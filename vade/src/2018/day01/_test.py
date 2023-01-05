res0 = -6
res1 = 582
res0_2 = 0
res1_2 = 488
def load(name):return open(name,"rt").read()
def apply2(s,loop=True):
    f=0
    f1=None
    seen=set()
    seen.add(0)
    done=False
    lines=s.splitlines()
    while not done:
        for s in lines:
            f+=int(s)
            #print(f"s={s} f={f} len(seen)={len(seen)}")
            if loop and not f1:
                if f not in seen:
                    seen.add(f)
                else:
                    f1=f
                    done=True
                    break
            if done:break
        if not loop:break
        #break
    return f,f1
def apply(s):return apply2(s,loop=False)[0]
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res0,apply("-1\n-2\n-3\n"))
    def test_001(self):
        self.assertEqual(3,apply("+1\n+1\n+1\n"))
    def test_002(self):
        self.assertEqual(3,apply("+1\n-2\n+3\n+1\n"))
    def test_003(self):
        self.assertEqual(0,apply("+1\n+1\n-2\n"))
    def test_004(self):
        self.assertEqual(res0,apply(load("input0")))
    def test_100(self):
        self.assertEqual(res1,apply(load("input1")))
    def test_200(self):
        self.assertEqual(0,apply2("+1\n-1\n")[1])
    def test_201(self):
        self.assertEqual(2,apply2("+1\n-2\n+3\n+1\n")[1])
    def test_202(self):
        self.assertEqual(10,apply2("+3\n+3\n+4\n-2\n-4\n")[1])
    def test_203(self):
        self.assertEqual(5,apply2("-6\n+3\n+8\n+5\n-6\n")[1])
    def test_204(self):
        self.assertEqual(14,apply2("+7\n+7\n-2\n-7\n-4\n")[1])
    def test_210(self):
        self.assertEqual(res1_2,apply2(load("input1"))[1])
