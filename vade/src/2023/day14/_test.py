import unittest
INP01="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
INP0201="""...#
..##
.###
####
"""
INP0202="""####
.###
..##
...#
"""
INP0102="""OOOO.#.O
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""
INP0101=[['O','O','O','O','.','#','.','O','.','.'],
['O','O','.','.','#','.','.','.','.','#'],
['O','O','.','.','O','#','#','.','.','O'],
['O','.','.','#','.','O','O','.','.','.'],
['.','.','.','.','.','.','.','.','#','.'],
['.','.','#','.','.','.','.','#','.','#'],
['.','.','O','.','.','#','.','O','.','O'],
['.','.','O','.','.','.','.','.','.','.'],
['#','.','.','.','.','#','#','#','.','.'],
['#','.','.','.','.','#','.','.','.','.'],
]
RES01=136
RES1=112048
RES02=64
#RES2=105642     # too high
#RES2=105594     # too low
RES2=105606
from copy import deepcopy
def cycle(m,n=1)->int:
    res=0
    m0={}
    seen=[]
    cnt=0
    seeni0=[]
    seencomp0=[]
    seenm0=[]
    for i in range(n):
        print(f"i={i}")
        #disp(m,f"COMPUTE before0")
        m=tiltN(m)                              # N
        #disp(m,f"COMPUTE before0 N <====")
        m=transpL(tiltN(transpR(m)))            # W
        #disp(m,f"COMPUTE before0 W <====")
        m=transpL(m)
        #disp(m,f"COMPUTE before0 transpL")
        m=transpL(m)
        #disp(m,f"COMPUTE before0 transpL")
        m=tiltN(m)
        #disp(m,f"COMPUTE before0 tiltN")
        m=transpR(m)
        #disp(m,f"COMPUTE before0 transpR")
        m=transpR(m)                            # S
        #disp(m,f"COMPUTE before0 S <====")
        m=transpL(m)
        #disp(m,f"COMPUTE before0 transpL")
        m=tiltN(m)
        #disp(m,f"COMPUTE before0 tiltN")
        m=transpR(m)                            # E
        #disp(m,f"COMPUTE before0 E <====")
        strm=str(m)
        comp=compute0(m)
        if strm in m0:
            i0,comp0=m0[strm]
            print(f"seen loop at i={i}, found for {i0} comp0={comp0} cnt={cnt} comp={comp}")
            if i0 in seeni0:
                idx=seeni0.index(i0)
                zecomp0=seencomp0[idx]
                zem0=seenm0[idx]
                print(f"Skipping dejavu-loop at i={i}, found for {i0} cnt={cnt} wished cycles={n} idx={idx} zecomp0={zecomp0}")
                #m=zem0
                res=seencomp0[(n-seeni0[0]-1)%(len(seeni0))]
                break
            else:
                seeni0+=[i0]
                seencomp0+=[comp0]
                seenm0+=[m]
                print(f"seeni0={seeni0}")
                print(f"seencomp0={seencomp0}")
            if cnt>1000:
                print(f"Skipping loop at i={i}, found for {i0} cnt={cnt}  WATCHDOG!!!!!")
                break
            cnt+=1
        else:
            m0[strm]=(i,comp)
            print(f"No loop at i={i}, comp={comp}")
        res=comp
    return res
def compute0(m:list)->int:
    res = 0
    h=len(m)
    #print(f"h={h} m={m}")
    #disp(m,f"COMPUTE0 after h={h}")
    #if part==1:return
    for j,r in enumerate(m):
        for c in r:
            if c=='O':
                res+=h-j
    return res
def compute(m:list,part=0,cycles=1000000000)->int:
    if part==0:
        m=tiltN(m)
    elif part==1:
        return cycle(m,cycles)
    disp(m,f"COMPUTE part={part}")
    return compute0(m)
def parse(inp,part=0):
    res=[]
    ll=inp.splitlines()
    for l in ll:
        res0=[]
        for c in l:
            res0+=c
        res+=[res0]
    return res
def disp(m,text="DISP"):
    print(f"\n{text}")
    h=len(m)
    for i,r in enumerate(m):
        print(f"{i: 2} {''.join(r)} {h-i}")
def tiltN(m):
    h=len(m)
    w=len(m[0])
    #print(f"w={w} h={h} m={m}")
    #disp(m,"M")
    res=m.copy()
    for i in range(w):
        gnd=999
        gnd0=999
        #print(f"\ni={i}")
        for j in range(h):
            #print(f"i={i} j={j} gnd={gnd}")
            if m[j][i]=='.':
                #print("space")
                if j<gnd:
                    #print(f"set gnd to {j}")
                    gnd=j
            elif m[j][i]=='O':
                #print("block")
                if gnd<j:
                    #print(f"lower Block {j} to {gnd}")
                    res[gnd][i]='O'
                    #print(f"set {j} to space")
                    res[j][i]='.'
                    #print(f"set gnd to {j}")
                    gnd=gnd+1
            elif m[j][i]=='#':
                #print(f"Rock at {j} voids gnd")
                gnd=999
        #break
    #disp(res,"RES")
    return res
def transpL(m):
    res=deepcopy(m)
    #disp(m,"M")
    h=len(m)
    for j,r in enumerate(m):
        #print(f"j={j}")
        for i,c in enumerate(r):
            #print(f"i={i}")
            #print(f"Set {(h-i-1,j)} to {c}={m[j][i]}")
            res[h-i-1][j]=c
    #disp(res,"RES")
    return res
def transpR(m):
    res=deepcopy(m)
    #disp(m,"M")
    h=len(m)
    for j,r in enumerate(m):
        #print(f"j={j}")
        for i,c in enumerate(r):
            #print(f"i={i}")
            #print(f"Set {(h-i-1,j)} to {c}={m[j][i]}")
            res[i][h-j-1]=c
    #disp(res,"RES")
    return res
class T000(unittest.TestCase):
    def test_0201(self):
        self.assertEqual(parse(INP0202),transpL(parse(INP0201)))
    def test_0202(self):
        self.assertEqual(parse(INP0201),transpR(transpL(parse(INP0201))))
    def test_0101(self):
        self.assertEqual(RES01+0,compute(INP0101))
    def test_0102(self):
        self.assertEqual(RES01+0,compute(parse(INP0102),part=-1))
    def test_0103(self):
        self.assertEqual(INP0101,tiltN(parse(INP01)))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES02+1*1000,compute(parse(INP01),part=1))
    def test_0201(self):
        self.assertEqual(87,compute(parse(INP01),part=1,cycles= 1))
        self.assertEqual(69,compute(parse(INP01),part=1,cycles= 2))
        self.assertEqual(69,compute(parse(INP01),part=1,cycles= 3))
        self.assertEqual(69,compute(parse(INP01),part=1,cycles= 4))
        self.assertEqual(65,compute(parse(INP01),part=1,cycles= 5))
        self.assertEqual(64,compute(parse(INP01),part=1,cycles= 6))
        self.assertEqual(65,compute(parse(INP01),part=1,cycles= 7))
        self.assertEqual(63,compute(parse(INP01),part=1,cycles= 8))
        self.assertEqual(68,compute(parse(INP01),part=1,cycles= 9))
        self.assertEqual(69,compute(parse(INP01),part=1,cycles=10))
        self.assertEqual(69,compute(parse(INP01),part=1,cycles=11))

        self.assertEqual(64,compute(parse(INP01),part=1,cycles=20))
        self.assertEqual(65,compute(parse(INP01),part=1,cycles=21))
    def test_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
