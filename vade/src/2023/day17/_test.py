import unittest
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
INP011=r"""2413
3215
3255
3446
"""
SOL011="""2>>3
32v>>
3255
3446
"""
RES011=11               # 5+1+1+4
RES1=0
RES02=0
RES2=0
N='.';R='>';D='v';L='<';U='^';
from astar import astar,infinity
def astar_h(maze:list,n:list)->int:
    c,n,d=maze[n[1]][n[0]]
    v=c
    return v
def astar_d(maze:list,fro:list,to:list,camefrom:dict)->int:
    #print(f"fro={fro} to={to} camefrom={camefrom}")
    t=astar_h(maze,to)
    f=astar_h(maze,fro)
    """if to[0]>fro[0]:
        print(">>")
    elif to[0]<fro[0]:
        print("<<")
    elif to[1]>fro[1]:
        print("VV")
    elif to[1]<fro[1]:
        print("^^")"""
    v=t-f
    #if v==0:v+=1        # increase cost of same levels moves to avoid pseudo zero cost
    #if v>=2:v=infinity  # prevent ever choosing 2+ levels edges
    return v
def astar_visit(maze,fro,to,t,g,h):
    #print(f"VISIT: fro={fro} to={to} t={t} g={g} h={h}")
    pass
def astar_reconspath(camefrom,current):
    total=[current]
    #print(f"camefrom={camefrom} current={current}")
    while current in camefrom:
        current0=current
        current=camefrom[current][0]
        #print(f"current0={current0} current={current}")
        total.insert(0,current)
    return total
def drawpath(d,v)->int:
    res=0
    d['path']=v
    last=d['path'][0]
    di='?'
    for p in d['path']:
        #print(f"p={p} last={last}")
        if p[0]>last[0]:
            di=R
        elif p[0]<last[0]:
            di=L
        elif p[1]>last[1]:
            di=D
        elif p[1]<last[1]:
            di=U
        d['m'][p[1]][p[0]][2]=di
        res+=d['m'][p[1]][p[0]][0]
        last=p
    return res
def compute(m0:list,part=0)->int:
    res=0
    h=len(m0)
    w=len(m0[0])
    pos=(0,0)
    goal=(w-1,h-1)
    d={'m':m0,'pos':pos}
    #m=mkmat([('.',0)]*w,h)
    disp(d,"INITIAL")
    v=astar(m0,pos,goal,astar_h,astar_d,astar_reconspath,astar_visit)
    res=drawpath(d,v)
    #print(f"v={v}")
    disp(d,"FINAL")
    return res
def parse(inp:str,part=0)->list:
    res=[]
    for s in inp.splitlines():
        res0=[]
        for c in s:
            res0+=[[int(c),0,N]]
        res+=[res0]
    return res
def disp(d:dict,text="DISP"):
    m=d['m']
    pos=d['pos']
    print(f"\n{text} ============== pos={pos}")
    h=len(m)
    w=len(m[0])
    print("  ",end='')
    for i in range(w):
        print(f"{i%10}",end='')
    print("\n  ",end='')
    for i in range(w):
        if pos and pos[0]==i:
            print(f"*",end='')
        else:
            print(f" ",end='')
    print()
    for j,r in enumerate(m):
        #print(f"i={i} r={r}")
        if pos and pos[1]==j:
            c='*'
        else:
            c=' '
        print(f"{j%10}{c}",end='')
        for i,l in enumerate(r):
            c,n,d=l
            if d!=N:
                c=d
            print(c,end='')
        print()
    print("\n  ",end="")
    for i in range(w):
        print(f"{i%10}",end='')
    print("\n")
class T000(unittest.TestCase):
    def test_0000(self):
        self.assertEqual(0,0)
    def Ztest_0110(self):
        self.assertEqual(RES011+0,compute(parse(INP011)))
    def Ztest_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def Ztest_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES02+0*1000,compute(parse(INP01),part=1))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
