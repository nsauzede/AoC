def calc1(d:dict,g=0,g2=0)->(int,int,int):
    n=0
    for k,v in d.items():
        t=type(v)
        if t==dict:
            t,g,g2=calc1(v,g,g2)
            n+=t
        else:
            n+=v
    g+=n
    if n < 100000:
        g2+=n
    return n,g,g2

def calc2(d:dict,max=0,g=0,g2=99999999999999)->(int,int,int):
    n=0
    for k,v in d.items():
        t=type(v)
        if t==dict:
            t,g,g2=calc2(v,max,g,g2)
            n+=t
        else:
            n+=v
    g+=n
    if n >= max:
        if n < g2:
            g2 = n
    return n,g,g2

def addfile(d:dict,p:list,n:str,v:int):
    if p==[]:
        d[n]=v
    else:
        if p[0] not in d:
            d[p[0]]={}
        addfile(d[p[0]],p[1:],n,v)

def parse(inp:str)->dict:
    d={}
    i=0
    cwd=[]
    for l in inp.splitlines():
        if l.startswith('$ '):#cmd
            _,cmd=l.split('$ ')
            if cmd.startswith('cd '):#cd
                dir=cmd.split(' ')[1]
                if dir=="/":
                    cwd=[]
                elif dir=="..":
                    cwd=cwd[:-1]
                else:
                    cwd+=[dir]
        elif l.startswith('dir '):#dir
            _,rval=l.split('dir ')
            n=rval.split(" ")[0]
            if n not in d:
                d[n]={}
        else:#file
            s,n=l.split(" ")
            addfile(d,cwd,n,int(s))
    return d

def run1(inp:str)->int:
    p=parse(inp)
    c,g,g2=calc1(p)
    return g2

def run2(inp:str)->int:
    p=parse(inp)
    c=calc1(p)[0]
    max=70000000-c
    max=30000000-max
    c,g,g2=calc2(p,max)
    return g2

import unittest
def load(name):return open(name,"rt").read()
res0 = 95437
res1 = 1844187
res0_2 = 24933642
res1_2 = 4978279
class T1(unittest.TestCase):
    def test_00(self):
        n=1001
        self.assertEqual(n, calc1({'a':n})[0])
    def test_01(self):
        n=1002
        self.assertEqual(n, calc1({'/':{'a':n}})[0])
    def test_02(self):
        a=1003
        b=1004
        self.assertEqual(a+b, calc1({'/':{'a':a, 'b':b}})[0])
    def test_0(self):
        self.assertEqual(584+29116+2557, calc1({'/':{'a':{'e':{'i':584}},'f':29116,'g':2557}})[0])
    def test_1(self):
        self.assertEqual(0, calc1(parse(""))[0])
    def test_2(self):
        n=1005
        self.assertEqual(n, calc1(parse(f"$ cd /\n$ ls\n{n} a\n"))[0])
    def test_3(self):
        a=1005
        b=1006
        self.assertEqual(a+b, calc1(parse(f"$ cd /\n$ ls\n{a} a\n{b} b"))[0])
    def test_4(self):
        a=1005
        b=1006
        self.assertEqual(a+b, calc1(parse(f"$ cd /\n$ ls\n{a} a\ndir e\n$ cd e\n$ ls\n{b} b\n"))[0])
    def test_add(self):
        d={}
        addfile(d,["a","b"], "c", 123)
        self.assertEqual({'a':{'b':{'c':123}}},d)
    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inpReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
class T2(unittest.TestCase):
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
