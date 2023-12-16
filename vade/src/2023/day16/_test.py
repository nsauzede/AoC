import unittest
INP01=r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
RES01=46
#RES1=5688 # too low
RES1=6816
RES02=51
RES2=8163
N='.';R='>';D='v';L='<';U='^';
def walk(seen,m,h,w,j,i,d,nest=0,cnt=0)->int:
    while True:
        if d==R:
            i+=1
        elif d==D:
            j+=1
        elif d==L:
            i-=1
        elif d==U:
            j-=1
        if j>=h or j<0 or i>=w or i<0:
            break
        k=f"{j} {i} {d}"
        if k in seen:
            break
        seen[k]=1
        c,n,d0=m[j][i]
        #if d==d0:break
        #disp(m,f"WALK #{cnt} nest={nest} j={j} i={i} d={d} c={c} n={n} d0={d0}",(j,i))
        #print(f"WALK #{cnt} nest={nest} j={j} i={i} d={d} c={c} n={n} d0={d0}")
        #if n>1:break
        n+=1
        m[j][i][1]=n
        #print(f"INC {j} {i}: {n}")
        m[j][i][2]=d
        if c=='|':
            if d==R or d==L:
                walk(seen,m,h,w,j,i,U,nest+1,cnt)
                #walk(seen,m,h,w,j,i,D,nest+1,cnt);break
                d=D
        elif c=='-':
            if d==U or d==D:
                walk(seen,m,h,w,j,i,L,nest+1,cnt)
                #walk(seen,m,h,w,j,i,R,nest+1,cnt);break
                d=R
        elif c=='\\':
            if d==R:d=D
            elif d==D:d=R
            elif d==L:d=U
            elif d==U:d=L
        elif c=='/':
            if d==R:d=U
            elif d==D:d=L
            elif d==L:d=D
            elif d==U:d=R
        cnt+=1
def total(m,h,w):
    res=0
    for y in range(h):
        for x in range(w):
            #print(f"{y} {x}: {m[y][x]}")
            if m[y][x][1]>0:
                res+=1
    return res
def compute(m0:list,part=0)->int:
    res=0
    h=len(m0)
    w=len(m0[0])
    #m=mkmat([('.',0)]*w,h)
    #disp(m0,"INITIAL")
    m=m0
    seen={}
    if part==0:
        walk(seen,m,h,w,0,-1,R)
        res=total(m,h,w)
    else:
        res=0
        i0=-1
        for i in range(w):
            import copy
            seen={}
            m=copy.deepcopy(m0)
            walk(seen,m,h,w,-1,i,D)
            res0=total(m,h,w)
            #print(f"i={i} res={res}")
            if res0>res:
                i0=i
                res=res0
            seen={}
            m=copy.deepcopy(m0)
            walk(seen,m,h,w,h,i,U)
            res0=total(m,h,w)
            #print(f"i={i} res={res}")
            if res0>res:
                i0=i
                res=res0
        for j in range(h):
            import copy
            seen={}
            m=copy.deepcopy(m0)
            walk(seen,m,h,w,j,-1,R)
            res0=total(m,h,w)
            #print(f"i={i} res={res}")
            if res0>res:
                i0=i
                res=res0
            seen={}
            m=copy.deepcopy(m0)
            walk(seen,m,h,w,w,i,L)
            res0=total(m,h,w)
            #print(f"i={i} res={res}")
            if res0>res:
                i0=i
                res=res0
        #print(f"max for i0={i0}")
    #disp(m,"FINAL")
    return res
def parse(inp:str,part=0)->list:
    res=[]
    for s in inp.splitlines():
        res0=[]
        for c in s:
            res0+=[[c,0,N]]
        res+=[res0]
    return res
def mkmat0(cnt=3)->list:
    return [None]*cnt
def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):mat+=[row.copy()]
    return mat
def disp(m:list,text="DISP",pos=None):
    #print(f"m={m}")
    print(f"\n{text} ==============")
    h=len(m)
    w=len(m[0])
    print("  ",end='')
    for i in range(w):
        print(f"{i%10}",end='')
    print("\n  ",end='')
    for i in range(w):
        if pos and pos[1]==i:
            print(f"*",end='')
        else:
            print(f" ",end='')
    print()
    for j,r in enumerate(m):
        #print(f"i={i} r={r}")
        if pos and pos[0]==j:
            c='*'
        else:
            c=' '
        print(f"{j%10}{c}",end='')
        for i,l in enumerate(r):
            c,n,d=l
            n=l[1]
            #print(f"{j} {i}: {l}")
            if c=='.':
                if n>=1:
                    if n>1:
                        c=n
                    else:
                        c=d
            print(c,end='')
        print()
class T000(unittest.TestCase):
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def test_0200(self):
        self.assertEqual(RES02+0*1000,compute(parse(INP01),part=1))
    def test_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
