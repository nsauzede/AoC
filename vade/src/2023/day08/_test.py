import unittest
INP01="""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
RES01=2
INP01_="""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
RES01_=6
RES1=21251
INP02="""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
RES02=6
RES2=11678319315857
def compute(inp:dict,part=0)->int:
    if part==0:return compute0(inp,part)
    else:return compute1(inp,part)
def compute1(inp:dict,part=0)->int:
    res = 0
    steps=inp['steps']
    print(f"steps={steps}")
    nxts=[s for s in inp.keys() if s.endswith('A')]
    ii=[]
    # find the LCM between all A=>Z paths cycle lengths
    for nxt in nxts:
        i = 0
        while not nxt.endswith('Z'):
            c=steps[i%len(steps)]
            l,r=inp[nxt]
            #print(f"i={i} nxt={nxt} l={l} r={r}")
            if c=='L':
                nxt=l
            else:
                nxt=r
            i+=1
        ii+=[i]
    from math import lcm
    res=lcm(*ii)
    return res
def compute0(inp:dict,part=0)->int:
    res = 0
    steps=inp['steps']
    print(f"steps={steps}")
    nxt='AAA'
    i = 0
    while nxt != 'ZZZ':
        c=steps[i%len(steps)]
        l,r=inp[nxt]
        print(f"i={i} nxt={nxt} l={l} r={r}")
        if c=='L':
            nxt=l
        else:
            nxt=r
        i+=1
    res=i
    return res
def parse(inp):
    res={}
    inp=inp.replace(' ','')
    inp=inp.replace('(','')
    inp=inp.replace(')','')
    ll=inp.splitlines()
    res['steps']=ll[0]
    for i in range(2,len(ll)):
        l,r=ll[i].split('=')
        nxt=l
        res[nxt]=r.split(",")
    #print(f"res={res}")
    return res
class T000(unittest.TestCase):
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_0100_(self):
        self.assertEqual(RES01_+0,compute(parse(INP01_)))
    def test_1000(self):
        self.assertEqual(RES1,compute(parse(open("input1","rt").read())))
    def test_0200(self):
        self.assertEqual(RES02+0,compute(parse(INP02),1))
    def test_2000(self):
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read()),1))
