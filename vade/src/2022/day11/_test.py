def mkmonkey()->list:
    return[
{'inspected':0, 'worry':[79, 98], 'operation':"new = old * 19", 'divisible':23, True:2, False:3},
{'inspected':0, 'worry':[54, 65, 75, 74], 'operation':"new = old + 6", 'divisible':19, True:2, False:0},
{'inspected':0, 'worry':[79, 60, 97], 'operation':"new = old * old", 'divisible':13, True:1, False:3},
{'inspected':0, 'worry':[74], 'operation':"new = old + 3", 'divisible':17, True:0, False:1},
]

def oneround(m:list, divworry=True, muldivs=1):
    for n in range(len(m)):
        monkey=m[n]
        #print(f"Monkey {n}:")
        rem=[]
        for w in range(len(monkey['worry'])):
            worry = monkey['worry'][w]
            #print(f"  Monkey inspects an item with a worry level of {monkey['worry'][w]}")
            monkey['inspected']+=1
            op = monkey['operation']
            opoldtimesold = "new = old * old"
            opoldtimes = "new = old * "
            opoldplus = "new = old + "
            if op.startswith(opoldtimesold):
                worry*=worry
                #print(f"    Worry level is multiplied by itself to {worry}.")
            elif op.startswith(opoldtimes):
                val=int(op.split(opoldtimes)[1])
                worry*=val
                #print(f"    Worry level is multiplied by {val} to {worry}.")
            elif op.startswith(opoldplus):
                val=int(op.split(opoldplus)[1])
                worry+=val
                #print(f"    Worry level increases by {val} to {worry}.")
            else:
                raise Exception(f"Unknown operation '{op}'")
            if divworry: worry//=3
            else:
                worry%=muldivs
            monkey['worry'][w] = worry
            #print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry}.")
            div=monkey['divisible']
            #print(f"Checking if worry={worry} is divisible by {div}...")
            isdiv=worry%div==0
            nex = monkey[isdiv]
            res = "" if isdiv else "not "
            #print(f"    Current worry level is {res}divisible by {div}.")
            #print(f"    Item with worry level {worry} is thrown to monkey {nex}.")
            m[nex]['worry'].append(worry)
            rem+=[w]
        rem.sort(reverse=True)
        for r in rem:
            #print(f"worry={m[n]['worry']}")
            #print(f"removing {r}")
            del m[n]['worry'][r]
    n=0
    for e in m:
        #print(f"Monkey {n}: {e['worry']}")
        n+=1

def calc(m:list, n=20, divworry=True)->int:
    r=[1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    muldivs=1
    if not divworry: # Chinese Remainder Theorem
        for e in m:
            muldivs*=e['divisible']
    for i in range(1,n+1):
        #print(f"round {i}")
        oneround(m, divworry, muldivs)
        if i in r:
            print(f"== After round {i} ==")
            for j in range(len(m)):
                print(f"Monkey {j} inspected items {m[j]['inspected']} times.")
                pass
    l=[]
    for e in m:
        l+=[e['inspected']]
    l.sort(reverse=True)
    return l[0]*l[1]

def run1(inp:str, n=20, divworry=True)->int:
    m=parse(inp)
    #m=mkmonkey()
    c=calc(m,n,divworry)
    return c

def run2(inp:str)->int:
    return run1(inp, 10000, False)

def parse(inp:str)->list:
    m=[]
    l=inp.splitlines()
    i = 0
    while i < len(l):
        #print(f"i={i} l={l[i]}")
        d={}
        n=l[i].split("Monkey ")[1]
        #print(f"parsing monkey {n}")
        i+=1
        d['inspected']=0
        worry = l[i].split("  Starting items: ")[1]
        d['worry'] = [int(x.split(",")[0]) for x in worry.split()]
        #print(f" worry={worry}")
        i+=1
        op= l[i].split("  Operation: ")[1]
        d['operation']=op
        i+=1
        div= int(l[i].split("  Test: divisible by ")[1])
        d['divisible']=div
        i+=1
        tr= int(l[i].split("    If true: throw to monkey ")[1])
        d[True]=tr
        i+=1
        v= int(l[i].split("    If false: throw to monkey ")[1])
        d[False]=v
        i+=1
        i+=1
        #print(f" monkey={d}")
        m+=[d]
    return m

import unittest
def load(name):return open(name,"rt").read()
res0 = 10605
res1 = 66124
res0_2 = 2713310158
res1_2 = 19309892877
class T1(unittest.TestCase):
#class T1():
    def test_10(self):
        m=mkmonkey()
        self.assertEqual(res0, calc(m))
    def test_50(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_60(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_70(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_80(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
