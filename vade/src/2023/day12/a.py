import unittest
INP01="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
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
                print(f"s={s} c={c}")
                res0[j]=s+c
    res=res0
    return res
def gen(s:str)->list:
    res=gen0(s,[""])
    #res=sorted(res)
    return res
class T000(unittest.TestCase):
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
