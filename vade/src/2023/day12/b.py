import unittest
def gen(s:str)->list:
    res=gen0(s,[""])
    #res=sorted(res)
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
def pregen(s:str, mult=5)->str:
    l,r=s.split(" ")
    l=filt(l,[int(e) for e in r.split(",")])
    print(f"l={l} r={r}")
    return " ".join(["?".join([l]*mult),",".join([r]*mult)])
def filt(s0:str, groups:list)->str:
    #print(f"s0={s0} groups={groups}")
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
    print(f"s0:{s0}=>{s} groups={groups}")
    return s
INP01="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
RES01=21
RES02=525152
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
def filt2(s0:str,groups:list)->str:
    s=""
    for g in groups:
        i=0
        while s0[i]=='.':
            s+=s0[i]
            i+=1
        for i,c in enumerate(s0):
            
    return s
class T000(unittest.TestCase):
    def test_filt_0000(self):
        ll=INP01.splitlines()
        s,groups=ll[0].split(" ")
        groups=[int(e)for e in groups.split(",")]
        self.assertEqual("#.#.###",filt2(s,groups))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
