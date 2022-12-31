import unittest
verbose=False
def aprint(s:str,end='\n'):
    if verbose:print(s,end=end)
#verbose=True
S='S';B='B';H='#'
# sensor, beacon; returns manhattan distance between them
def manhattan(s:tuple, b:tuple)->int:
    n=0
    y1,y2=s[1],b[1]
    if y1!=y2:
        delta=y2-y1
        step=delta//abs(delta)
        for y in range(y1,y2,step):
            n+=1
    x1,x2=s[0],b[0]
    if x1!=x2:
        delta=x2-x1
        step=delta//abs(delta)
        for x in range(x1,x2,step):
            n+=1
    return n
def box(d:dict)->tuple:
    INF=999999999
    x1=INF;y1=INF
    x2=-INF;y2=-INF
    for e in d:
        x,y=e
        if x<x1:x1=x
        if x>x2:x2=x
        if y<y1:y1=y
        if y>y2:y2=y
    return x1,y1,x2,y2
def rawmap(ls:list)->dict:
    m={}
    for e in ls:m[e[0]]=S;m[e[1]]=B
    return m
def flood(m:dict, s:tuple, b:tuple, y0=None, yy={}):
    n=manhattan(s,b)
    aprint(f"s={s} b={b} n={n}")
    if y0!=None:
        r=[y0]
    else:
        r=range(s[1]-n,s[1]+n+1)
    for y in r:
        d=n-abs(s[1]-y)
        aprint(f"y={y}:n-y={d}  ", end='')
        for x in range(s[0]-d,s[0]+d+1):
            if (x,y) in m:continue
            c='#'
            if (x,y)==s:c=S
            elif (x,y)==b:c=B
            m[(x,y)]=c
            aprint(f" x={x} {c}", end='')
            if y0!=None:
                if c=='#':
                    yy[x]=c
        aprint('')
#@unittest.skip
class T0Merge(unittest.TestCase):
    def test_merge0(self):
        m={}
        merge(m,-2,[8,8])
        self.assertEqual({-2:{8:8}},m)
    def test_merge1(self):
        m={}
        merge(m,-2,[-6,10])
        self.assertEqual({-2:{-6:10}},m)
        merge(m,-2,[8,8])
        self.assertEqual({-2:{-6:10}},m)
    def test_merge2(self):
        m={}
        merge(m,-2,[8,8])
        self.assertEqual({-2:{8:8}},m)
        merge(m,-2,[-6,10])
        self.assertEqual({-2:{-6:10}},m)
    def test_merge3(self):
        m={}
        merge(m,-2,[8,8])
        self.assertEqual({-2:{8:8}},m)
        merge(m,-2,[-6,10])
        self.assertEqual({-2:{-6:10}},m)
        merge(m,-2,[16,24])
        self.assertEqual({-2:{-6:10, 16:24}},m)
    def test_merge4(self):
        m={}
        global verbose;verbose=True
        merge(m,0,[12,14])
        self.assertEqual({0:{12:14}},m)
        merge(m,0,[-8,12])
        self.assertEqual({0:{-8:14}},m)
        verbose=False
    def test_merge5(self):
        m={}
        global verbose;verbose=True
        merge(m,0,[-8,14])
        self.assertEqual({0:{-8:14}},m)
        merge(m,0,[14,26])
        self.assertEqual({0:{-8:26}},m)
        verbose=False
# 0  -8,14 14,26
    def test_merge6(self):
        m={}
        global verbose;verbose=True
        merge(m,8,[0,16])
        self.assertEqual({8:{0:16}},m)
        merge(m,8,[0,4])
        self.assertEqual({8:{0:16}},m)
        merge(m,8,[0,0])
        self.assertEqual({8:{0:16}},m)
        merge(m,8,[18,22])
        self.assertEqual({8:{0:16, 18:22}},m)
        merge(m,8,[12,20])
        self.assertEqual({8:{0:22}},m)
        merge(m,8,[20,20])
        self.assertEqual({8:{0:22}},m)
        verbose=False
