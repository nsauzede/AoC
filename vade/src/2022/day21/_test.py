import copy
def load(name):return open(name,"rt").read()
def parse(name):
    f=open(name,"rt")
    var={}
    ops={}
    for line in f.readlines():
        #print(f"line={line}")
        if line=="":continue
        l,r=line.strip().split(": ")
        if " " in r:
            ops[l]=r.split(" ")
            if ops[l][1]=='/':ops[l][1]='//'
        else:
            var[l]=int(r)
    return var,ops
def apply(var:dict,ops:dict):
    N=len(var)+len(ops)
    while len(var)<N:
        ops0=copy.deepcopy(ops)
        for n,opl in ops0.items():
            l,op,r=opl
            aprint(f"testing {n} : {l} and {r}..")
            if l in var:
                aprint(f"VAR {l} HAS VALUE {var[l]}")
                l=var[l]
            if r in var:
                aprint(f"VAR {r} HAS VALUE {var[r]}")
                r=var[r]
            if str(l).isnumeric() and str(r).isnumeric():
                aprint(f"EVAL'ING {n}={l}{op}{r}")
                var[n]=eval(f"{l}{op}{r}")
                del ops[n]
            else:
                aprint(f"KEEPING {n}={l}{op}{r}")
                ops[n]=[l,op,r]
def apply2(var:dict,ops:dict):
    N=len(var)+len(ops)
    del var['humn']
    n=len(ops)
    n0=n-1
    while len(ops)!=n0:
        n0=len(ops)
        ops0=copy.deepcopy(ops)
        for n,opl in ops0.items():
            if n=="humn":continue
            l,op,r=opl
            aprint(f"testing {n} : {l} and {r}..")
            if l in var:
                aprint(f"VAR {l} HAS VALUE {var[l]}")
                l=var[l]
            if r in var:
                aprint(f"VAR {r} HAS VALUE {var[r]}")
                r=var[r]
            if str(l).isnumeric() and str(r).isnumeric():
                aprint(f"EVAL'ING {n}={l}{op}{r}")
                var[n]=eval(f"{l}{op}{r}")
                del ops[n]
            else:
                aprint(f"KEEPING {n}={l}{op}{r}")
                ops[n]=[l,op,r]
        aprint(f"ops={ops}")
    print(f"len(ops)={len(ops)}")
    var2={}
    ops2={}
    l,_,r=ops['root']
    if str(l).isnumeric():var2[r]=int(l)
    else:var2[l]=int(r)
    del ops['root']
    #print(f"ops={ops}")
    print(f"var2={var2}")
    for k,opl in ops.items():
        l,op,r=opl
        if str(l).isnumeric():n=r;v=l
        else:n=l;v=r
        op = '-' if op=='+' else '+' if op=='-' else '*' if op=='//' else '//'
        ops2[n]=[k,op,v]
    print(f"ops2={ops2}")
    apply(var2,ops2)
    print(var2['humn'])
    return var2,ops2

verbose=False
def aprint(s:str):
    if verbose:
        print(s)

class Game:
    def __init__(self):
        self.m={}
        self.air={}

inp00=[1,2,-3,3,-2,0,4,]

res0 = 152
res1 = 145167969204648
res0_2 = 301
res1_2 = 0

# res2 7560831729513 is too high

import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_100(self):
        g=Game()
        v,o=parse("input0")
        self.assertEqual(8,len(v))
        self.assertEqual(7,len(o))
        print(f"v={v} o={o} r={len(o)}")
        apply(v,o);r=v['root']
        print(f"v={v} o={o} r={r}")
        self.assertEqual(res0,r)
    def test_110(self):
        g=Game()
        v,o=parse("input1")
        #print(f"v={v} o={o} r={len(o)}")
        apply(v,o);r=v['root']
        print(f"v={v} o={o} r={r}")
        self.assertEqual(res1,r)
    def test_200(self):
        g=Game()
        v,o=parse("input0")
        self.assertEqual(8,len(v))
        self.assertEqual(7,len(o))
        print(f"v={v} o={o} r={len(o)}")
        v,o=apply2(v,o);r=v['humn']
        print(f"v={v} o={o} r={r}")
        self.assertEqual(res0_2,r)
    def Ztest_210(self):
        g=Game()
        v,o=parse("input1")
        #print(f"v={v} o={o} r={len(o)}")
        v,o=apply2(v,o);r=v['humn']
        print(f"v={v} o={o} r={r}")
        self.assertEqual(res1_2,r)
