res0 = 12
res1 = 271
res0_2 = 4
res1_2 = 153
def manh(a,b):
    n=0
    if a!=b:
        delta=b-a
        step=delta//abs(delta)
        for i in range(a,b,step):n+=1
    return n
# returns manhattan distance between coords
def manhattan(coord1:tuple, coord2=(0,0))->int:
    return manh(coord1[1],coord2[1])+manh(coord1[0],coord2[0])
def cnt2(s):
    p=[0,0]
    d=N
    seen=set()
    first=None
    for i in s.split(", "):
        c=i[0]
        n=int(i[1:])
        d={N:{R:E,L:W},E:{L:N,R:S},S:{R:W,L:E},W:{L:S,R:N}}[d][c]
        #print(f"c={c} n={n} d={d}")
        if d==N:
            for j in range(n):
                p[1]+=1
                if not first:
                    if tuple(p)not in seen:seen.add(tuple(p))
                    else:first=manhattan(p)
        elif d==E:
            for j in range(n):
                p[0]+=1
                if not first:
                    if tuple(p)not in seen:seen.add(tuple(p))
                    else:first=manhattan(p)
        elif d==S:
            for j in range(n):
                p[1]-=1
                if not first:
                    if tuple(p)not in seen:seen.add(tuple(p))
                    else:first=manhattan(p)
        elif d==W:
            for j in range(n):
                p[0]-=1
                if not first:
                    if tuple(p)not in seen:seen.add(tuple(p))
                    else:first=manhattan(p)
        else: raise Exception("d={d}")
    return manhattan((0,0),p),first
def cnt(s):return cnt2(s)[0]
def load(name):return open(name,"rt").read()
import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_000(self):
        self.assertEqual(0,0)
    def test_001(self):
        self.assertEqual(5,manhattan((2,3)))
    def test_100(self):
        self.assertEqual(res0,cnt("R5, L5, R5, R3\n"))
    def test_101(self):
        self.assertEqual(res0,cnt(load("input0")))
    def test_110(self):
        self.assertEqual(res1,cnt(load("input1")))
    def test_200(self):
        self.assertEqual(res0_2,cnt2("R8, R4, R4, R8\n")[1])
    def test_210(self):
        self.assertEqual(res1_2,cnt2(load("input1"))[1])
N='N';E='E';S='S';W='W';R='R';L='L'
