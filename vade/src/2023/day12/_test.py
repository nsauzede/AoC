import unittest
INP01="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
INP01_0=[["?###????????",[ 3,2,1]],]
RES01_0=10
INP01_1=[["???.###",[ 1,1,3]],
[".??..??...?##.",[ 1,1,3]],
["?#?#?#?#?#?#?#?",[ 1,3,1,6]],
["????.#...#...",[ 4,1,1]],
["????.######..#####.",[ 1,6,5]],
["?###????????",[ 3,2,1]],
]
RES01=21
RES1=7599
RES2=0
def compute(inp:list,part=0)->int:
    res = 0
    for r in inp:
        states,groups=r
        #print(f"states={states} groups={groups}")
        l=gen(states)
        #print(f"l={l}")
        for s in l:
            if check(s,groups):
                res+=1
    return res
def parse(inp):
    res=[]
    ll=inp.splitlines()
    for l in ll:
        states,groups=l.split(" ")
        groups=[int(e) for e in groups.split(",")]
        res+=[[states,groups]]
    return res
def gen0(s:str,l0:list)->list:
    res0=l0.copy()
    for i,c in enumerate(s):
        if c=='?':
            res=[]
            for j,s in enumerate(res0):
                res+=[s+'#']
                res+=[s+'.']
            res0=res
        else:
            for j,s in enumerate(res0):
                #print(f"s={s} c={c}")
                res0[j]=s+c
    res=res0
    return res
def gen(s:str)->list:
    res=gen0(s,[""])
    #res=sorted(res)
    return res
def check(s,groups):
    x=0
    #print(f"s={s} groups={groups}")
    for g in groups:
        #print(f"g={g} x={x} len={len(s)}")
        ok=0
        if x>=len(s):
            return False
        while x<len(s) and s[x]=='.':
            #print("SKIP.")
            x+=1
        if x>=len(s):
            return False
        while ok<g:
            if x>=len(s):
                return False
            if s[x]!='#':
                return False
            ok+=1
            x+=1
        #print(f"x={x}")
        if x<len(s):
            if s[x]!='.':
                return False
            x+=1
        #print(f"group {g} is OK")
    while x<len(s):
        if s[x]!='.':
            return False
        x+=1
    #print(f"s={s} groups={groups} TRUE!!")
    return True
class T000(unittest.TestCase):
    def test_check_000(self):
        self.assertEqual(True,check("#.#.###",[1,1,3]))
        self.assertEqual(False,check("###.###",[1,1,3]))
    def test_check_001(self):
        self.assertEqual(False,check("######......",[3,2,1]))
        self.assertEqual(False,check(".###.....###",[3,2,1]))
    def test_00_1(self):
        self.assertEqual(["#"],gen0("#",[""]))
        self.assertEqual(["."],gen0(".",[""]))
        self.assertEqual([".#.##"],gen0(".#.##",[""]))
        self.assertEqual(["#","."],gen0("?",[""]))
        self.assertEqual([".#",".."],gen0(".?",[""]))
        self.assertEqual(["##",".#"],gen0("?#",[""]))
    def test_00_0(self):
        self.assertEqual(["#."],gen("#."))
        self.assertEqual(["#.",".."],gen("?."))
        self.assertEqual([".#",".."],gen(".?"))
    def test_00_0(self):
        self.assertEqual(["."],gen("."))
        self.assertEqual(["#"],gen("#"))
        self.assertEqual([".#.#"],gen(".#.#"))
        self.assertEqual(["#..#"],gen("#..#"))
    def test_00_5(self):
        self.assertEqual([
            "##",
            "#.",
            ".#",
            "..",
            ],gen("??"))
    def test_00_6(self):
        self.assertEqual(["#","."],gen("?"))
        self.assertEqual([
            ".#",
            "..",
            ],gen(".?"))
        self.assertEqual([
            "#.",
            "..",
            ],gen("?."))
    def test_00_1(self):
        self.assertEqual([
            "###.###",
            "##..###",
            "#.#.###",
            "#...###",
            ".##.###",
            ".#..###",
            "..#.###",
            "....###",
            ],gen("???.###"))
    def test_01_0(self):
        self.assertEqual(RES01_0+0,compute(INP01_0))
    def Ztest_01_1(self):
        self.assertEqual(RES01+0,compute(INP01_1))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_2000(self):
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read()),1))
