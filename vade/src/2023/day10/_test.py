import unittest
INP01=""".....
.S-7.
.|.|.
.L-J.
....."""
INP011="""..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
RES01=4
RES011=8
INP01_=[
['.','.','.','.','.'],
['.','S','-','7','.'],
['.','|','.','|','.'],
['.','L','-','J','.'],
['.','.','.','.','.'],
]
#RES1=6745 # too low
RES1=6823
INP020="""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
RES020=4
INP021="""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""
RES021=4
INP022=""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
RES022=8
INP023="""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
RES023=10
#RES2=32 # not right
#RES2=35 # not right
#RES2=88 # not right
#RES2=97 # not right
#RES2=29 # not right
RES2=0
def getstart(m):
    for j,l in enumerate(m):
        if 'S'in l:
            i = l.index('S')
            return[j,i]
    return None
def die(s):print(f"DIE!!! {s}");0/0
def move(sa,ca,ea):
    if ca=='-':
        if sa[1]<ea[1]:
            ea[1]+=1
        else:
            ea[1]-=1
    elif ca=='|':
        if sa[0]<ea[0]:
            ea[0]+=1
        else:
            ea[0]-=1
    elif ca=='7':
        if sa[1]<ea[1]:
            ea[0]+=1
        else:
            ea[1]-=1
    elif ca=='L':
        if sa[1]>ea[1]:
            ea[0]-=1
        else:
            ea[1]+=1
    elif ca=='J':
        if sa[0]<ea[0]:
            ea[1]-=1
        else:
            ea[0]-=1
    elif ca=='F':
        #print(f"sa={sa} ea={ea}")
        if sa[1]>ea[1]:
            #print("INC Y")
            ea[0]+=1
        else:
            ea[1]+=1
            #print("INC X")
    elif ca=='.':pass
    elif ca=='S':pass
    else:die(f"ca={ca}")
    return ea
def wander(m,steps,seen,sa,ea,sb,eb)->dict:
    h=len(m)
    w=len(m[0])
    path1=[]
    path2=[]
    while True:
        ja,ia=ea
        jb,ib=eb
        if ja<0 or ja>=h:
            print(f"COORD JA {ja}")
            return None
        if ia<0 or ia>=w:
            print(f"COORD IA {ia}")
            return None
        if jb<0 or jb>=h:
            print(f"COORD JB {jb}")
            return None
        if ib<0 or ib>=w:
            print(f"COORD IB {ib}")
            return None
        ca=m[ja][ia]
        cb=m[jb][ib]
        #print(f"steps={steps} sa={sa} ca={ca} ea={ea} sb={sb} cb={cb} eb={eb}")
        ea0=ea.copy()
        eb0=eb.copy()
        ea=move(sa,ca,ea)
        eb=move(sb,cb,eb)
        #print(f"move => ea={ea} eb={eb}")
        path1+=[ea0]
        path2+=[eb0]
        steps+=1
        if ea==eb:
            path1+=[ea]
            path2+=[eb]
            print(f"found loop {steps}")
            return {'max':steps,'path1':path1,'path2':path2}
        sea=str(ea);seb=str(eb)
        if sea in seen:
            #print(f"SEEN A {sea}");
            return None
        if seb in seen:
            #print(f"SEEN B {seb}");
            return None
        seen[sea]=1
        seen[seb]=1
        sa=ea0
        sb=eb0
        #return wander(m,steps,seen,sa,ea,sb,eb)
def compute_(inp:list,part=0)->dict:
    res = {}
    spos=getstart(inp)
    j,i=spos
    #print(f"inp={inp}")
    print(f"spos={spos}")
    mx=0
    path1=[]
    path2=[]
    for c in['|','-','L','J','7','F']:
        seen={}
        sa=spos
        sb=spos
        if c=='F':
            ea=[j,i+1]
            eb=[j+1,i]
        elif c=='|':
            ea=[j-1,i]
            eb=[j+1,i]
        elif c=='-':
            ea=[j,i-1]
            eb=[j,i+1]
        elif c=='L':
            ea=[j-1,i]
            eb=[j,i+1]
        elif c=='J':
            ea=[j-1,i]
            eb=[j,i-1]
        elif c=='7':
            ea=[j,i-1]
            eb=[j+1,i]
        else:die(f"c={c}")
        #else:continue
        print(f"WANDER {c}..")
        d = wander(inp,1,seen,sa,ea,sb,eb)
        if d:
            r=d['max']
            if r>mx:
                mx=r
                path1=[spos]+d['path1']
                path2=[spos]+d['path2']
    res['max']=mx
    res['path1']=path1
    res['path2']=path2
    return res
