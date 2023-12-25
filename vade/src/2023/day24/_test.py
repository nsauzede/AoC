import unittest
infinity=999999
INP01=r"""19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""
OUT01={'o':[
((19, 13, 30),( -2,  1, -2)),
((18, 19, 22),( -1, -1, -2)),
((20, 25, 34),( -2, -2, -4)),
((12, 31, 28),( -1, -2, -1)),
((20, 19, 15),(  1, -5, -3)),
]
}
RES01=2
RES1=16779
RES02=47
RES2=0
def calc(d:dict,part=0)->int:
    res = 0
    return res
def disp(d0:dict,text="DISP"):
    print(f"\n{text} ==============")
    m=d0['m']
    w,h,d=d0['dims']
    xm,xM,ym,yM,zm,zM=d0['extr']
    #print(f"w={w} h={h} d={d}")
    for x in range(xm,xM+1):
        print(f"{'x'if x==w//2 else ' '}", end="")
    print()
    for x in range(xm,xM+1):
        print(f"{x}", end="")
    print()
    for z in range(zM,zm-2,-1):
        c='-'
        for x in range(xm,xM+1):
            if z>0:
                c='.'
                for y in range(ym,yM+1):
                    p=(x,y,z)
                    if p in m:
                        c=f"{m[p]}"
                        break
            print(f"{c}",end="")
        print(f" {z}{' z'if z==d//2+1 else''}")
    print()

    for x in range(xm,xM+1):
        print(f"{'y'if x==w//2 else ' '}", end="")
    print()
    for y in range(ym,yM+1):
        print(f"{y}", end="")
    print()
    for z in range(zM,zm-2,-1):
        c='-'
        for y in range(ym,yM+1):
            if z>0:
                c='.'
                for x in range(xm,xM+1):
                    p=(x,y,z)
                    if p in m:
                        c=f"{m[p]}"
                        break
            print(f"{c}",end="")
        print(f" {z}{' z'if z==d//2+1 else''}")
    return
    w=len(m[0])
    for j,r in enumerate(m):
        for i,c in enumerate(r):
            print(c,end='')
        print()
def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    import copy
    for i in range(count):mat+=[copy.deepcopy(row)]
    return mat
def eq(pt:tuple)->(float,float):
    A,D=pt
    B=tuple(a+b for a,b in zip(A,D))
    xa,ya=A[0:2]
    xb,yb=B[0:2]
    m=(yb-ya)/(xb-xa)
    p=ya-m*xa
    #print(f"m={m} p={p}")
    return m,p

def inter(a,b)->(float,float):
    if a==b:return None
    elif a[0]==b[0]:return None
    elif a[0]==0:xj,yj=(a[1]-b[1])/a[0],a[1]
    elif b[0]==0:xj,yj=(b[1]-a[1])/b[0],b[1]
    else:
        xj=(b[1]-a[1])/(a[0]-b[0])
        yj=a[0]*xj+a[1]
    #print(f"xj={xj} yj={yj}")
    return xj,yj
def parse(inp:str,part=0)->dict:
    o=[]
    for s in inp.splitlines():
        l,r=s.split('@')
        p=tuple(float(e) for e in l.split(','))
        d=tuple(float(e) for e in r.split(','))
        o+=[(p,d)]
    res={'o':o}
    return res
def dist(pt:tuple,pt2:tuple)->float:
    A,D=pt
    if D[0]!=0:
        return (pt2[0]-A[0])/D[0]
    else:
        return (pt2[1]-A[1])/D[1]
def compute(d0:dict,xm,ym,xM,yM,part=0)->int:
    #print(f"d0={d0}")
    res = 0
    o=d0['o']
    #xm,ym,xM,yM=7,7,27,27
    for j in range(len(o)-1):
        for i in range(j+1,len(o)):
            #print(f"compare j={j} with i={i}")
            A,B=o[j],o[i]
            a=eq(A)
            b=eq(B)
            p=inter(a,b)
            if p:
                x,y=p
                n1=dist(A,p)
                n2=dist(B,p)
                if x>=xm and y>=ym and x<=xM and y<=yM and n1>0 and n2>0:
                    #print(f"p={p} n1={n1} n2={n2} (j={j} i={i})")
                    res+=1
    return res
class T000(unittest.TestCase):
    def test_0110(self):
        res=parse(INP01)
        self.assertEqual(OUT01['o'],res['o'])
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01),7,7,27,27))
    def test_1000(self):
        m=200000000000000
        M=400000000000000
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read()),m,m,M,M))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
