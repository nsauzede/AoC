p=(17,15,15)
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
    def box(self)->tuple:
        INF=999999999
        x1,y1,z1=INF,INF,INF
        x2,y2,z2=-INF,-INF,-INF
        for x,y,z in self.m:
            if x<x1:x1=x
            if x>x2:x2=x
            if y<y1:y1=y
            if y>y2:y2=y
            if z<z1:z1=z
            if z>z2:z2=z
        return x1,y1,z1,x2,y2,z2
    def draw(self):
        x1,y1,z1,x2,y2,z2=self.box()
        inner=self.scanInner()
        for z in range(z1,z2+1):
            print(f"z={z}")
            print(f"{x1:<2} ",end='')
            for x in range(x1,x2+1):
                print(' 'if x%2!=0 else f"{x%10:1}",end='')
            print('')
            for y in range(y1,y2+1):
                print(f"{y:2} ",end='')
                for x in range(x1,x2+1):
                    c=\
                    'A'if(x,y,z)==(13,17,916)else\
                    'a'if(x,y,z)in((12,17,16),(13,16,16),(13,17,15),(13,17,17),(14,17,16))else\
                    'B'if(x,y,z)==(17,15,915)else\
                    'b'if(x,y,z)in((16,15,15),(17,14,15),(17,15,14),(17,15,16),(17,16,15))else\
                    'O'if(x,y,z)in self.m else'-'if(x,y,z)in inner else'.'
                    print(c,end='')
                print('')
    def scanX(self, outer:dict,inner:dict,x1,y1,z1,x2,y2,z2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    if(x,y,z)==p:aprint(f"PING SCANX")
                    if (x,y,z) not in self.m:
                        if x==x1 or y==y1 or z==z1\
                        or (x-1,y,z) in outer or (x+1,y,z) in outer\
                        or (x,y-1,z) in outer or (x,y+1,z) in outer\
                        or (x,y,z-1) in outer or (x,y,z+1) in outer:
                            if(x,y,z)==p:
                                aprint(f"PING SCANX OUTER")
                            inner.pop((x,y,z),None)
                            outer[(x,y,z)]=1
                            continue
                        if(x,y,z)==p:
                            aprint(f"PING SCANX INNER")
                        inner[(x,y,z)]=1
    def scanY(self, outer:dict,inner:dict,x1,y1,z1,x2,y2,z2):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                for x in range(x1,x2+1):
                    if(x,y,z)==p:aprint(f"PING SCANY")
                    if (x,y,z) not in self.m:
                        if x==x1 or y==y1 or z==z1\
                        or (x-1,y,z) in outer or (x+1,y,z) in outer\
                        or (x,y-1,z) in outer or (x,y+1,z) in outer\
                        or (x,y,z-1) in outer or (x,y,z+1) in outer:
                            if(x,y,z)==p:
                                aprint(f"PING SCANY OUTER")
                            inner.pop((x,y,z),None)
                            outer[(x,y,z)]=1
                            continue
                        if(x,y,z)==p:
                            aprint(f"PING SCANY INNER")
                        inner[(x,y,z)]=1
    def scanZ(self, outer:dict,inner:dict,x1,y1,z1,x2,y2,z2):
        for z in range(z1,z2+1):
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    if(x,y,z)==p:aprint(f"PING SCANZ")
                    if (x,y,z) not in self.m:
                        if x==x1 or y==y1 or z==z1\
                        or (x-1,y,z) in outer or (x+1,y,z) in outer\
                        or (x,y-1,z) in outer or (x,y+1,z) in outer\
                        or (x,y,z-1) in outer or (x,y,z+1) in outer:
                            if(x,y,z)==p:
                                aprint(f"PING SCANZ OUTER")
                            inner.pop((x,y,z),None)
                            outer[(x,y,z)]=1
                            continue
                        if(x,y,z)==p:
                            aprint(f"PING SCANZ INNER")
                        inner[(x,y,z)]=1
    def scanInner(self):
        x1,y1,z1,x2,y2,z2=self.box()
        print(x1,y1,z1,x2,y2,z2)
        outer={}
        inner={}
        self.scanZ(outer,inner,x1,y1,z1,x2,y2,z2)
        self.scanY(outer,inner,x1,y1,z1,x2,y2,z2)
        self.scanX(outer,inner,x1,y1,z1,x2,y2,z2)
        #do it a second time to back-propagate inners (FIXME??)
        self.scanZ(outer,inner,x1,y1,z1,x2,y2,z2)
        self.scanY(outer,inner,x1,y1,z1,x2,y2,z2)
        self.scanX(outer,inner,x1,y1,z1,x2,y2,z2)
        print(f"len(outer)={len(outer)}")
        print(f"len(inner)={len(inner)}")
        return inner
    def surface2(self):
        c=0
        inner=self.scanInner()
        sides=set()
        for x,y,z in self.m:
             if (x-1,y,z) not in self.m and (x-1,y,z) not in inner:c+=1;aprint(f"{(x-1,y,z)}=>{(x,y,z)}");sides.add(((x-1,y,z),(x,y,z)))
             if (x+1,y,z) not in self.m and (x+1,y,z) not in inner:c+=1;aprint(f"{(x+1,y,z)}=>{(x,y,z)}");sides.add(((x+1,y,z),(x,y,z)))
             if (x,y-1,z) not in self.m and (x,y-1,z) not in inner:c+=1;aprint(f"{(x,y-1,z)}=>{(x,y,z)}");sides.add(((x,y-1,z),(x,y,z)))
             if (x,y+1,z) not in self.m and (x,y+1,z) not in inner:c+=1;aprint(f"{(x,y+1,z)}=>{(x,y,z)}");sides.add(((x,y+1,z),(x,y,z)))
             if (x,y,z-1) not in self.m and (x,y,z-1) not in inner:c+=1;aprint(f"{(x,y,z-1)}=>{(x,y,z)}");sides.add(((x,y,z-1),(x,y,z)))
             if (x,y,z+1) not in self.m and (x,y,z+1) not in inner:c+=1;aprint(f"{(x,y,z+1)}=>{(x,y,z)}");sides.add(((x,y,z+1),(x,y,z)))
        print(f"c={c} len(sides)={len(sides)}")
        #for s in sorted(sides):print(s)
        return c
res00 = 10
res0 = 64
res1 = 4580
res0_2 = 58
res1_2 = 2610
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        g=Game()
        g.load(inp000)
        res=g.surface()
        self.assertEqual(res00,res)
    def test_000box(self):
        g=Game()
        g.load(inp000)
        self.assertEqual((1,1,1,2,1,1),g.box())
    def test_001box(self):
        g=Game()
        g.load(inp001)
        self.assertEqual((0,0,0,2,2,2),g.box())
        self.assertEqual(36,g.surface())
        g.draw()
    def test_001scan(self):
        g=Game()
        g.load(inp001)
        g.draw()
        self.assertEqual((0,0,0,2,2,2),g.box())
        self.assertEqual(surf001,g.surface())
        self.assertEqual(surf2001,g.surface2())
        self.assertEqual(inner001,len(g.scanInner()))
    def test_002scan(self):
        g=Game()
        g.load(inp002)
        g.draw()
        self.assertEqual((0,0,0,2,2,3),g.box())
        self.assertEqual(surf002,g.surface())
        self.assertEqual(surf2002,g.surface2())
        self.assertEqual(inner002,len(g.scanInner()))
    def test_003scan(self):
        g=Game()
        g.load(inp003)
        g.draw()
        self.assertEqual((0,0,0,4,4,4),g.box())
        self.assertEqual(surf003,g.surface())
        self.assertEqual(surf2003,g.surface2())
        self.assertEqual(inner003,len(g.scanInner()))
    def test_004scan(self):
        g=Game()
        g.load(inp004)
        g.draw()
        self.assertEqual(box004,g.box())
        print(surf004)
        self.assertEqual(surf004,g.surface())
        print(surf2004)
        self.assertEqual(surf2004,g.surface2())
        self.assertEqual(inner004,len(g.scanInner()))
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
        print(g.box())
        g.draw()
    def test_200(self):
        g=Game()
        g.load(parse(load("input0")))
        res=g.surface2()
        self.assertEqual(res0_2,res)
    def test_210(self):
        g=Game()
        g.load(parse(load("input1")))
        res=g.surface2()
        #g.draw()
        print(g.box())
        self.assertEqual(res1_2,res)
def parse(inp:str)->list:
    m=[]
    for l in inp.splitlines():
        if l=="":
            continue
        m+=[eval(l)]
    return m
def load(name):return open(name,"rt").read()
def aprint(s):pass
inp000=[[1,1,1],[2,1,1]]
surf001=36
surf2001=36-6
inner001=1
inp001=[
        [1,1,0],

        [0,1,1],
[1,0,1],        [1,2,1],
        [2,1,1],

        [1,1,2],
]
surf002=36
surf2002=36
inner002=0
inp002=[
[1,0,1],[1,2,1],
[0,1,1],[2,1,1],
[1,1,3],[1,1,0],
]
"""
.....
.###.
.###.
.###.
.....

.###.
#...#
#...#
#...#
.###.
"""
surf003=(9*2+12)*2+(12)*2+(8*2+8*2)*3
surf2003=(9*2+12)*2+(12)*2+(8*2+8*2)*3-(12*3+9*2)
inner003=9*3
inp003=[
        [1,1,0],[1,2,0],[1,3,0],
        [2,1,0],[2,2,0],[2,3,0],
        [3,1,0],[3,2,0],[3,3,0],

        [0,1,1],[0,2,1],[0,3,1],
[1,0,1],                        [1,4,1],
[2,0,1],                        [2,4,1],
[3,0,1],                        [3,4,1],
        [4,1,1],[4,2,1],[4,3,1],

        [0,1,2],[0,2,2],[0,3,2],
[1,0,2],                        [1,4,2],
[2,0,2],                        [2,4,2],
[3,0,2],                        [3,4,2],
        [4,1,2],[4,2,2],[4,3,2],

        [0,1,3],[0,2,3],[0,3,3],
[1,0,3],                        [1,4,3],
[2,0,3],                        [2,4,3],
[3,0,3],                        [3,4,3],
        [4,1,3],[4,2,3],[4,3,3],

        [1,1,4],[1,2,4],[1,3,4],
        [2,1,4],[2,2,4],[2,3,4],
        [3,1,4],[3,2,4],[3,3,4],
]
box004=(0,0,0,4,4,5)
surf004=(9*2+12)*2+(12)*2+(8*2+8*2)*3+6+2+4+6
surf2004=(9*2+12)*2+(12)*2+(8*2+8*2)*3-(12*3+9*2)+4
inner004=27-1-1+1
inp004=[
        [1,1,0],[1,2,0],[1,3,0],
        [2,1,0],[2,2,0],[2,3,0],
        [3,1,0],[3,2,0],[3,3,0],

        [0,1,1],[0,2,1],[0,3,1],
[1,0,1],                        [1,4,1],
[2,0,1],                        [2,4,1],
[3,0,1],                        [3,4,1],
        [4,1,1],[4,2,1],[4,3,1],

        [0,1,2],[0,2,2],[0,3,2],
[1,0,2],                        [1,4,2],
[2,0,2],        [2,2,2],        [2,4,2],
[3,0,2],                        [3,4,2],
        [4,1,2],[4,2,2],[4,3,2],

        [0,1,3],[0,2,3],[0,3,3],
[1,0,3],                        [1,4,3],
[2,0,3],        [2,2,3],        [2,4,3],
[3,0,3],                        [3,4,3],
        [4,1,3],[4,2,3],[4,3,3],

        [1,1,4],[1,2,4],[1,3,4],
        [2,1,4],[2,2,5],[2,3,4],
        [3,1,4],[3,2,4],[3,3,4],
]
