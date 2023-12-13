import unittest
INP01="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
RES01=405
RES1=33195
RES02=400
#RES2=25046      # too low
RES2=0
def compute(inp:list,part=0)->int:
    res = 0
    for r in inp:
        sh=scanH(r)
        sv=scanV(r)
        print(f"r={r} sh={sh} sv={sv}")
        res+=sv*100+sh
    return res
def parse(inp,part=0,mult=5):
    res=[]
    ll=inp.splitlines()
    res0=[]
    for l in ll:
        if l=="":
            res+=[res0]
            res0=[]
        else:
            #res0+=[[c for c in l]]
            res0+=[l]
    if res0!=[]:
        res+=[res0]
    return res
def scanH(m):
    res=0
    #h=len(m)
    w=len(m[0])
    for i in range(w-1):
        #print(f"i={i}")
        res0=False
        for j,s in enumerate(m):
            #print(f"j={j} s={s}")
            l=s[:i+1][::-1]
            r=s[i+1:]
            #print(f"l={l} r={r}")
            res0=True
            for k,c in enumerate(l):
                if k>=len(r):
                    break
                if c!=r[k]:
                    res0=False
                    break
            #print(f"res0={res0}")
            if not res0:
                break
        if res0:
            #print(f"Found {i+1} to be reflectionH")
            res=i+1
            break
    return res
def disp(m,text="DISP"):
    print(f"{text} -----")
    for r in m:
        print("".join(r))
def scanV(m):
    res=0
    h=len(m)
    w=len(m[0])
    #disp(m)
    for j in range(h-1):
        #print(f"j={j}")
        res0=False
        for i in range(w):
            #print(f"i={i}")
            res0=True
            for k in range(h-j-1):
                if j-k<0:
                    break
                #print(f"j+1+k={j+1+k}:'{m[j+1+k]}' j-k={j-k}:'{m[j-k]}'")
                if m[j+1+k]!=m[j-k]:
                    res0=False
                    break
            #print(f"res0={res0}")
            if not res0:
                break
        if res0:
            #print(f"Found {j+1} to be reflectionV")
            res=j+1
            break
    return res
def smudge(m):
    res=0
    disp(m,"INITIAL")
    rh0=0;rv0=0
    #rh0=scanH(m)
    #rv0=scanV(m)
    #print(f"rh0={rh0} rv0={rv0}")
    for j,r in enumerate(m):
        l=[c for c in r]
        for i,c in enumerate(r):
            if c=='.':
                c2='#'
            else:
                c2='.'
            l[i]=c2
            m[j]="".join(l)
            #disp(m,f"WITH {(j,i)}:'{c}'=>'{c2}'")
            rh=scanH(m)
            rv=scanV(m)
            #print(f"j={j} i={i} c={c}=>{c2} rh={rh} rv={rv} rh0={rh0} rv0={rv0}")
            if (rh or rv) and (rh0!=rh and rv0!=rv):
                #print(f"j={j} i={i} c={c}=>{c2} rh={rh} rv={rv}")
                return [j,i]
            l[i]=c
            m[j]=["".join(l)]
            break
        break
    return res
def compute1(inp):
    res=0
    for n,m in enumerate(inp):
        rh0=scanH(m)
        rv0=scanV(m)
        #print(f"rh0={rh0} rv0={rv0}")
        res0=0
        for j,r in enumerate(m):
            l=[c for c in r]
            for i,c in enumerate(r):
                if c=='.':
                    c2='#'
                else:
                    c2='.'
                l[i]=c2
                m[j]="".join(l)
                #disp(m,f"WITH {(j,i)}:'{c}'=>'{c2}'")
                rh=scanH(m)
                rv=scanV(m)
                #print(f"COMPUTE1 j={j} i={i} c={c}=>{c2} rh={rh} rv={rv} rh0={rh0} rv0={rv0}")
                if (rh0!=rh and rh>0) or (rv0!=rv and rv>0):
                    #print(f"j={j} i={i} c={c}=>{c2} rh={rh} rv={rv}")
                    if rv0!=rv:
                        res0+=rv*100
                    if rh0!=rh:
                        res0+=rh
                    print(f"COMPUTE1 n={n} j={j} i={i} c={c}=>{c2} res0={res0} rh={rh} rv={rv} rh0={rh0} rv0={rv0}")
                    #break
                l[i]=c
                m[j]=["".join(l)]
            #if res0>0:break
        res+=res0
    return res
class T000(unittest.TestCase):
    def Ztest_smudge_0001(self):
        INPa="""#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual([1,4],smudge(parse(INPa)[0]))
    def test_smudge_0000(self):
        INPa="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        self.assertEqual([0,0],smudge(parse(INPa)[0]))
    def test_scanV_0002(self):
        INPa="""..##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        self.assertEqual(3+0*1000,scanV(parse(INPa)[0]))
    def test_scanV_0001(self):
        INPa="""#...##..#
#...##..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(1+0*1000,scanV(parse(INPa)[0]))
    def test_scanV_0000(self):
        INPa="""#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(4,scanV(parse(INPa)[0]))
    def test_scanH_0001(self):
        INPa="""#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(0,scanH(parse(INPa)[0]))
    def test_scanH_0000(self):
        INPa="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        self.assertEqual(5,scanH(parse(INPa)[0]))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES02+1*1000,compute1(parse(INP01)))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute1(parse(open("input1","rt").read())))
