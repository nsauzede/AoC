import unittest
INP01=r"""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
SOL011=r"""#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
"""
RES011=38
SOL01=r"""#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######
"""
RES01=62
#RES1=27109     # too low
#RES1=70025     # too low
RES1=70026
RES021=[
['R',461937,'#70c710'],
['D',56407,'#0dc571'],
['R',356671,'#5713f0'],
['D',863240,'#d2c081'],
['R',367720,'#59c680'],
['D',266681,'#411b91'],
['L',577262,'#8ceee2'],
['U',829975,'#caa173'],
['L',112010,'#1b58a2'],
['D',829975,'#caa171'],
['L',491645,'#7807d2'],
['U',686074,'#a77fa3'],
['L',5411,'#015232'],
['U',500254,'#7a21e3'],
]
"""
    #d2c081 = D 863240
    #59c680 = R 367720
    #411b91 = D 266681
    #8ceee2 = L 577262
    #caa173 = U 829975
    #1b58a2 = L 112010
    #caa171 = D 829975
    #7807d2 = L 491645
    #a77fa3 = U 686074
    #015232 = L 5411
    #7a21e3 = U 500254
"""
RES02=952408144115
RES2=0

#N='.';R='>';D='v';L='<';U='^';
N=' ';R='R';D='D';L='L';U='U';
BOUNDARY=":"
INTERIOR="#"
def compute(insns:list,part=0)->int:
    res=0
    pos=(0,0)
    m0,pos,surf=dig(pos,insns,part)
    h=len(m0)
    w=len(m0[0])
    #disp(m0,"INITIAL")
    dump(m0,pos,"initial.ppm")
    res1=calc(m0,pos)
    res=res1
    print(f"initial res={res}")
    import copy
    m1=copy.deepcopy(m0)
    dig2(m1,surf,pos,insns,part)
    #disp(m1,"FINAL")
    dump(m1,pos,"final.ppm")
    res2=calc(m1,pos)
    res=res2
    print(f"final res={res}")
    return res
def floodD(m:list,surf,w,h,x,y):
    while True:
        if x<0 or x>=w or y<0 or y>=h:
            break
        if (x,y)in surf:
            break
        #print(f" floodD {x} {y},", end='')
        m[y][x]=INTERIOR
        y+=1
def floodR(m:list,surf,w,h,x,y):
    while True:
        if x<0 or x>=w or y<0 or y>=h:
            break
        if (x,y)in surf:
            break
        #print(f" floodR {x} {y},", end='')
        m[y][x]=INTERIOR
        x+=1
def floodU(m:list,surf,w,h,x,y):
    while True:
        if x<0 or x>=w or y<0 or y>=h:
            break
        if (x,y)in surf:
            break
        #print(f" floodU {x} {y},", end='')
        m[y][x]=INTERIOR
        y-=1
def floodL(m:list,surf,w,h,x,y):
    while True:
        if x<0 or x>=w or y<0 or y>=h:
            break
        if (x,y)in surf:
            break
        #print(f" floodL {x} {y},", end='')
        m[y][x]=INTERIOR
        x-=1
def dig2(m:list,surf:dict,pos:list,insns:list,part=0)->list:
    x,y=pos
    h=len(m)
    w=len(m[0])
    #print(f"w={w} h={h}")
    i=0
    last=N
    for insn in insns:
        d,n,c=insn
        if d==R:
            delta=0
            if last==D:delta=-1
            #print(f"R {n} x0={x} y0={y}")
            for x in range(x+1+delta,x+n+1):
                #print(f" x={x} y={y},", end='')
                floodD(m,surf,w,h,x,y+1)
            #print()
        elif d==D:
            delta=0
            if last==L:delta=-1
            #print(f"D {n} x0={x} y0={y}")
            for y in range(y+1+delta,y+n+1):
                #print(f" x={x} y={y},", end='')
                floodL(m,surf,w,h,x-1,y)
            #print()
        elif d==L:
            delta=0
            if last==U:delta=1
            #print(f"L {n} x0={x} y0={y}")
            for x in range(x-1+delta,x-n-1,-1):
                #print(f" x={x} y={y},", end='')
                floodU(m,surf,w,h,x,y-1)
            #print()
        elif d==U:
            delta=0
            if last==R:delta=1
            #print(f"U {n} x0={x} y0={y}")
            for y in range(y-1+delta,y-n-1,-1):
                #print(f" x={x} y={y},", end='')
                floodR(m,surf,w,h,x+1,y)
            #print()
        #disp(m, f"Flood #{i}")
        i+=1
        last=d
    return m
def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):
        mat+=[row.copy()]
    return mat
def calc(m:list,pos)->int:
    res = 0
    for j,r in enumerate(m):
        for i,c in enumerate(r):
            if c==BOUNDARY or c==INTERIOR:
                if (i,j)==pos:print("CALC SEE POS!!")
                res+=1
    return res
def dig(pos:list,insns:list,part=0)->tuple:
    x,y=pos
    xmin=x;ymin=y
    xmax=x;ymax=y
    for insn in insns:
        d,n,c=insn
        if d==R:x+=n
        elif d==D:y+=n
        elif d==L:x-=n
        elif d==U:y-=n
        if x<xmin:xmin=x
        if x>xmax:xmax=x
        if y<ymin:ymin=y
        if y>ymax:ymax=y
    w=xmax-xmin+1
    h=ymax-ymin+1
    print(f"xmin={xmin} ymin={ymin}")
    print(f"xmax={xmax} ymax={ymax}")
    #print(f"w={w} h={h}")
    m=mkmat(['.']*w,h)
    x=abs(xmin);y=abs(ymin)
    pos=(x,y)
    surf={}
    print(f"first x,y={x,y}")
    i=0
    for insn in insns:
        #print(f"INSN #{i}...")
        i+=1
        d,n,c=insn
        if d==R:
            #print(f"R {n} x0={x} y0={y}")
            for x in range(x+1,x+n+1):
                if (x,y)in surf:0/0
                surf[(x,y)]=1
                #print(f" x={x} y={y},", end='')
                m[y][x]=BOUNDARY
            #print()
        elif d==D:
            #print(f"D {n} x0={x} y0={y}")
            for y in range(y+1,y+n+1):
                if (x,y)in surf:0/0
                surf[(x,y)]=1
                #print(f" x={x} y={y},", end='')
                m[y][x]=BOUNDARY
            #print()
        elif d==L:
            #print(f"L {n} x0={x} y0={y}")
            for x in range(x-1,x-n-1,-1):
                if (x,y)in surf:0/0
                surf[(x,y)]=1
                #print(f" x={x} y={y},", end='')
                m[y][x]=BOUNDARY
            #print()
        elif d==U:
            #print(f"U {n} x0={x} y0={y}")
            for y in range(y-1,y-n-1,-1):
                if (x,y)in surf:0/0
                surf[(x,y)]=1
                #print(f" x={x} y={y},", end='')
                m[y][x]=BOUNDARY
            #print()
    print(f"last x,y={x,y}")
    return m,pos,surf
def parse(inp:str,part=0)->list:
    res=[]
    for s in inp.splitlines():
        d,n,c=s.split(" ")
        n=int(n)
        if part==1:
            #print(f"c={c}")
            n=int("0x"+c[2:7],16)
            #print(f"n={n}")
            match int(c[7:8]):
                case 0:d=R
                case 1:d=D
                case 2:d=L
                case 3:d=U
            c=c[1:-1]
        res+=[[d,n,c]]
    return res
def disp(m:list,text="DISP"):
    print(f"\n{text} ==============")
    h=len(m)
    w=len(m[0])
    for j,r in enumerate(m):
        for i,c in enumerate(r):
            print(c,end='')
        print()
def dump(m:list,pos,fil="dump.ppm"):
    h=len(m)
    w=len(m[0])
    with open(fil,"wt") as f:
        print("P3", file=f)
        print(f"{w} {h}", file=f)
        print("255", file=f)
        for j,r in enumerate(m):
            for i,c in enumerate(r):
                v=((j%2)+(i%2))*50+50
                if c==BOUNDARY:
                    r=100;g=100;b=200
                elif c==INTERIOR:
                    r=100;g=200;b=000
                else:
                    r=v;g=v;b=v
                if (i,j)==pos:r=255;b=100
                print(f"{r} {g} {b}", file=f)
            print("", file=f)
class T000(unittest.TestCase):
    def Ztest_0111(self):
        self.assertEqual(RES011+0,compute(parse(INP01)))
    def Ztest_0120(self):
        INP012=r"""U 1 #70c710
R 1 #70c710
D 2 #70c710
R 1 #70c710
D 2 #70c710
L 3 #70c710
U 1 #70c710
L 1 #70c710
U 1 #70c710
R 1 #70c710
U 1 #70c710
R 1 #70c710
"""
        self.assertEqual(+0,compute(parse(INP012)))
    def Ztest_0110(self):
        INP011=r"""U 1 #70c710
R 1 #70c710
D 2 #70c710
R 1 #70c710
D 2 #70c710
L 3 #70c710
U 1 #70c710
L 1 #70c710
U 1 #70c710
R 1 #70c710
U 1 #70c710
R 1 #70c710
"""
        self.assertEqual(19+0,compute(parse(INP011)))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def Ztest_0210(self):
        res=parse(INP01,part=1)
        print(f"res={res}")
        print(f"RES={RES021}")
        self.assertEqual(RES021,res)
    def Ztest_0200(self):
        self.assertEqual(RES02+0*1000,compute(parse(INP01,part=1),part=1))
    def Ztest_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read(),part=1),part=1))
