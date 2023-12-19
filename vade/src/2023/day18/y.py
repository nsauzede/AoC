infinity=9999999999999999999
def parse(inp:str)->(list,tuple,tuple):
    m=[]
    s=[0,0]
    e=[0,0]
    j=0
    for l in inp.splitlines():
        r=[]
        for c in l:
            r+=[int(c)]
        m+=[r]
    return m,s,e

def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):
        mat+=[row.copy()]
    return mat

def draw(m:list, v:list):
    w=len(m[0])
    h=len(m)
    #d=mkmat(['.']*w, h)
    import copy
    d=copy.deepcopy(m)
    for i in range(len(v)-1):
        c=v[i]
        n=v[i+1]
        x='?'
        if n[0]>c[0]:x='>'
        if n[0]<c[0]:x='<'
        if n[1]>c[1]:x='v'
        if n[1]<c[1]:x='^'
        d[n[1]][n[0]]=x
    j=0
    for r in d:
        i=0
        for e in r:
            print(f"{e}",end="")
        print("")
    print("")

def calc(m:list, s:list, e: list)->int:
    v=astar(m,s,e,h,d)
    draw(m,v)
    c=len(v)-1
    return c

def run1(inp:str)->int:
    m,s,e=parse(inp)
    c=calc(m,s,e)
    return c

def run2(inp:str)->int:
    m,s,e=parse(inp)
    starts=getstarts(m)
    min=infinity
    for s in starts:
        c=calc(m,s,e)
        if c>0 and c<min:
            min=c
    return min

# d(current,neighbor) is the weight of the edge from current to neighbor
# d is the heuristic function. h(n) estimates the cost to reach goal from node n.
def d(maze,fro,to):
    t=maze[to[1]][to[0]]
    f=maze[fro[1]][fro[0]]
    v=t-f
    #if v==0:v+=1        # increase cost of same levels moves to avoid pseudo zero cost
    #if v>=2:v=infinity  # prevent ever choosing 2+ levels edges
    return v

# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def h(maze,n):
    v=maze[n[1]][n[0]]
    return v

import unittest
def load(name):return open(name,"rt").read()
S=(0,0)
E=(2,1)
m0=[
[0,2,3],
[1,4,5],
[2,3,5],
]
res0 = 31
res1 = 425
res0_2 = 29
res1_2 = 418
INP011=r"""2413
3215
3255
3446
"""
SOL011="""2>>3
32v>
3255
3446
"""
#RES1=1181               # too high
RES1=0
RES011=11               # 5+1+1+4
INP01=r"""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
SOL01=r"""2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
"""
RES01=102               # 3+3+3+6+3+3+7+3+5+6+5+3+5+4+2+4+5+3+1+3+2+3+5+4+5+1+1+4
class T1(unittest.TestCase):
    def test_0100(self):
        m,s,e=parse(INP01)
        #print(f"m={m}")
        s=(0,0)
        l=len(m)
        e=(l-1,l-1)
        v=astar(m,s,e,h,d)
        draw(m,v)
        print(f"v={v}")
        res=0
        for e in v[1:]:
            #print(f"e={e}")
            res+=m[e[1]][e[0]]
        self.assertEqual(RES01, res)
    def Ztest_1000(self):
        m,s,e=parse(open("input1","rt").read())
        #print(f"m={m}")
        s=(0,0)
        l=len(m)
        e=(l-1,l-1)
        v=astar(m,s,e,h,d)
        draw(m,v)
        #print(f"v={v}")
        res=0
        for e in v[1:]:
            #print(f"e={e}")
            res+=m[e[1]][e[0]]
        self.assertEqual(RES1, res)
    def Ztest_0110(self):
        m,s,e=parse(INP011)
        print(f"m={m}")
        s=(0,0)
        e=(3,1)
        v=astar(m,s,e,h,d)
        draw(m,v)
        print(f"v={v}")
        res=0
        for e in v[1:]:
            #print(f"e={e}")
            res+=m[e[1]][e[0]]
        self.assertEqual(RES011, res)
    def Ztest_50(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def Ztest_60(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def Ztest_70(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def Ztest_80(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))

def reconspath(camefrom,current):
    total=[current]
    while current in camefrom:
        current=camefrom[current]
        total.insert(0,current)
    return total

def astar(maze,start,goal,h,d):
    global infinity
    ww=len(maze[0])
    hh=len(maze)
    openset={start:0}
    camefrom={}
    gscore={}
    for y in range(hh):
        for x in range(ww):
            gscore[(x,y)]=infinity
    gscore[start]=0
    fscore={start:[h(maze,start),[0,0,0,0]]}            # R D L U
    prev=tuple(start)
    while len(openset)>0:
        fsmin=infinity
        for e in openset:
            fs=fscore[e][0]
            if fs<fsmin:
                current=e
                fsmin=fs
        dirs=fscore[current][1]
        #print(f"prev={prev} current={current} dirs={dirs}")
        if current==goal:
            return reconspath(camefrom,current)
        del openset[current]
        x,y=current
        neighbors=[]
        if x>0 and prev!=(x-1,y):neighbors+=[(x-1,y)]
        if y>0 and prev!=(x,y-1):neighbors+=[(x,y-1)]
        if x<ww-1 and prev!=(x+1,y):neighbors+=[(x+1,y)]
        if y<hh-1 and prev!=(x,y+1):neighbors+=[(x,y+1)]
        for neighbor in neighbors:
            di=dirs.copy()
            n=0
            if neighbor[0]>current[0]:di=[u*v+v for u,v in zip(di,[1,0,0,0])];n=di[0]
            elif neighbor[0]<current[0]:di=[u*v+v for u,v in zip(di,[0,0,1,0])];n=di[2]
            elif neighbor[1]>current[1]:di=[u*v+v for u,v in zip(di,[0,1,0,0])];n=di[1]
            elif neighbor[1]<current[1]:di=[u*v+v for u,v in zip(di,[0,0,0,1])];n=di[3]
            if n>3:n=infinity
            else:n=0
            tentgscore=gscore[current]+d(maze,current,neighbor)+n
            if tentgscore<gscore[neighbor]:
                camefrom[neighbor]=current
                gscore[neighbor]=tentgscore
                fscore[neighbor]=[tentgscore+h(maze,neighbor),di]
                if neighbor not in openset:
                    openset[neighbor]=0
        prev=tuple(current)
    return []   # failure
