res0 = 9
res1 = 1034
res0_2 = 0
res1_2 = 1356
def load(name):return open(name,"rt").read().strip()
def captcha(s):
    n=0
    last=s[-1]
    for c in s:
        #print(f"Seen c={c} n={n} last={last}")
        if c==last:
            n+=int(c)
        last=c
    return n
def captcha2(s):
    n=0
    l=len(s)
    h=l//2
    for i,c in enumerate(s):
        #print(f"Seen c={c} n={n} last={last}")
        if c==s[(i+h)%l]:
            n+=int(c)
    return n
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res0,captcha("91212129"))
    def test_001(self):
        self.assertEqual(res0,captcha(load("input0")))
    def test_002(self):
        self.assertEqual(3,captcha("1122"))
    def test_003(self):
        self.assertEqual(4,captcha("1111"))
    def test_004(self):
        self.assertEqual(0,captcha("1234"))
    def test_100(self):
        self.assertEqual(res1,captcha(load("input1")))
    def test_200(self):
        self.assertEqual(6,captcha2("1212"))
    def test_201(self):
        self.assertEqual(0,captcha2("1221"))
    def test_202(self):
        self.assertEqual(4,captcha2("123425"))
    def test_203(self):
        self.assertEqual(12,captcha2("123123"))
    def test_204(self):
        self.assertEqual(4,captcha2("12131415"))
    def test_200(self):
        self.assertEqual(res1_2,captcha2(load("input1")))
