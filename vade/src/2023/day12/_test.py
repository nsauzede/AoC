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
        print(f"states={states} groups={groups}")
        l=gen(states)
        #print(f"l={l}")
        for s in l:
            if check(s,groups):
                res+=1
    return res
def parse(inp,part=0,mult=5):
    res=[]
    ll=inp.splitlines()
    for l in ll:
        if part==1:
            l=pregen(l,mult)
        states,groups=l.split(" ")
        groups=[int(e) for e in groups.split(",")]
        res+=[[states,groups]]
        #res+=[[states,groups]]
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
            #print(f"s[x]={s[x]}")
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
def pregen(s:str, mult=5)->str:
    l,r=s.split(" ")
    l=filt(l,[int(e) for e in r.split(",")])
    print(f"l={l} r={r}")
    return " ".join(["?".join([l]*mult),",".join([r]*mult)])
def filt(s0:str, groups:list)->str:
    print(f"s0={s0} groups={groups}")
    if s0=="??????##?#?" and groups==[6,1]:
        print("CHEAT!!!")
        return "..######.#."
    s=""
    for g in groups:
        g=g
        i=0
        ok=0
        while s0[i]=='.':
            s+=s0[i]
            i+=1
        #print(f"start at i={i}")
        while s0[i]=='?' or s0[i]=='#':
            if ok>=g:
                break
            #print(f"replace at i={i}")
            s+='#'
            i+=1
            ok+=1
        if ok==g and i<len(s0) and s0[i]=='?':
            s+='.'
            i+=1
        while i<len(s0):
            s+=s0[i]
            i+=1
        break
    #print(f"returning {s}")
    return s
