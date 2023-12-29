import unittest
infinity=999999
INP01=r"""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""
INP01_=r"""0,0,2~2,0,2
1,0,1~1,2,1
0,2,3~2,2,3
2,0,5~2,2,5
0,0,4~0,2,4
1,1,8~1,1,9
0,1,6~2,1,6
"""
OUT01={'o':[
[[1,0,1],[1,1,1],[1,2,1]],
[[0,0,2],[1,0,2],[2,0,2]],
[[0,2,3],[1,2,3],[2,2,3]],
[[0,0,4],[0,1,4],[0,2,4]],
[[2,0,5],[2,1,5],[2,2,5]],
[[0,1,6],[1,1,6],[2,1,6]],
[[1,1,8],[1,1,9]],
]
}
RES01=5
#RES1=938  # too high
#RES1=928  # too high
RES1=0
RES02=0
RES2=0
def compute(d0:dict,n=6,part=0)->int:
    #print(f"d0={d0}")
    #disp(d0,"INITIAL")
    d=fall(d0)
    #disp(d,"FINAL")
    res=calc(d)
    return res
def fall(d0:dict)->dict:
    m=d0['m']
    (w,h,d)=d0['dims']
    (xm,xM,ym,yM,zm,zM)=d0['extr']
    print(f"x:{(xm,xM)} y:{(ym,yM)} z:{(zm,zM)}")
    #print(f"z={d0['z']}")
    #print(f"m={m}")
    l=[]
    for i in range(w):
        l+=[[0,-1]]
    floor=mkmat(l,h)
    z1={}
    import copy
    d1=copy.deepcopy(d0)
    o0=copy.deepcopy(d0['o'])
    #print(f"o={o0}")
    for z0 in range(zm,zM):
        if z0 in d1['z']:
            #print(f"d1['z'][z0={z0}]={d1['z'][z0]}")
            nl=d1['z'][z0]
            #print(f"nl={nl}")
            for n in nl:
                o=o0[n]
                delt=[0,0,0]
                #print(f"obj[n={n}]={o}")
                if len(o)==1 or o[0][2]!=o[1][2]:
                    x,y,z=o[0]
                    f=floor[y][x][0]
                    if f>minZ:
                        minZ=f
                    #print(f"floor={f} x={x} y={y} z={z}")
                    #print(f"minZ={minZ}")
                    if z>minZ+1:
                        delt[2]=minZ+1-z
                    if minZ+len(o)>floor[y][x][0]:
                        floor[y][x][0]=minZ+len(o)
                        floor[y][x][1]=n
                elif o[0][0]!=o[1][0]:
                    x,y,z=o[0]
                    minZ=-infinity
                    for x in range(o[0][0],o[-1][0]+1):
                        f=floor[y][x][0]
                        if f>minZ:
                            minZ=f
                        #print(f"floor={f} x={x} y={y} z={z}")
                    #print(f"minZ={minZ}")
                    if z>minZ+1:
                        delt[2]=minZ+1-z
                    for x in range(o[0][0],o[-1][0]+1):
                        if minZ+1>floor[y][x][0]:
                            floor[y][x][0]=minZ+1
                            floor[y][x][1]=n
                elif o[0][1]!=o[1][1]:
                    x,y,z=o[0]
                    minZ=-infinity
                    for y in range(o[0][1],o[-1][1]+1):
                        f=floor[y][x][0]
                        if f>minZ:
                            minZ=f
                        #print(f"floor={f} x={x} y={y} z={z}")
                    #print(f"minZ={minZ}")
                    if z>minZ+1:
                        delt[2]=minZ+1-z
                    for y in range(o[0][1],o[-1][1]+1):
                        if minZ+1>floor[y][x][0]:
                            floor[y][x][0]=minZ+1
                            floor[y][x][1]=n
                #print(f"delt={delt}")
                #print(f"floor={floor}")
                if delt!=[0,0,0]:
                    o0[n]=[[x+y for x,y in zip(l,delt)]for l in o0[n]]
                    #print(f"remove n={n} from nl={nl}")
                    nl.remove(n)
                    d1['z'][o0[n][0][2]]=n
    res=place_objs(o0)
    return res
def calc(d:dict,part=0)->int:
    res = 0
    #print(f"m={d['m']}")
    below={}
    for n,o in enumerate(d['o']):
        #print(f"n={n} o={o}")
        if len(o)==1 or o[0][2]!=o[1][2]:
            x,y,z=o[0]
            pos=(x,y,z-1)
            #print(f"checking pos={pos}")
            if pos in d['m']:
                n0=d['m'][pos]
                #print(f"pos={pos} n0={n0}")
                if n not in below:
                    below[n]=[]
                below[n]+=[n0]
        elif o[0][0]!=o[1][0]:
            x,y,z=o[0]
            for x in range(o[0][0],o[-1][0]+1):
                pos=(x,y,z-1)
                #print(f"checking pos={pos}")
                if pos in d['m']:
                    n0=d['m'][pos]
                    #print(f"pos={pos} n0={n0}")
                    if n not in below:
                        below[n]=[]
                    below[n]+=[n0]
        elif o[0][1]!=o[1][1]:
            x,y,z=o[0]
            for y in range(o[0][1],o[-1][1]+1):
                pos=(x,y,z-1)
                #print(f"checking pos={pos}")
                if pos in d['m']:
                    n0=d['m'][pos]
                    #print(f"pos={pos} n0={n0}")
                    if n not in below:
                        below[n]=[]
                    below[n]+=[n0]
    print(f"below={below}")
    above={}
    for k,v in below.items():
        #print(f"below k={k} v={v}")
        for n in v:
            if n not in above:
                above[n]=[]
            above[n]+=[k]
    print(f"above={above}")
    print(f"len(above)={len(above)}")
    #for k,v in above.items():
    for k in range(len(d['o'])):
        #print(f"checking k={k}")
        if k in above:
            v=above[k]
            r=0
            for n0 in v:
                if n0 in below:
                    for n in below[n0]:
                        if n!=k:
                            r=1
                            break
                    if r==0:
                        break
        else:
            r=1
        if k in below:be=below[k]
        else:be=[]
        if k in above:ab=above[k]
        else:ab=[]
        #print(f"k={k} is {'ok'if r>0 else 'KO'} !!! be={be} ab={ab}")
        res+=r
    return res
def parse_objs(inp:str,part=0)->(list,dict):
    o=[]
    #print(f"inp={inp}")
    for i,s in enumerate(inp.splitlines()):
        start,stop=s.split("~")
        start=[int(e)for e in start.split(",")]
        stop=[int(e)for e in stop.split(",")]
        p=start
        r=[]
        for dim in (0,1,2):
            if start[dim]!=stop[dim]:
                break
        for p[dim] in range(start[dim],stop[dim]+1):
                r+=[p.copy()]
        o+=[r]
    return o
def place_objs0(objs:[])->(dict,int,int,int,int,int,int,int,int,int):
    m={}
    xm=infinity
    ym=infinity
    zm=infinity
    xM=-infinity
    yM=-infinity
    zM=-infinity
    for i,o in enumerate(objs):
        for x,y,z in o:
            if x<xm:xm=x
            if x>xM:xM=x
            if y<ym:ym=y
            if y>yM:yM=y
            if z<zm:zm=z
            if z>zM:zM=z
            m[(x,y,z)]=i
    #print(m)
    #print(f"x:{(xm,xM)} y:{(ym,yM)} z:{(zm,zM)}")
    w=xM-xm+1
    h=yM-ym+1
    d=zM-zm+1
    return m,w,h,d,xm,xM,ym,yM,zm,zM
def place_objs(objs:[])->dict:
    z={}
    for i,o in enumerate(objs):
        start=o[0]
        if start[2]not in z:z[start[2]]=[]
        z[start[2]]+=[i]
    res={'o':objs,'z':z}
    m,w,h,d,xm,xM,ym,yM,zm,zM=place_objs0(objs)
    res['m']=m
    res['dims']=(w,h,d)
    res['extr']=(xm,xM,ym,yM,zm,zM)
    return res
def parse(inp:str,part=0)->dict:
    o=parse_objs(inp,part)
    res=place_objs(o)
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
class T000(unittest.TestCase):
    def test_0010(self):
        self.assertEqual([[0,0,0],[0,0,0],[0,0,0]],mkmat([0]*3,3))
    def Ztest_0110(self):
        res=parse(INP01)
        #print(f"\nres={res}")
        #print(f"OUT={OUT01}")
        self.assertEqual(OUT01['o'],res['o'])
    def Ztest_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def Ztest_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
