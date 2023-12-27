import unittest
infinity=999999
INP01=r"""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""
OUT01={'m':[
['#','.','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','.','.','.','#','#','#'],
['#','#','#','#','#','#','#','.','#','#','#','#','#','#','#','#','#','.','#','.','#','#','#'],
['#','#','#','.','.','.','.','.','#','.','>','.','>','.','#','#','#','.','#','.','#','#','#'],
['#','#','#','v','#','#','#','#','#','.','#','v','#','.','#','#','#','.','#','.','#','#','#'],
['#','#','#','.','>','.','.','.','#','.','#','.','#','.','.','.','.','.','#','.','.','.','#'],
['#','#','#','v','#','#','#','.','#','.','#','.','#','#','#','#','#','#','#','#','#','.','#'],
['#','#','#','.','.','.','#','.','#','.','#','.','.','.','.','.','.','.','#','.','.','.','#'],
['#','#','#','#','#','.','#','.','#','.','#','#','#','#','#','#','#','.','#','.','#','#','#'],
['#','.','.','.','.','.','#','.','#','.','#','.','.','.','.','.','.','.','#','.','.','.','#'],
['#','.','#','#','#','#','#','.','#','.','#','.','#','#','#','#','#','#','#','#','#','v','#'],
['#','.','#','.','.','.','#','.','.','.','#','.','.','.','#','#','#','.','.','.','>','.','#'],
['#','.','#','.','#','v','#','#','#','#','#','#','#','v','#','#','#','.','#','#','#','v','#'],
['#','.','.','.','#','.','>','.','#','.','.','.','>','.','>','.','#','.','#','#','#','.','#'],
['#','#','#','#','#','v','#','.','#','.','#','#','#','v','#','.','#','.','#','#','#','.','#'],
['#','.','.','.','.','.','#','.','.','.','#','.','.','.','#','.','#','.','#','.','.','.','#'],
['#','.','#','#','#','#','#','#','#','#','#','.','#','#','#','.','#','.','#','.','#','#','#'],
['#','.','.','.','#','#','#','.','.','.','#','.','.','.','#','.','.','.','#','.','#','#','#'],
['#','#','#','.','#','#','#','.','#','.','#','#','#','v','#','#','#','#','#','v','#','#','#'],
['#','.','.','.','#','.','.','.','#','.','#','.','>','.','>','.','#','.','>','.','#','#','#'],
['#','.','#','#','#','.','#','#','#','.','#','.','#','#','#','.','#','.','#','v','#','#','#'],
['#','.','.','.','.','.','#','#','#','.','.','.','#','#','#','.','.','.','#','.','.','.','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','.','#'],
],
'start':(1,0),
'goal':(21,22),
}
RES01=94
RES1=2278
RES02=154
#RES2=6583       # too low
#RES2=6735       # too high
RES2=0
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
def parse(inp:str,part=0)->dict:
    m=[]
    for s in inp.splitlines():
        m+=[list(s)]
    j=0
    for i,c in enumerate(m[j]):
        if c=='.':
            start=(i,j)
            break
    j=len(m)-1
    for i,c in enumerate(m[j]):
        if c=='.':
            goal=(i,j)
            break
    res={'m':m,'start':start,'goal':goal}
    return res
N='^';E='>';S='v';W='<'
def walk00(d0:dict,seen0:dict,x,y,heading=S,part=0)->dict:
    m=d0['m']
    h=len(m)
    w=len(m[0])
    if x<0 or x>=w or y<0 or y>=h:
        return None
    if m[y][x]=='#':
        return None
    #"""
    if m[y][x]=='<' and heading==E:
        return None
    if m[y][x]=='>' and heading==W:
        return None
    if m[y][x]=='^' and heading==S:
        return None
    if m[y][x]=='v' and heading==N:
        return None
    #"""
    pos=(x,y)
    if pos in seen0:
        return None
    seen0[pos]=1
    if pos==d0['goal']:
        #print(f"goal reached at {pos}, seen0={seen0}")
        return seen0
    if m[y][x]=='<':
        r=walk0(d0,seen0.copy(),x-1,y,W,part)
        if r:d0['r']+=[r]
    elif m[y][x]=='>':
        r=walk0(d0,seen0.copy(),x+1,y,E,part)
        if r:d0['r']+=[r]
    elif m[y][x]=='^':
        r=walk0(d0,seen0.copy(),x,y-1,N,part)
        if r:d0['r']+=[r]
    elif m[y][x]=='v':
        r=walk0(d0,seen0.copy(),x,y+1,S,part)
        if r:d0['r']+=[r]
    else:
        r=walk0(d0,seen0.copy(),x,y-1,N,part)
        if r:d0['r']+=[r]
        r=walk0(d0,seen0.copy(),x+1,y,E,part)
        if r:d0['r']+=[r]
        r=walk0(d0,seen0.copy(),x,y+1,S,part)
        if r:d0['r']+=[r]
        r=walk0(d0,seen0.copy(),x-1,y,W,part)
        if r:d0['r']+=[r]
    return None
