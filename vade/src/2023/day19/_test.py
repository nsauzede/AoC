import unittest
INP01=r"""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
WF011={
'px':['a<2006:qkq','m>2090:A','rfg'],
'pv':['a>1716:R','A'],
'lnx':['m>1548:A','A'],
'rfg':['s<537:gd','x>2440:R','A'],
'qs':['s>3448:A','lnx'],
'qkq':['x<1416:A','crn'],
'crn':['x>2662:A','R'],
'in':['s<1351:px','qqz'],
'qqz':['s>2770:qs','m<1801:hdj','R'],
'gd':['a>3333:R','R'],
'hdj':['m>838:A','pv'],
}
RTS011=[
[787,2655,1222,2876],
[1679,44,2067,496],
[2036,264,79,2244],
[2461,1339,466,291],
[2127,1623,2188,1013],
]
RES01=19114
RES1=395382
RES02=0
RES2=0
def compute(d:dict,part=0)->int:
    res=0
    #print(f"d={d}")
    wfs=d['wfs']
    rts=d['rts']
    for rt in rts:
        #print(f"rt={rt}")
        x,m,a,s=rt
        res0=calc(wfs,x,m,a,s)
        res+=res0
    return res
def calc(wfs:dict,x,m,a,s)->int:
    res = 0
    #print(f"x={x} m={m} a={a} s={s}")
    k='in'
    approved=False
    while True:
        #print(f"k={k}")
        if k=='A':
            approved=True
            break
        elif k=='R':
            approved=False
            break
        l=wfs[k]
        for stmt in l:
            #print(f"stmt={stmt}")
            if ':'in stmt:
                expr,k0=stmt.split(':')
                if eval(expr):
                    k=k0
                    break
            else:
                k=stmt
                break
    if approved:
        res=x+m+a+s
    return res
def parse(inp:str,part=0)->dict:
    res={
    'wfs':{},
    'rts':[],
    }
    wf=True
    for s in inp.splitlines():
        if wf:
            if s=="":
                wf=False
                continue
            s=s.replace("}","")
            k,r=s.split("{")
            stmts=r.split(",")
            res['wfs'][k]=stmts
        else:
            s=s.replace("{x=","")
            s=s.replace("m=","")
            s=s.replace("a=","")
            s=s.replace("s=","")
            s=s.replace("}","")
            res['rts']+=[[int(e)for e in s.split(",")]]
    return res
def disp(d:dict,text="DISP"):
    print(f"\n{text} ==============")
    h=len(m)
    w=len(m[0])
    for j,r in enumerate(m):
        for i,c in enumerate(r):
            print(c,end='')
        print()
class T000(unittest.TestCase):
    def test_0110(self):
        res=parse(INP01)
        wfs=res['wfs']
        rts=res['rts']
        self.assertEqual((WF011,RTS011),(wfs,rts))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES02+0*1000,compute(parse(INP01),part=1))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