# 8  0,22
def merge(m:dict,y:int,xrng:tuple):
    x1,x2=xrng
    if y not in m:m[y]={}
    found=False
    todel=[]
    toadd={x1:x2}
    if y==8:aprint(f"{y} Merge {x1,x2} ?")
    for k,v in m[y].items():
        if y==8:aprint(f"{y} Testing {x1,x2} with {k,v}..")
        if x1>=k and x2<=v:
            if y==8:aprint(f"{y} will skip {x1,x2} included in {k,v}.")
            toadd.pop(x1,None)
            continue
        if k>=x1 and v<=x2:
            if y==8:aprint(f"{y} will remove {k,v} included in {x1,x2}.")
            todel+=[k]
            continue
        #-8,12  12,14
        #14,26  -8,14
        if x1<k and x2>=k-1:
            if x2>v:
                v2=x2
            else:
                v2=v
            todel+=[k]
            if y==8:aprint(f"{y} will remove {k,v}, merged left into new merged {x1,v2}.")
            toadd.pop(x1,None)
            toadd[x1]=v2
        if x1>=k and x1<=v+1:
            if v<x2:
                todel+=[k]
                if y==8:aprint(f"{y} will remove {k,v}, merged right into new merged {k,x2}.")
                toadd.pop(x1,None)
                toadd[k]=x2
                x1=k
    for k in todel:
        v=m[y].pop(k)
        if y==8:aprint(f"{y} Removing {k,v}")
    for k,v in toadd.items():
        if y==8:aprint(f"{y} Adding {k,v}")
        m[y][k]=v
    return m
def flood2(m:dict, s:tuple, b:tuple, box:tuple):
    n=manhattan(s,b)
    r=range(s[1]-n,s[1]+n+1)
    for y in r:
        d=n-abs(s[1]-y)
        x1,x2=s[0]-d,s[0]+d
        merge(m,y,(x1,x2))
def draw(m:dict):
    print('')
    x1,y1,x2,y2=box(m)
    print(f"{'':2} ",end='')
    for x in range(x1,x2+1):
        if x%2 == 0:
            print(f"{x%10}",end='')
        else:
            print(" ",end='')
    print('')
    for y in range(y1,y2+1):
        print(f"{y:2} ",end='')
        for x in range(x1,x2+1):
            c='.'
            if (x,y) in m:c=m[(x,y)]
            print(c,end='')
        print('')
def cnt(m:dict,y:int)->int:
    x1,y1,x2,y2=box(m)
    c=0
    for x in range(x1,x2+1):
        if (x,y) in m:
            if m[(x,y)]==H:c+=1
    return c
def scan(ls:list, y:int)->int:
    m=rawmap(ls)
    yy={}
    for e in ls:
        flood(m,e[0],e[1],y,yy)
    c=len(yy)
    return c
def draw2_new(m:dict,box:tuple):
    xmax,ymax=box
    for y,xranges in sorted(m.items()):
        if y<0 or y>ymax:continue
        if len(xranges)!=2:continue
        a,b=list(xranges.items())
        if abs(a[1]-b[0])==2:
            n=(a[1]+b[0])//2
        else:
            n=(a[0]+b[1])//2
        print(f"n={n}")
        return n
        print(f"{y:2} ",end='')
        for x1,x2 in xranges.items():
            print(f" {x1},{x2}",end='')
        print('')
def draw2(m:dict,box:tuple):
    xmax,ymax=box
    for y,xranges in sorted(m.items()):
        if y<0 or y>ymax:continue
        #if len(xranges)!=2:continue
        print(f"{y:2} ",end='')
        for x1,x2 in xranges.items():
            print(f" {x1},{x2}",end='')
        print('')
