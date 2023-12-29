import unittest
def check(s,groups):
    x=0
    for g in groups:
        ok=0
        if x>=len(s):
            return False
        while x<len(s) and s[x]=='.':
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
        if x<len(s):
            if s[x]!='.':
                return False
            x+=1
    while x<len(s):
        if s[x]!='.':
            return False
        x+=1
    return True
def filt(s0:str,groups:list)->str:
    res0=gen(s0,groups)
    #print(f"s0={s0} groups={groups} res0={res0}")
    res=[]
    for r in res0:
        if check(r,groups):
            res+=[r]
    #print(f"res={res}")
    l=0
    if len(res)>0:
        l=len(res[0])
    s=""
    for i in range(l):
        res0=True
        c=res[0][i]
        for r in res:
            if r[i]!=c:
                res0=False
                break
        #print(f"i={i} c={c} res0={res0}")
        if res0:
            s+=c
        else:
            s+=s0[i]
    return s
def gen(s:str,groups:list)->list:
    res=gen0(s,groups,[""])
    return res
def gen0(s:str,groups:list,l0:list)->list:
    res0=l0.copy()
    for i,c in enumerate(s):
        if c=='?':
            res=[]
            for j,s in enumerate(res0):
                r1=[s+'#']
                res+=r1
                r2=[s+'.']
                res+=r2
            res0=res
            #print(f"?: res0={res0}")
        else:
            for j,s in enumerate(res0):
                res0[j]=s+c
            #print(f"{c}: res0={res0}")
    res=res0
    return res
def gen2(s:str,groups:list)->list:
    res0=[""]
    for i,c in enumerate(s):
        if c=='?':
            res=[]
            for j,s in enumerate(res0):
                r1=[s+'#']
                res+=r1
                r2=[s+'.']
                res+=r2
            res0=res
            #print(f"?: res0={res0}")
        else:
            for j,s in enumerate(res0):
                res0[j]=s+c
            #print(f"{c}: res0={res0}")
    print(f"prefinal res0={len(res0)}")
    res=[]
    num=0
    for r in res0:
        if check(r,groups):
            #res+=[r]
            num+=1
    print(f"final res={len(res)} num={num}")
    #return res
    return num
def compute00(s0:str,groups:list,part=0,mult=1)->int:
    res = 0
    if part==0:
        s=filt(s0,groups)
    elif part==1:
        s=s0
        #s=filt(s,groups)
        print("PREGEN!!")
        s,groups=pregen(s,groups,mult)
        #print("FILT!!")
        #s=filt(s,groups)
        print(f"Using s={s} groups={groups}")
    print("GEN2!!")
    res = gen2(s,groups)
    print(f"res={res}")
    return res
    res0=gen(s,groups)
    for r in res0:
        if check(r,groups):
            res+=1
    #print(f"res={res}")
    return res
def compute00BAD(s0:str,groups:list,part=0,mult=1)->int:
    res = 0
    if part==0:
        s=filt(s0,groups)
    elif part==1:
        s=s0
        s=filt(s,groups)
        s,groups=pregen2(s,groups,mult)
        #s=filt(s,groups)
        print(f"Using s={s} groups={groups}")
        return gen2(s,groups)

    return gen2(s,groups)
    res0=gen(s,groups)
    for r in res0:
        if check(r,groups):
            res+=1
    #print(f"res={res}")
    return res
def pregen1(s:str, groups:list, mult=5)->tuple:
    return ".".join([s]*mult),groups*mult
def pregen2(s:str, groups:list, mult=5)->tuple:
    return "#".join([s]*mult),groups*mult
def compute0(s0:str,groups:list,part=0,mult=5)->int:
    res1=compute00(s0,groups,part,1)
    #print(f"res1={res1}")
    if mult==1:
        print(f"returning res1={res1}")
        return res1
    res2=res1
    n=2
    while res1==res2:
        if n>2:
            #0/0
            break
        print(f"computing n={n} s0={s0} groups={groups}.. (res1={res1} )")
        res2=compute00(s0,groups,part,n)
        print(f"res2={res2} n={n}")
        if mult==n:
            print(f"returning res2={res2} n={n}")
            return res2
        n+=1
    ratio=res2//res1
    res=res2
    for i in range(mult-2):
        res*=ratio
    print(f"returning res={res} ratio={ratio}")
    return res
def compute(l:list,part=0,mult=5):
    res = 0
    for i,(s,groups) in enumerate(l):
        print(f"COMPUTING #{i} s={s} groups={groups}.. (res={res}) -----------------------")
        if part==0:
            res+=compute0(s,groups,part,mult)
        else:
            if mult>=2:
                res1=compute0(s,groups,part,mult=1)
                gg=groups+groups
                priont""
                s1=filt(s+".",groups)+s
                #s=filt(s,groups)
                res2=compute0(s1,gg,part,mult=1)
                s2=filt(s+"#",groups)+s
                res2+=compute0(s2,gg,part,mult=1)
                if res1==res2:
                    res+=res1
                else:
                    ratio=res2//res1
                    n=1
                    while n<mult:
                        res1*=ratio
                        n+=1
                    res+=res1
    return res