def walk0(d0:dict,seen0:dict,x,y,heading=S,nest=0,part=0)->dict:
    m=d0['m']
    h=len(m)
    w=len(m[0])
    p0=part==0
    #print(f"nest={nest} heading={heading}")
    while True:
        if x<0 or x>=w or y<0 or y>=h:
            #print(f"out limits")
            return None
        if m[y][x]=='#':
            #print(f"hit wall")
            return None
        #"""
        if p0 and m[y][x]=='<' and heading==E:
            #print(f"hit <")
            return None
        if p0 and m[y][x]=='>' and heading==W:
            #print(f"hit >")
            return None
        if p0 and m[y][x]=='^' and heading==S:
            #print(f"hit ^")
            return None
        if p0 and m[y][x]=='v' and heading==N:
            #print(f"hit v")
            return None
        #"""
        pos=(x,y)
        if pos in seen0:
            #print(f"already seen")
            return None
        seen0[pos]=1
        if pos==d0['goal']:
            #print(f"goal reached at {pos}, seen0={seen0}")
            l=len(seen0)
            if l>d0['max']:
                print(f"goal reached - len(seen0)={l}")
                d0['max']=l
                d0['r']=[]
                d0['r']+=[seen0]
            return None
            return seen0
        if p0 and m[y][x]=='<':
            x-=1
            heading=W
        elif p0 and m[y][x]=='>':
            x+=1
            heading=E
        elif p0 and m[y][x]=='^':
            y-=1
            heading=N
        elif p0 and  m[y][x]=='v':
            y+=1
            heading=S
        else:
            nxt=[]
            if y>0 and (not p0 or m[y-1][x]!='v') and m[y-1][x]!='#' and heading!=S:
                nxt+=[(x,y-1,N)]
            if x<w-1 and (not p0 or m[y][x+1]!='v') and m[y][x+1]!='#' and heading!=W:
                nxt+=[(x+1,y,E)]
            if y<h-1 and (not p0 or m[y+1][x]!='^') and m[y+1][x]!='#' and heading!=N:
                nxt+=[(x,y+1,S)]
            if x>0 and (not p0 or m[y][x-1]!='>') and m[y][x-1]!='#' and heading!=E:
                nxt+=[(x-1,y,W)]
            #print(f"len(nxt)={len(nxt)}")
            if len(nxt)==0:
                #print(f"no candidate")
                break
            for n in nxt[1:]:
                #print(f"walk {n}")
                x,y,heading=n
                r=walk0(d0,seen0.copy(),x,y,heading,nest+1,part)
                #if r:d0['r']+=[r]
            x,y,heading=nxt[0]
        #print(f"loop {(x,y,heading)}")
    return None
def compute(d0:dict,n=6,part=0)->int:
    #print(f"d0={d0}")
    #disp(d0,"INITIAL")
    #d=walk(d0,part=part)
    seen={}
    x,y=d0['start']
    d0['r']=[]
    d0['max']=0
    d=walk0(d0,seen,x,y,S,0,part=part)
    #disp(d,"FINAL")
    res=calc(d0['r'])
    return res
def calc(d:dict,part=0)->int:
    #print(f"d={d}")
    res=0
    for e in d:
        l=len(e)-1
        if l>res:
            res=l
        #print(f" len={l}")
    return res
class T000(unittest.TestCase):
    def Ztest_0010(self):
        self.assertEqual([[0,0,0],[0,0,0],[0,0,0]],mkmat([0]*3,3))
    def Ztest_0110(self):
        res=parse(INP01)
        #print(f"\nres={res}")
        #print(f"OUT={OUT01}")
        self.assertEqual(OUT01['m'],res['m'])
        self.assertEqual(OUT01['start'],res['start'])
        self.assertEqual(OUT01['goal'],res['goal'])
    def test_0120(self):
        INP011=r"""#.#
#.#
"""
        OUT011={'m':[
['#','.','#'],
['#','.','#'],
],
'start':(1,0),
'goal':(1,1),
}
        RES011=1
        res=parse(INP011)
        self.assertEqual(OUT011['m'],res['m'])
        self.assertEqual(OUT011['start'],res['start'])
        self.assertEqual(OUT011['goal'],res['goal'])
        self.assertEqual(RES011+0,compute(parse(INP011)))
    def test_0130(self):
        INP011=r""".##
...
...
##.
"""
        OUT011={'m':[
['.','#','#'],
['.','.','.'],
['.','.','.'],
['#','#','.'],
],
'start':(0,0),
'goal':(2,3),
}
        RES011=7
        res=parse(INP011)
        self.assertEqual(OUT011['m'],res['m'])
        self.assertEqual(OUT011['start'],res['start'])
        self.assertEqual(OUT011['goal'],res['goal'])
        self.assertEqual(RES011+0,compute(parse(INP011)))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES02+0,compute(parse(INP01), part=1))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