def locate(ls:list, box:tuple)->int:
    m={}
    print("FLOOD2   !!!!!!!!!!!!!!!!!!!")
    for e in ls:
        flood2(m,e[0],e[1], box)
    #draw2(m,box)
    xmax,ymax=box
    xx=0;yy=0
    for y,xranges0 in sorted(m.items()):
        if y<0 or y>ymax:continue
        xranges=crop(xranges0, 0, xmax)
        print(f"y={y} xranges0={xranges0} xranges={xranges}")
        if len(xranges)!=2:continue
        a,b=list(xranges.items())
        if abs(a[1]-b[0])==2:
            xx=(a[1]+b[0])//2
        else:
            xx=(a[0]+b[1])//2
        yy=y
        print(f"x,y={xx,yy} xranges0={xranges0} xranges={xranges}")
        break
    n=4000000*xx+yy
    print(f"Returning {n} for {xx,yy}")
    return n
#11  -3,13 15,25
def crop(m0:dict,xmin:int,xmax:int)->dict:
    m={}
    for k,v in m0.items():
        if k>=xmin:
            if k<=xmax:
                if v<=xmax:
                    m[k]=v
                else:
                    m[k]=xmax
        elif v>=xmin:
            if v<=xmax:
                m[xmin]=v
            else:
                m[xmin]=xmax
    return m
def flood3(m:dict, s:tuple, b:tuple, xy:tuple)->dict:
    n=manhattan(s,b)
    y1,y2=s[1]-n,s[1]+n+1
    xmax,ymax=xy
    if y2>=0 and y1<=ymax:
        yr=range(y1,y2)
        for y in yr:
            if y<0 or y>ymax:
                continue
            d=n-abs(s[1]-y)
            x1,x2=s[0]-d,s[0]+d
            if x2<0 or x1>xmax:
                continue
            merge(m,y,(x1,x2))
    return m
def scan3(ls:list, xy:tuple)->(dict,int):
    m={}
    for s,b in ls:
        flood3(m,s,b,xy)
    #print(f"len(m)={len(m)} m={m}")
    print(f"len(m)={len(m)}")
    xx,yy=0,0
    for k,v in m.items():
        if len(v)!=1:
            print(f"{k}: {v}")
            yy=k
            a,b=list(v.items())[:2]
            if abs(a[1]-b[0])==2:
                xx=(a[1]+b[0])//2
            else:
                xx=(a[0]+b[1])//2
            break
    n=4000000*xx+yy
    print(f"Returning {n} for {xx,yy}")
    return m,n
res0 = 26
res1 = 4560025
res0_2 = 56000011
res1_2 = 12480406634249
# res1_2=5034470 is too low
# res1_2=4690952501132 is too low
#@unittest.skip
class T0locate(unittest.TestCase):
    def test_scan3(self):
        ls=parse(load("input0"))
        m,f=scan3(ls,(20,20))
        #draw2(m,(20,20))
        self.assertEqual(res0_2,f)
    def test_scan3_1(self):
        ls=parse(load("input1"))
        m,f=scan3(ls,(4000000,4000000))
        #draw2(m,(20,20))
        self.assertEqual(res1_2,f)
    def test_locate0(self):
        ls=parse(load("input0"))
        global verbose;verbose=True
        print("BEGIN LOCATE")
        f=locate(ls, (20,20))
        print("END LOCATE")
        verbose=False
        self.assertEqual(res0_2,f)
    def test_crop0(self):
        self.assertEqual({0:13,15:20},crop({-3:13, 15:25}, 0, 20))
    def test_crop1(self):
        self.assertEqual({0:4000000},crop({-1238897: 4670234}, 0, 4000000))
    def Ztest_locate1(self):
        ls=parse(load("input1"))
        #global verbose;verbose=True
        aprint("BEGIN LOCATE")
        f=locate(ls, (4000000,4000000))
        aprint("END LOCATE")
        verbose=False
        self.assertEqual(res1_2,f)