def parse(inp:str)->list:
    res=[]
    for l in inp.splitlines():
        s,groups=l.split(" ")
        groups=[int(e) for e in groups.split(",")]
        res+=[[s,groups]]
    return res
def pregen(s:str, groups:list, mult=5)->tuple:
    return "?".join([s]*mult),groups*mult
"""
Part 1
    ???.### 1,1,3 - 1 arrangement
    .??..??...?##. 1,1,3 - 4 arrangements
    ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
    ????.#...#... 4,1,1 - 1 arrangement
    ????.######..#####. 1,6,5 - 4 arrangements
    ?###???????? 3,2,1 - 10 arrangements
Part 2
    ???.### 1,1,3 - 1 arrangement
    .??..??...?##. 1,1,3 - 16384 arrangements
    ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
    ????.#...#... 4,1,1 - 16 arrangements
    ????.######..#####. 1,6,5 - 2500 arrangements
    ?###???????? 3,2,1 - 506250 arrangements
"""
class T000(unittest.TestCase):
    def Ztest_0102(self):
        self.assertEqual(("???.###", [1,1,3]),pregen("???.###", [1,1,3], mult=1))
        self.assertEqual(("???.###????.###", [1,1,3,1,1,3]),pregen("???.###", [1,1,3], mult=2))

    def Ztest_0101(self):
        self.assertEqual(1,compute0("???.###", [1,1,3]))
        self.assertEqual(4,compute0(".??..??...?##.", [1,1,3]))
        self.assertEqual(1,compute0("?#?#?#?#?#?#?#?", [1,3,1,6]))
        self.assertEqual(1,compute0("????.#...#...", [4,1,1]))
        self.assertEqual(4,compute0("????.######..#####.", [1,6,5]))
        self.assertEqual(10,compute0("?###????????", [3,2,1]))

    def Ztest_0200(self):
        self.assertEqual(1,compute0("???.###", [1,1,3], part=1))
        self.assertEqual(16384,compute0(".??..??...?##.", [1,1,3], part=1))
        self.assertEqual(1,compute0("?#?#?#?#?#?#?#?", [1,3,1,6], part=1))
        self.assertEqual(16,compute0("????.#...#...", [4,1,1], part=1))
        self.assertEqual(2500,compute0("????.######..#####.", [1,6,5], part=1))
        self.assertEqual(506250,compute0("?###????????", [3,2,1], part=1))

    def Ztest_0220(self):
        #
        self.assertEqual(1,compute0("???.###", [1,1,3], part=1))

        self.assertEqual(1,compute0("???.###", [1,1,3], part=1,mult=1))

        self.assertEqual(1,compute0("???.###", [1,1,3], part=1,mult=2))
        self.assertEqual(1,compute0("???.###.???.###", [1,1,3,1,1,3], part=1,mult=1))
        self.assertEqual(0,compute0("???.####???.###", [1,1,3,1,1,3], part=1,mult=1))

        #
        self.assertEqual(16384,compute0(".??..??...?##.", [1,1,3], part=1))

        self.assertEqual(    4,compute0(".??..??...?##.", [1,1,3], part=1,mult=1))

        self.assertEqual(   32,compute0(".??..??...?##.", [1,1,3], part=1,mult=2))
        self.assertEqual(   16,compute0(".??..??...?##...??..??...?##.", [1,1,3,1,1,3], part=1,mult=1))
        self.assertEqual(   16,compute0(".??..??...?##.#.??..??...?##.", [1,1,3,1,1,3], part=1,mult=1))

        #
        self.assertEqual(1,compute0("?#?#?#?#?#?#?#?", [1,3,1,6], part=1))

        self.assertEqual(1,compute0("?#?#?#?#?#?#?#?", [1,3,1,6], part=1,mult=1))

        self.assertEqual(1,compute0("?#?#?#?#?#?#?#?", [1,3,1,6], part=1,mult=1))
        self.assertEqual(1,compute0("?#?#?#?#?#?#?#?.?#?#?#?#?#?#?#?", [1,3,1,6,1,3,1,6], part=1,mult=1))
        self.assertEqual(0,compute0("?#?#?#?#?#?#?#?#?#?#?#?#?#?#?#?", [1,3,1,6,1,3,1,6], part=1,mult=1))

        #
        self.assertEqual(16,compute0("????.#...#...", [4,1,1], part=1))

        self.assertEqual( 1,compute0("????.#...#...", [4,1,1], part=1,mult=1))

        self.assertEqual( 2,compute0("????.#...#...", [4,1,1], part=1,mult=2))
        self.assertEqual( 1,compute0("????.#...#....????.#...#...", [4,1,1,4,1,1], part=1,mult=1))
        self.assertEqual( 1,compute0("????.#...#...#????.#...#...", [4,1,1,4,1,1], part=1,mult=1))

        #
        self.assertEqual(2500,compute0("????.######..#####.", [1,6,5], part=1))

        self.assertEqual(   4,compute0("????.######..#####.", [1,6,5], part=1,mult=1))

        self.assertEqual(  20,compute0("????.######..#####.", [1,6,5], part=1,mult=2))
        self.assertEqual(  16,compute0("????.######..#####..????.######..#####.", [1,6,5,1,6,5], part=1,mult=1))
        self.assertEqual(   4,compute0("????.######..#####.#????.######..#####.", [1,6,5,1,6,5], part=1,mult=1))

        #
        self.assertEqual(506250,compute0("?###????????", [3,2,1], part=1))

        self.assertEqual(    10,compute0("?###????????", [3,2,1], part=1,mult=1))

        self.assertEqual(   150,compute0("?###????????", [3,2,1], part=1,mult=2))
        self.assertEqual(   100,compute0("?###????????.?###????????", [3,2,1,3,2,1], part=1,mult=1))
        self.assertEqual(    50,compute0("?###????????#?###????????", [3,2,1,3,2,1], part=1,mult=1))

    def Ztest_0201(self):
        self.assertEqual(32,compute0(".??..??...?##.", [1,1,3], part=1,mult=2))
        self.assertEqual(32,compute0(".??..??...?##.?.??..??...?##.", [1,1,3,1,1,3], part=1,mult=1))
        self.assertEqual(32,compute0(".??..??...?##.?.??..??...?##.", [1,1,3,1,1,3], part=0,mult=1))
        self.assertEqual(16,compute0(".??..??...?##...??..??...?##.", [1,1,3,1,1,3], part=0,mult=1))
        self.assertEqual(16,compute0(".??..??...?##.#.??..??...?##.", [1,1,3,1,1,3], part=0,mult=1))

        self.assertEqual(16,compute0("????.#...#...", [4,1,1], part=1))

    def test_0203(self):
        self.assertEqual( 12,compute0("?#??#??????????.??.?", [7, 2, 3, 1], part=1,mult=1))

        groups=[7, 2, 3, 1]
        s="?#??#??????????.??.?"
        s=filt(s,groups)
        gg=groups+groups
        s1=s+"."+s
        s10=filt(s1,gg)
        print(f"s1={s1} s10={s10}")
        self.assertEqual(144,compute0("?######??#??##?.??.?.?######??#??##?.??.?", [7, 2, 3, 1,7, 2, 3, 1], part=1,mult=1))
        self.assertEqual( 12,compute0("?######??#??##?.??.?#?######??#??##?.??.?", [7, 2, 3, 1,7, 2, 3, 1], part=1,mult=1))

        print(f"ALERT!!")
        #self.assertEqual(  0,compute0("?#??#??????????.??.?", [7, 2, 3, 1], part=1,mult=2))

        self.assertEqual(   0,compute0("?#??#??????????.??.?.?#??#??????????.??.?", [7, 2, 3, 1,7, 2, 3, 1], part=1,mult=1))
        print(f"END OF ALERT.")

    def Ztest_0202(self):
        INPa="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
        self.assertEqual(525152,compute(parse(INPa), part=1))
        """
Problem:
computing s=?#??#??????????.??.? groups=[7, 2, 3, 1].. (res=17846129)
Using s=?######??#??##?.??.? groups=[7, 2, 3, 1]
"""
    def Ztest_ZE01000(self):
        INP="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
        self.assertEqual(21,compute(parse(INP), part=0))
    def test_ZE02000(self):
        INP="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
        self.assertEqual(525152,compute(parse(INP), part=1))
    def Ztest_2000(self):
        self.assertEqual(0,compute(parse(open("input1").read()), part=1))
    def Ztest_1000(self):
        self.assertEqual(7599,compute(parse(open("input1").read()), part=0))

    def Ztest_0100(self):
        self.assertEqual(["#.###","..###"],gen("?.###"))
        self.assertEqual(True,check("#.###",[1,3]))
        self.assertEqual(False,check("..###",[1,3]))

        self.assertEqual("#.#.###",filt("???.###", [1,1,3]))
        self.assertEqual(".??..??...###.",filt(".??..??...?##.", [1,1,3]))
        self.assertEqual(".#.###.#.######",filt("?#?#?#?#?#?#?#?", [1,3,1,6]))
        self.assertEqual("####.#...#...",filt("????.#...#...", [4,1,1]))
        self.assertEqual("????.######..#####.",filt("????.######..#####.", [1,6,5]))
        self.assertEqual(".###.???????",filt("?###????????", [3,2,1]))
