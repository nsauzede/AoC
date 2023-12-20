import unittest
INP011=r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
OUT011={
'broadcaster': ['', 0,['a', 'b', 'c']],
'a': ['%',0,['b']],
'b': ['%',0,['c']],
'c': ['%',0,['inv']],
'inv': ['&',{'c':0},['a']],
}
RES011=32000000
INP012=r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""
OUT012={
'broadcaster': ['', 0, ['a']],
'a': ['%',0,['inv','con']],
'inv': ['&',{'a':0},['b']],
'b': ['%',0,['con']],
'con': ['&',{'a':0,'b':0},['output']],
}
RES012=11687500
#RES1=288               # too lot
RES1=819397964
RES02=0
RES2=0
def compute(d0:dict,n=1000,part=0)->int:
    #print(f"d0={d0}")
    d=d0.copy()
    res=0
    ons=0
    offs=0
    for i in range(n):
        l,r=compute0(d,part)
        ons+=l
        offs+=r
    return ons*offs
def compute0(d:dict,part=0)->(int,int):
    tosend=[['button',0,['broadcaster']]]
    #print(f"d={d}")
    ons=0
    offs=0
    while tosend:
        #print(f"tosend={tosend}")
        fro,sig,tos=tosend.pop(0)
        #print(f"fro={fro} sig={sig} tos={tos}")
        cont=False
        for to in tos:
            #print(f"{fro} -{'high'if sig else'low'}-> {to}       ons={ons} offs={offs} sig={sig}")
            #print(f"{fro} -{'high'if sig else'low'}-> {to}")
            if sig:ons+=1
            else:offs+=1
            if to=='output' or to not in d:
                #print("OUTPUT={output}                  ***")
                continue
            t,s,dests=d[to]
            #print(f"fro={fro} sig={sig} to={to}: t={t} s={s} dests={dests}")
            if t=='%':
                if sig==1:
                    continue
                s=1-s
                d[to][1]=s
                for dest in dests:
                    cont=True
                    #print(f"ADDING% tosend {to} {s} {dest}")
                    tosend+=[[to,s,[dest]]]
            elif t=='&':
                d[to][1][fro]=sig
                #print(f"d[to][1]={d[to][1]}")
                s=0
                if fro not in d[to][1]:0/0
                for k,v in d[to][1].items():
                    #print(f"k={k} v={v} ")
                    if v==0:
                        s=1
                        break
                for dest in dests:
                    cont=True
                    #print(f"ADDING& tosend {to} {s} {dest}")
                    tosend+=[[to,s,[dest]]]
            else:
                for dest in dests:
                    cont=True
                    #print(f"ADDING tosend {to} {sig} {dest}")
                    tosend+=[[to,sig,[dest]]]
        #if not cont:break
    #print(f"final d={d}")
    return ons,offs
def compute20(d:dict,part=0)->(int,int):
    tosend=[['button',0,['broadcaster']]]
    #print(f"d={d}")
    ons=0
    offs=0
    while tosend:
        #print(f"tosend={tosend}")
        fro,sig,tos=tosend.pop(0)
        #print(f"fro={fro} sig={sig} tos={tos}")
        cont=False
        for to in tos:
            #print(f"{fro} -{'high'if sig else'low'}-> {to}       ons={ons} offs={offs} sig={sig}")
            #print(f"{fro} -{'high'if sig else'low'}-> {to}")
            if to=='rx':
                if sig==0:
                    ons+=1
                    0/0
                else:
                    offs+=1
                #print("OUTPUT={output}                  ***")
                continue
            t,s,dests=d[to]
            #print(f"fro={fro} sig={sig} to={to}: t={t} s={s} dests={dests}")
            if t=='%':
                if sig==1:
                    continue
                s=1-s
                d[to][1]=s
                for dest in dests:
                    cont=True
                    #print(f"ADDING% tosend {to} {s} {dest}")
                    tosend+=[[to,s,[dest]]]
            elif t=='&':
                d[to][1][fro]=sig
                #print(f"d[to][1]={d[to][1]}")
                s=0
                if fro not in d[to][1]:0/0
                for k,v in d[to][1].items():
                    #print(f"k={k} v={v} ")
                    if v==0:
                        s=1
                        break
                for dest in dests:
                    cont=True
                    #print(f"ADDING& tosend {to} {s} {dest}")
                    tosend+=[[to,s,[dest]]]
            else:
                for dest in dests:
                    cont=True
                    #print(f"ADDING tosend {to} {sig} {dest}")
                    tosend+=[[to,sig,[dest]]]
        #if not cont:break
    #print(f"final d={d}")
    return ons,offs
def compute2(d0:dict,start=0,n=1000,part=0)->int:
    #print(f"d0={d0}")
    d=d0.copy()
    for res in range(start,start+n):
        ons,offs=compute20(d,part)
        if ons==0 and offs==1:
            print(f"Found 1 RX Low for res={res}")
            break
        print(f"res={res} ons={ons} offs={offs} {res/n*100.:.02}%")
    if res>=n-1:
        print(f"Not found in n={1000}")
        res=0
    return res
def calc(wfs:dict,x,m,a,s)->int:
    res = 0
    #print(f"x={x} m={m} a={a} s={s}")
    k='in'
    while True:
        break
    return res
def parse(inp:str,part=0)->dict:
    res={}
    conjs=[]
    for s in inp.splitlines():
        s=s.replace(" ","")
        k,v=s.split("->")
        t=k[0]
        s=0
        if t=='%':
            k=k[1:]
        elif t=='&':
            k=k[1:]
            s={}
            conjs+=[k]
        else:
            t=''
        res[k]=[t,s,v.split(",")]
    for conj in conjs:
        for k in res:
            if conj in res[k][2]:
                res[conj][1][k]=0
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
        res=parse(INP011)
        #print(f"res={res}")
        #print(f"OUT={OUT011}")
        self.assertEqual(OUT011,res)
    def test_0120(self):
        res=parse(INP012)
        #print(f"res={res}")
        #print(f"OUT={OUT012}")
        self.assertEqual(OUT012,res)
    def test_0111(self):
        self.assertEqual(RES011+0,compute(parse(INP011),n=1000))
    def test_0120(self):
        self.assertEqual(RES012+0,compute(parse(INP012),n=1000))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_2000(self):
        """
res=2772531 ons=0 offs=5 0.00028%
res=2772532 ons=0 offs=7 0.00028%
res=2772533 ons=0 offs=6 0.00028%
res=2772534 ons=0 offs=8 0.00028%
res=2772535 ons=0 offs=5 0.00028%
res=2772536 ons=0 offs=9 0.00028%
        """
        #start=0
        #n=1000000000000
        start=2772531
        n=4
        self.assertEqual(RES2+0*1000,compute2(parse(open("input1","rt").read()),start=start,n=n,part=1))