"""
8 Merge (0, 16) ?
8 Adding (0, 16)
8 Merge (0, 4) ?
8 Testing (0, 4) with (0, 16)..
8 will skip (0, 4) included in (0, 16).
8 Merge (0, 0) ?
8 Testing (0, 0) with (0, 16)..
8 will skip (0, 0) included in (0, 16).
8 Merge (18, 22) ?
8 Testing (18, 22) with (0, 16)..
8 Adding (18, 22)
8 Merge (12, 20) ?
8 Testing (12, 20) with (0, 16)..
8 will remove (0, 16), merged right into new merged (0, 20).
8 Testing (12, 20) with (18, 22)..
8 will remove (18, 22), merged left into new merged (12, 22).
8 Removing (0, 16)
8 Removing (18, 22)
8 Adding (0, 20)
8 Adding (12, 22)
8 Merge (20, 20) ?
8 Testing (20, 20) with (0, 20)..
8 will skip (20, 20) included in (0, 20).
8 Testing (20, 20) with (12, 22)..
8 will skip (20, 20) included in (12, 22).
"""
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(ls00,parse(inp00))
    def test_001(self):
        self.assertEqual(ls00,parse(load("input0")))
#@unittest.skip
class T010(unittest.TestCase):
    def test_manhattan(self):
        s=(8,7)
        b=(2,10)
        n=manhattan(s,b)
        self.assertEqual(9,n)
    def test_rawmap(self):
        ls=parse(load("input0"))
        m=rawmap(ls)
        #draw(m)
        self.assertEqual(map00,m)
    def test_box(self):
        ls=parse(load("input0"))
        m=rawmap(ls)
        b=box(m)
        self.assertEqual((-2,0,25,22),b)
    def test_flood(self):
        f={}
        flood(f, (2,0),(0,0))
        #draw(f)
        self.assertEqual(flood00,f)
        self.assertEqual(3,cnt(f,0))
    def test_flood2(self):
        f={}
        flood(f, (8,7),(2,10))
        #draw(f)
        #self.assertEqual(flood00,f)
        self.assertEqual(12,cnt(f,10))
    def Ztest_flood3(self):
        f={}
        flood(f, (2,18),(-2,15))
        draw(f)
        #self.assertEqual(flood00,f)
        self.assertEqual(12,cnt(f,10))
    def test_scan0(self):
        ls=parse(load("input0"))
        c=scan(ls,10)
        self.assertEqual(res0,c)
    def Ztest_scan1(self):
        ls=parse(load("input1"))
        c=scan(ls,2000000)
        self.assertEqual(res1,c)

def load(name):return open(name,"rt").read()
def parse(s:str)->list:
    ls=[]
    for line in s.splitlines():
        l,r=line.split(": closest beacon is at x=")
        x,y=r.split(", y=")
        b=(int(x),int(y))
        r=l.split("Sensor at x=")[1]
        x,y=r.split(", y=")
        s=(int(x),int(y))
        ls+=[[s,b]]
    #l,r=
    return ls

inp00="""\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
ls00=[
[(2, 18),(-2, 15)],
[(9, 16),(10, 16)],
[(13, 2),(15, 3)],
[(12, 14),(10, 16)],
[(10, 20),(10, 16)],
[(14, 17),(10, 16)],
[(8, 7),(2, 10)],
[(2, 0),(2, 10)],
[(0, 11),(2, 10)],
[(20, 14),(25, 17)],
[(17, 20),(21, 22)],
[(16, 7),(15, 3)],
[(14, 3),(15, 3)],
[(20, 1),(15, 3)],
]
map00={
(2,18):S,(-2,15):B,
(9, 16):S,(10, 16):B,
(13, 2):S,(15, 3):B,
(12, 14):S,(10, 16):B,
(10, 20):S,(10, 16):B,
(14, 17):S,(10, 16):B,
(8, 7):S,(2, 10):B,
(2, 0):S,(2, 10):B,
(0, 11):S,(2, 10):B,
(20, 14):S,(25, 17):B,
(17, 20):S,(21, 22):B,
(16, 7):S,(15, 3):B,
(14, 3):S,(15, 3):B,
(20, 1):S,(15, 3):B,
}
flood00={
(2,-2):H,
(1, -1):H,(2, -1):H,(3,-1):H,
(0, 0):B,(1,0):H,(2,0):S,(3,0):H,(4,0):H,
(1, 1):H,(2, 1):H,(3,1):H,
(2,2):H,
}
