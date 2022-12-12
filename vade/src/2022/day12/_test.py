infinity=9999999999999999999
def parse(inp:str)->(list,tuple,tuple):
    m=[]
    s=[0,0]
    e=[0,0]
    j=0
    for l in inp.splitlines():
        r=[]
        i=0
        for c in l:
            if c=='S':s=(i,j);c='a'
            elif c=='E':e=(i,j);c='z'
            r+=[ord(c)-ord('a')]
            i+=1
        m+=[r]
        j+=1
    return m,s,e

def getstarts(m:list)->list:
    l=[]
    j=0
    for r in m:
        i = 0
        for e in r:
            if e==0:
                l+=[(i,j)]
            i+=1
        j+=1
    return l

def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):
        mat+=[row.copy()]
    return mat

def draw(m:list, v:list):
    return
    w=len(m[0])
    h=len(m)
    d=mkmat(['.']*w, h)
    for i in range(len(v)-1):
        c=v[i]
        n=v[i+1]
        x='?'
        if n[0]>c[0]:x='>'
        if n[0]<c[0]:x='<'
        if n[1]>c[1]:x='v'
        if n[1]<c[1]:x='^'
        d[c[1]][c[0]]=x
    print(f"goal={v[-1]}")
    print(f"draw")
    j=0
    for r in d:
        i=0
        for e in r:
            print(f" {e}",end="")
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
    if v==0:v+=1        # increase cost of same levels moves to avoid pseudo zero cost
    if v>=2:v=infinity  # prevent ever choosing 2+ levels edges
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
class T1(unittest.TestCase):
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
    fscore={start:h(maze,start)}
    while len(openset)>0:
        fsmin=infinity
        for e in openset:
            fs=fscore[e]
            if fs<fsmin:
                current=e
                fsmin=fs
        if current==goal:
            return reconspath(camefrom,current)
        del openset[current]
        x,y=current
        neighbors=[]
        if x>0:neighbors+=[(x-1,y)]
        if y>0:neighbors+=[(x,y-1)]
        if x<ww-1:neighbors+=[(x+1,y)]
        if y<hh-1:neighbors+=[(x,y+1)]
        for neighbor in neighbors:
            tentgscore=gscore[current]+d(maze,current,neighbor)
            if tentgscore<gscore[neighbor]:
                camefrom[neighbor]=current
                gscore[neighbor]=tentgscore
                fscore[neighbor]=tentgscore+h(maze,neighbor)
                if neighbor not in openset:
                    openset[neighbor]=0
    return []   # failure
