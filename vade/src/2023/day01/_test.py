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
def calc01(inp:list)->list:
    print(inp)
    res = []
    for s in inp:
        num0=""
        num1=""
        for c in s:
            if c.isdigit():
                if num0=="":
                    num0 = c
                else:
                    num1 = c
        if num1=="":
            num1 = num0
        res += [int(num0+num1)]
    return res
def puz01(inp:str)->int:
    l=inp.splitlines()
    return sum(calc01(l))
def fw2n(w:str)->str:
    w2n={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    res = None
    for i in range(len(w)):
        if w[i:] in w2n:
            res = w2n[w[i:]]
    return res
def calc02(inp:list)->list:
    print(inp)
    res = []
    for s in inp:
        num0=""
        num1=""
        word0=""
        print(f"s={s}")
        for c in s:
            if c.isdigit():
                word0=""
                if num0=="":
                    num0 = c
                else:
                    num1 = c
            else:
                word0+=c
                n=fw2n(word0)
                if n:
                    if num0 == "":
                        num0 = n
                    else:
                        num1 = n
                    word0=c
        if num1=="":
            num1 = num0
        res0 = int(num0+num1)
        res += [res0]
    return res
def puz02(inp:str)->int:
    l=inp.splitlines()
    return sum(calc02(l))
def load(name):return open(name,"rt").read()
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(res01,puz01(inp01))
    def test_001(self):
        self.assertEqual(res1,puz01(load("input1")))
    def test_100(self):
        self.assertEqual(res02,puz02(inp02))
    def test_102(self):
        self.assertEqual(res2,puz02(load("input1")))
    def test_1020(self):
        self.assertEqual([22],calc02(["2"]))
        self.assertEqual([33],calc02(["three"]))
