def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):
        mat+=[row.copy()]
    return mat

def parse(inp:str)->dict:
    m=[]
    for l in inp.splitlines():
        s="addx "
        if l=="noop":
            m+=[0]
        elif l.startswith(s):
            m+=[int(l.split(s)[1])]
            m+=[0]
    return m

def calc(l:list)->int:
    c=0
    print(f"l={l}")
    x=1
    cy=1
    r=[20,60,100,140,180,220]
    y=0
    for insn in l:
        if cy in r:
            strength=cy*x
            print(f"cy={cy} x={x} strength={strength}")
            c+=strength
        x+=y
        y=insn
        cy+=1
    return c

def prspr(x:int)->list:
    l=['.']*40
    for i in range(len(l)):
        if i>=x-1 and i <= x+1:
            l[i]='#'
    s="".join(l)
    print(f"Sprite position: {s}")
    return l
def calc2(l:list)->int:
    c=0
    x=1
    cy=1
    crt=0
    pos=prspr(x)
    row=[]
    img=[]
    while cy <= len(l):
        opc=l[cy-1]
        print()
        if opc==0:
            insn = "noop"
        else:
            insn = f"addx {opc}"
        print(f"Start cycle  {cy:2}: begin executing {insn}")
        print(f"During cycle {cy:2}: CRT draws pixel in position {crt} ({pos[crt]})")
        row+=[pos[crt]]
        srow="".join(row)
        print(f"Current CRT row: {srow}")
        cy+=1
        crt+=1
        if crt>=40:
            crt = 0
            img+=[row]
            row = []
        if opc==0:
            print(f"End of cycle {cy:2}: finish executing {insn}")
            continue
        print()
        x+=opc
        print(f"During cycle {cy:2}: CRT draws pixel in position {crt} ({pos[crt]})")
        row+=[pos[crt]]
        srow="".join(row)
        print(f"Current CRT row: {srow}")
        print(f"End of cycle {cy:2}: finish executing {insn} (Register X is now {x})")
        pos=prspr(x)
        cy+=1
        crt+=1
        if crt>=40:
            crt = 0
            img+=[row]
            row = []
        if cy>20:
            #break
            pass
    s=""
    for r in img:
        st=f"{''.join(r)}\n"
        print(st,end='')
        s+=st
    return s

def run1(inp:str)->int:
    m=parse(inp)
    c=calc(m)
    return c

def run2(inp:str)->int:
    m=parse(inp)
    c=calc2(m)
    return c

import unittest
def load(name):return open(name,"rt").read()
m0="""noop
addx 3
addx -5"""
res0 = 13140
res00 = 1234
res1 = 15680
res0_2 = """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
res1_2 = """\
####.####.###..####.#..#..##..#..#.###..
...#.#....#..#.#....#..#.#..#.#..#.#..#.
..#..###..###..###..####.#....#..#.#..#.
.#...#....#..#.#....#..#.#.##.#..#.###..
#....#....#..#.#....#..#.#..#.#..#.#....
####.#....###..#....#..#..###..##..#....
"""
res1_2_str = "ZFBFHGUP"
def mkrope(k:list,c:int)->list:
    l=[]
    for i in range(c):
        l+=[k.copy()]
    return l
class T1(unittest.TestCase):
    def test_10(self):
        self.assertEqual([0,3,0,-5,0], parse(m0))
    def test_50(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_60(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
class T2(unittest.TestCase):
    def test_70(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_80(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
