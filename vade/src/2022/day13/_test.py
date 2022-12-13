m0=[
[
[1,1,3,1,1],
[1,1,5,1,1]
],
[
[[1],[2,3,4]],
[[1],4]
],
[
[9],
[[8,7,6]]
],
[
[[4,4],4,4],
[[4,4],4,4,4]
],
[
[7,7,7,7],
[7,7,7]
],
[
[],
[3]
],
[
[[[]]],
[[]]
],
[
[1,[2,[3,[4,[5,6,7]]]],8,9],
[1,[2,[3,[4,[5,6,0]]]],8,9]
]
]
m0_20=[
[1,1,3,1,1],
[1,1,5,1,1],
[[1],[2,3,4]],
[[1],4],
[9],
[[8,7,6]],
[[4,4],4,4],
[[4,4],4,4,4],
[7,7,7,7],
[7,7,7],
[],
[3],
[[[]]],
[[]],
[1,[2,[3,[4,[5,6,7]]]],8,9],
[1,[2,[3,[4,[5,6,0]]]],8,9],
]
m0_2=[
[],
[[]],
[[[]]],
[1,1,3,1,1],
[1,1,5,1,1],
[[1],[2,3,4]],
[1,[2,[3,[4,[5,6,0]]]],8,9],
[1,[2,[3,[4,[5,6,7]]]],8,9],
[[1],4],
[[2]],
[3],
[[4,4],4,4],
[[4,4],4,4,4],
[[6]],
[7,7,7],
[7,7,7,7],
[[8,7,6]],
[9],
]
def parse(inp:str)->list:
    m=[]
    lines=inp.splitlines()
    i=0
    while i < len(lines):
        l=eval(lines[i])
        i+=1
        r=eval(lines[i])
        m+=[[l,r]]
        i+=1
        i+=1
    return m
def parse2(inp:str)->list:
    m=[]
    for l in inp.splitlines():
        if l=="":
            continue
        m+=[eval(l)]
    return m

def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):
        mat+=[row.copy()]
    return mat

ino=1;unk=0;nio=-1
# 1 : in order ino
# 0 : unknown unk
# -1 : not in order nio
def in_order(l, r, depth=0)->int:
    ret=unk
    s=" "*depth*2
    s2=" "*(depth+1)*2
    #print(f"{s}- Compare {l} vs {r}")
    if type(l)==int and type(r)==int:
        if l<r:
            #print(f"{s2}- Left side is smaller, so inputs are in the right order")
            return ino
        elif l>r:
            #print(f"{s2}- Right side is smaller, so inputs are not in the right order")
            return nio
        else:
            return unk
    if type(l)!=list:
        #print(f"listifying l={l}")
        l=[l]
        #print(f"{s2}- Mixed types; convert left to {l} and retry comparison")
        return in_order(l,r, depth+1)
    if type(r)!=list:
        #print(f"listifying r={r}")
        r=[r]
        #print(f"{s2}- Mixed types; convert right to {r} and retry comparison")
        return in_order(l,r, depth+1)
    #print(f"l={l} len(l)={len(l)} r={r} len(r)={len(r)}")
    i=-1
    for i in range(len(l)):
        if i >= len(r):
            #print(f"l bigger than r, returning nio")
            #print(f"{s2}- Right side ran out of items, so inputs are not in the right order")
            return nio
        tmp = in_order(l[i],r[i], depth+1)
        if tmp!=unk:
            return tmp
    #print(f"i={i} len(r)={len(r)}")
    if i<len(r)-1:
        #print(f"{s2}- Left side ran out of items, so inputs are in the right order")
        ret=ino
    return ret

def calc(m:list)->int:
    c=0
    i=1
    for l,r in m:
        #print(f"== Pair {i} ==")
        ret = in_order(l,r, 0)
        #print(f"i={i} l={l} r={r} in_order returned {ret}")
        if ret==ino:
            #print(f"Adding index {i} ======")
            c+=i
        print()
        i+=1
    return c

def sort2(m:list)->list:
    s=[m[0]]
    for i in range(1,len(m)):
        for j in range(len(s)):
            #print(f"Comparing {s[j]} vs {m[i]} s={s} i={i} j={j}")
            if in_order(s[j], m[i], 0) == nio:
                if m[i] not in s:
                    #print(f"Inserting {m[i]} at {j}")
                    s.insert(j,m[i])
                continue
        if m[i] not in s:
            s.append(m[i])
            #print(f"Appending {m[i]}")
        else:
            #print(f"Skipping {m[i]}?")
            pass
    return s

def sort2_(m:list)->list:
    return sorted(m)

def run1(inp:str)->int:
    m=parse(inp)
    c=calc(m)
    return c

def run2(inp:str)->int:
    m=parse2(inp)
    m+=[[[2]]]
    m+=[[[6]]]
    s=sort2(m)
    #print(f"Sorted list is: {s}")
    for e in s:
        #print(f"{e}")
        pass
    i=s.index([[2]])+1
    #print(f"Index of [[2]] is {i}")
    j=s.index([[6]])+1
    #print(f"Index of [[6]] is {j}")
    c=i*j
    return c

import unittest
def load(name):return open(name,"rt").read()
res0 = 13
res1 = 5580
res0_2 = 140
res1_2 = 26200
class T1(unittest.TestCase):
#class T1():
    def test_10(self):
        self.assertEqual(unk, in_order(0,0))
    def test_11(self):
        self.assertEqual(ino, in_order(0,1))
    def test_12(self):
        self.assertEqual(nio, in_order(1,0))
    def test_20(self):
        self.assertEqual(unk, in_order([0],0))
    def test_21(self):
        self.assertEqual(ino, in_order(0,[1]))
    def test_22(self):
        self.assertEqual(nio, in_order([1],[0]))
    def test_30(self):
        self.assertEqual(unk, in_order([0,1],[0,1]))
    def test_31(self):
        self.assertEqual(ino, in_order([0,1],[0,1,2]))
    def test_32(self):
        self.assertEqual(nio, in_order([0,1,2],[0,1]))
    def test_140(self):
        self.assertEqual(res0, calc(m0))
    def test_50(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_60(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_61(self):
        inp0=load("input0")
        self.assertEqual(m0_20, parse2(inp0))
class T2(unittest.TestCase):
#class T2():
    def test_62(self):
        self.assertEqual([1, 2, 3, 4], sort2([1, 3, 2, 4]))
    def test_63(self):
        self.assertEqual([[1], [2], [3], [4]], sort2([[1], [3], [2], [4]]))
    def test_64(self):
        self.assertEqual([[[8, 7, 6]], [9]], sort2([[9], [[8, 7, 6]]]))
    def test_64(self):
        self.assertEqual([[[2]], [[8, 7, 6]], [9]], sort2([[9], [[8, 7, 6]]]+[[[2]]]))
    def test_65(self):
        self.assertEqual([[[2]], [[6]], [[8, 7, 6]], [9]], sort2([[9], [[8, 7, 6]]]+[[[2]]]+[[[6]]]))
    def test_66(self):
        self.assertEqual(m0_2, sort2(m0_20+[[[6]]]+[[[2]]]))
    def test_67(self):
        self.assertEqual([[[6]], [[2]]], parse2("[[6]]\n[[2]]\n"))
    def test_68(self):
        self.assertEqual([[[0]], [[1]], [[2]], [[6]]], sort2(parse2("[[6]]\n[[1]]\n[[2]]\n[[0]]\n")))
    def test_69(self):
        self.assertEqual(12, run2("[[6]]\n[[1]]\n[[2]]\n[[0]]\n"))
    def test_70(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_80(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
