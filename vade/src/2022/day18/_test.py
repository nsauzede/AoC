def load(name):return open(name,"rt").read()
class Game:
    def __init__(self):
        self.m={}
    def load(self,l:list):
        for e in l:
            self.m[tuple(e)]=1
    def surface(self):
        c=0
        for x,y,z in self.m:
            if (x-1,y,z) not in self.m:c+=1
            if (x+1,y,z) not in self.m:c+=1
            if (x,y-1,z) not in self.m:c+=1
            if (x,y+1,z) not in self.m:c+=1
            if (x,y,z-1) not in self.m:c+=1
            if (x,y,z+1) not in self.m:c+=1
        return c
res00 = 10
res0 = 64
res1 = 4580
res0_2 = 58
res1_2 = 0
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        g=Game()
        g.load(inp000)
        res=g.surface()
        self.assertEqual(res00,res)
    def test_100(self):
        g=Game()
        g.load(parse(load("input0")))
        res=g.surface()
        self.assertEqual(res0,res)
    def test_110(self):
        g=Game()
        g.load(parse(load("input1")))
        res=g.surface()
        self.assertEqual(res1,res)

def parse(inp:str)->list:
    m=[]
    for l in inp.splitlines():
        if l=="":
            continue
        m+=[eval(l)]
    return m

inp000=[[1,1,1],[2,1,1]]