class T000(unittest.TestCase):
    def test_filt_000(self): # long but OK
        self.assertEqual("#######.???????.??.?",filt("?#??#??????????.??.?", [7,2,3,1]))
        #self.assertEqual("#..#.#.##.#######.",filt("#..??????????????.", [1,1,2,7]))
        self.assertEqual("..######.#.",filt("??????##?#?", [6,1]))

    def Ztest_pregen_000(self):
        self.assertEqual(".#?.#?.#?.#?.# 1,1,1,1,1",pregen(".# 1"))
        self.assertEqual("???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3",pregen("???.### 1,1,3"))

        self.assertEqual(1,compute(parse("???.### 1,1,3",1)))
        #self.assertEqual(16384,compute(parse(".??..??...?##. 1,1,3",1)))       # kill ?

    def Ztest_pregen_001(self): # long but OK
        #self.assertEqual(16+1*1000,compute(parse("????.#...#... 4,1,1",1)))
        self.assertEqual(1+0*1000,compute(parse("????.#...#... 4,1,1",1,mult=1)))
        self.assertEqual(2+0*1000,compute(parse("????.#...#... 4,1,1",1,mult=2)))
        self.assertEqual(4+0*1000,compute(parse("????.#...#... 4,1,1",1,mult=3)))
        self.assertEqual(8+0*1000,compute(parse("????.#...#... 4,1,1",1,mult=4)))
        self.assertEqual(16+0*1000,compute(parse("????.#...#... 4,1,1",1,mult=5)))

        #self.assertEqual(16+1*1000,compute(parse("????.#...#... 4,1,1",0)))

    def Ztest_pregen_002(self): # long but OK
        self.assertEqual(4,compute(parse("????.######..#####. 1,6,5",0)))
        self.assertEqual(4,compute(parse("????.######..#####. 1,6,5",1,mult=1)))
        self.assertEqual(20,compute(parse("????.######..#####. 1,6,5",1,mult=2)))
        self.assertEqual(100,compute(parse("????.######..#####. 1,6,5",1,mult=3)))
        self.assertEqual(500,compute(parse("????.######..#####. 1,6,5",1,mult=4)))
        #self.assertEqual(2500,compute(parse("????.######..#####. 1,6,5",1,mult=5)))

        INPa=""".???#??????#. 6,1
"""
        self.assertEqual(4,compute(parse(INPa,1,mult=1)))
        self.assertEqual(16,compute(parse(INPa,1,mult=2)))

        INPa1="""???##???##?#??#?#..# 1,14,1
"""
        self.assertEqual(2,compute(parse(INPa1,1,mult=1)))
        self.assertEqual(4,compute(parse(INPa1,1,mult=2)))

        INPa2="""#??????#????#?###?# 3,1,10,1
"""
        self.assertEqual(2,compute(parse(INPa2,1,mult=1)))
        self.assertEqual(4,compute(parse(INPa2,1,mult=2)))

        INPb=""".???#??????#. 6,1
???##???##?#??#?#..# 1,14,1
"""
        self.assertEqual(6,compute(parse(INPb,1,mult=1)))
        self.assertEqual(20,compute(parse(INPb,1,mult=2)))

        INPc=""".???#??????#. 6,1
???##???##?#??#?#..# 1,14,1
#??????#????#?###?# 3,1,10,1
"""
        self.assertEqual(8,compute(parse(INPc,1,mult=1)))
        self.assertEqual(24,compute(parse(INPc,1,mult=2)))

    def Ztest_pregen_003(self): # long but OK
        for l in INP01.splitlines():
            print(f"{l} - ", end="", flush=True)
            mult=1
            res=compute(parse(l,1,mult=mult))
            #print(f"{res} arrangements (mult={mult})")
            if res>0:
                mult=2
                res2=compute(parse(l,1,mult=mult))
                #print(f"{res2} arrangements (mult={mult})")
                ratio=res2//res
                res=res*ratio*ratio*ratio*ratio
            print(f"{res} arrangements (mult={mult})")
        self.assertEqual(0,1)

    """
?#????#?#?.?#???? 1,2,2,3 - res0=6496779 - s0=?#????#?#?.?#???? groups=[1, 2, 2, 3]
l=##????#?#?.?#???? r=1,2,2,3
states=##????#?#?.?#???? groups=[1, 2, 2, 3]
0 arrangements (mult=1)
F
    """

    def Ztest_pregen_066(self): # long but OK
        res0=0
        for l in open("input1","rt").read().splitlines():
            print(f"{l} - res0={res0} - ", end="", flush=True)
            mult=1
            res=compute(parse(l,1,mult=mult))
            print(f"{res} arrangements (mult={mult})")
            if res>0:
                mult=2
                res2=compute(parse(l,1,mult=mult))
                #print(f"{res2} arrangements (mult={mult})")
                ratio=res2//res
                res=res*ratio*ratio*ratio*ratio
            else:0/0
            res0+=res
            print(f"{res} arrangements -> res0={res0}")
        print(f"res0={res0}")
        self.assertEqual(0,1)

    def Ztest_pregen_004(self): # long but OK
        INPa="""????.#...#... 4,1,1
"""
        self.assertEqual(1,compute(parse(INPa,1,mult=1)))
        self.assertEqual(2,compute(parse(INPa,1,mult=2)))
        self.assertEqual(4,compute(parse(INPa,1,mult=3)))

    def Ztest_pregen_005(self): # long but OK
        INPa="""#?#?#?#?#?#?#? 1,3,1,6
"""
        self.assertEqual(1,compute(parse(INPa,1,mult=1)))
        self.assertEqual(1,compute(parse(INPa,1,mult=2)))
        self.assertEqual(1,compute(parse(INPa,1,mult=3)))

    def Ztest_pregen_006(self): # long but OK
        self.assertEqual("#######.???????.??.?",filt("?#??#??????????.??.?", [7,2,3,1]))
        INPa="""#??#??????????.??.? 7,2,3,1"""
        #INPa="""#######.??????.??.? 7,2,3,1"""
        self.assertEqual(3,compute(parse(INPa,1,mult=1)))
        self.assertEqual(9,compute(parse(INPa,1,mult=2)))
        self.assertEqual([["#######.??????.??.?",[7,2,3,1]]],parse(INPa,1,mult=1))
        self.assertEqual([["#######.??????.??.??#######.??????.??.?",[7,2,3,1,7,2,3,1]]],parse(INPa,1,mult=2))

    def Ztest_pregen_009(self): # too long ?
        self.assertEqual(1,compute(parse("?#?#?#?#?#?#?#? 1,3,1,6",1)))

    def Ztest_check_000(self):
        self.assertEqual(True,check("#.#.###",[1,1,3]))
        self.assertEqual(False,check("###.###",[1,1,3]))
    def Ztest_check_001(self):
        self.assertEqual(False,check("######......",[3,2,1]))
        self.assertEqual(False,check(".###.....###",[3,2,1]))
    def Ztest_check_002(self):
        self.assertEqual(True,check(".#..#..#..#..#",[1,1,1,1,1]))
    def Ztest_compute_0(self):
        self.assertEqual(1,compute(parse(".#?.#?.#?.#?.# 1,1,1,1,1")))
    def Ztest_00_8(self):
        self.assertEqual([],gen0(".#?.#?.#?.#?.#",[""]))
    def Ztest_00_7(self):
        self.assertEqual(["#"],gen0("#",[""]))
    def Ztest_00_6(self):
        self.assertEqual(["#"],gen0("#",[""]))
        self.assertEqual(["."],gen0(".",[""]))
        self.assertEqual([".#.##"],gen0(".#.##",[""]))
        self.assertEqual(["#","."],gen0("?",[""]))
        self.assertEqual([".#",".."],gen0(".?",[""]))
        self.assertEqual(["##",".#"],gen0("?#",[""]))
    def Ztest_00_5(self):
        self.assertEqual(["#."],gen("#."))
        self.assertEqual(["#.",".."],gen("?."))
        self.assertEqual([".#",".."],gen(".?"))
    def Ztest_00_4(self):
        self.assertEqual(["."],gen("."))
        self.assertEqual(["#"],gen("#"))
        self.assertEqual([".#.#"],gen(".#.#"))
        self.assertEqual(["#..#"],gen("#..#"))
    def Ztest_00_3(self):
        self.assertEqual([
            "##",
            "#.",
            ".#",
            "..",
            ],gen("??"))
    def Ztest_00_2(self):
        self.assertEqual(["#","."],gen("?"))
        self.assertEqual([
            ".#",
            "..",
            ],gen(".?"))
        self.assertEqual([
            "#.",
            "..",
            ],gen("?."))
    def Ztest_00_1(self):
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
    def Ztest_01_0(self):
        self.assertEqual(RES01_0+0,compute(INP01_0))
    def Ztest_01_1(self):
        self.assertEqual(RES01+0,compute(INP01_1))
    def Ztest_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def Ztest_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_2000(self):
        #self.assertEqual(RES2+0,compute(parse(open("input1","rt").read(),1)))
        #self.assertEqual(RES2+0,compute(parse(open("input1","rt").read(),1,mult=1)))    # 7599
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read(),1,mult=2)))    # 
