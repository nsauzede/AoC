import unittest
#@unittest.skip
inp01="""1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
inp02="""two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""
res01=142
res1=55816
res02=281
#res2=54970      # too low ?
res2=54980      # must always keep last letter to begin a new word ? [sigh]
def compute(part:int, inp:str)->int:
    res = 0
    for s in inp.splitlines():
        num0=0
        num1=0
        word0=""
        for c in s:
            if c.isdigit():
                word0=""
                if num0==0:
                    num0 = int(c)
                else:
                    num1 = int(c)
            elif part==1:
                word0+=c
                words=["one","two","three","four","five","six","seven","eight","nine"]
                for i in range(len(word0)):
                    try:
                        n = words.index(word0[i:]) + 1
                        if num0 == 0:
                            num0 = n
                        else:
                            num1 = n
                        word0=c
                        break
                    except:
                        pass
        if num1==0:
            num1 = num0
        res += num0*10+num1
    return res
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res01,compute(0, inp01))
    def test_001(self):
        self.assertEqual(res1,compute(0, open("input1","rt").read()))
    def test_100(self):
        self.assertEqual(res02,compute(1, inp02))
    def test_102(self):
        self.assertEqual(res2,compute(1, open("input1","rt").read()))
    def test_1020(self):
        self.assertEqual(22,compute(1, "2"))
        self.assertEqual(33,compute(1, "three"))