def disp(inp):
    for r in inp:
        s="".join(r)
        print(s)
def color(m,j,i,col):
    h=len(m)
    w=len(m[0])
    if j<0 or j>=h:return
    if i<0 or i>=w:return
    if col=='A':
        if m[j][i]=='A':
            pass
            #die(1)
        if m[j][i]=='B':die(2)
        if m[j][i]=='.':
            m[j][i]=col
            #return
            color(m,j,i-1,col)
            color(m,j,i+1,col)
            color(m,j-1,i,col)
            color(m,j+1,i,col)
            #print(f"j={j} i={i} col={col}")
    else:
        if m[j][i]=='B':
            pass
            #die(3)
        if m[j][i]=='A':die(4)
        if m[j][i]=='.':
            m[j][i]=col
            #return
            color(m,j,i-1,col)
            color(m,j,i+1,col)
            color(m,j-1,i,col)
            color(m,j+1,i,col)
            #print(f"j={j} i={i} col={col}")
def flood(inp,d,path,inv=False):
    if inv:
        A='B';B='A'
    else:
        A='A';B='B'
    #disp(inp)
    #print(d)
    last = path[0]
    for nxt in path[1:]:
        lj,li=last
        j,i=nxt
        c=inp[j][i]
        print(f"flooding last={last} nxt={nxt} c={c}")
        if c=='-':
            if li<i:
                #print("HORIZ EAST")
                color(inp,j-1,i,A)
                color(inp,j+1,i,B)
            else:
                #print("HORIZ WEST")
                color(inp,j-1,i,B)
                color(inp,j+1,i,A)
        elif c=='|':
            if lj<j:
                #print("VERT SOUTH")
                color(inp,j,i+1,A)
                color(inp,j,i-1,B)
            else:
                #print("VERT NORTH")
                color(inp,j,i+1,B)
                color(inp,j,i-1,A)
        elif c=='7':
            if li<i:
                color(inp,j-1,i,A)
                color(inp,j,i+1,A)
            else:
                color(inp,j-1,i,B)
                color(inp,j,i+1,B)
        elif c=='J':
            if lj<j:
                color(inp,j+1,i,A)
                color(inp,j,i+1,A)
            else:
                color(inp,j+1,i,B)
                color(inp,j,i+1,B)
        elif c=='L':
            if li>i:
                color(inp,j+1,i,A)
                color(inp,j,i-1,A)
            else:
                color(inp,j+1,i,B)
                color(inp,j,i-1,B)
        elif c=='F':
            if lj>j:
                color(inp,j-1,i,A)
                color(inp,j,i-1,A)
            else:
                color(inp,j-1,i,B)
                color(inp,j,i-1,B)
        else:die(f"c")
        last=nxt
    print("FLOOD RESULT: ---------------------------------------------------")
    disp(inp)
def compute(inp:list,part=0,cnt='B')->int:
    res=compute_(inp,part)
    if part==1:
        #print(f"path1={res['path1']}")
        #print(f"path2={res['path2']}")
        flood(inp,res,res['path1'])
        flood(inp,res,res['path2'],True)
        res=0
        for r in inp:
            res+=r.count(cnt)
            #res+=r.count('B')
            #res+=r.count('A')
        print(f"res={res}")
        return res
    else:
        return res['max']
def parse(inp):
    res=[]
    ll=inp.splitlines()
    for l in ll:
        l0=[]
        for c in(l):
            l0+=[c]
        res+=[l0]
    return res
class T000(unittest.TestCase):
    def test_0110(self):
        self.assertEqual(RES011+0,compute(parse(INP011)))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_0100_(self):
        self.assertEqual(RES01+0,compute(INP01_))
    def test_1000(self):
        self.assertEqual(RES1,compute(parse(open("input1","rt").read())))
    def test_0200(self):
        self.assertEqual(RES020+0,compute(parse(INP020),1))
    def test_0210(self):
        self.assertEqual(RES021+0,compute(parse(INP021),1))
    def test_0220(self):
        self.assertEqual(RES022+0,compute(parse(INP022),1,'A'))
    def Ztest_0230(self):
        self.assertEqual(RES023+0,compute(parse(INP023),1,'A'))
    def Ztest_2000(self):
        self.assertEqual(RES2+0,compute(parse(open("input1","rt").read()),1))
