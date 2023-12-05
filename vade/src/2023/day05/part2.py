d={
    "seeds":[79,14,55,13],
    "seed-to-soil":[
        [50, 98, 2],
        [52,50,48]
    ],
    "soil-to-fertilizer":[
        [0, 15, 37],
        [37, 52, 2],
        [39, 0, 15],
    ],
    "fertilizer-to-water":[
        [49, 53, 8],
        [0, 11, 42],
        [42, 0, 7],
        [57, 7, 4],
    ],
    "water-to-light":[
        [88, 18, 7],
        [18, 25, 70],
    ],
    "light-to-temperature":[
        [45, 77, 23],
        [81, 45, 19],
        [68, 64, 13],
    ],
    "temperature-to-humidity":[
        [0, 69, 1],
        [1, 0, 69],
    ],
    "humidity-to-location":[
        [60, 56, 37],
        [56, 93, 4],
    ],
}

def trans(r0,m):
    res0=[]
    for r in r0:
        #print(f"r={r} m={m}")
        (n0,l0)=r
        res=[]
        for i in range(len(m)):
            if l0==0:
                break
            #print(f"n0={n0} l0={l0}")
            (d,s,l)=m[i]
            #print(f"d={d} s={s} l={l}")
            if n0<s:
                #print(f"n0 before s")
                if n0+l0-1<s:
                    #print(f"l0 before s")
                    res+=[[n0,l0]]
                    l1=l0
                    n0+=l1
                    l0-=l1
                else:
                    #print(f"l0 after s")
                    if n0+l0-1<s+l:
                        #print(f"l0 before l")
                        res+=[[n0,s-n0]]
                        l1=s-n0
                        res+=[[d,n0+l0-s]]
                        l1+=n0+l0-s
                        n0+=l1
                        l0-=l1
                    else:
                        #print(f"l0 after l")
                        res+=[[n0,s-n0]]
                        l1=s-n0
                        res+=[[d,l]]
                        l1+=l
                        n0+=l1
                        l0-=l1
            else:
                #print(f"n0 after s")
                if n0<s+l:
                    #print("n0 before l")
                    if n0+l0-1<s+l:
                        #print("l0 before l")
                        res+=[[n0-s+d,l0]]
                        l1=l0
                        n0+=l1
                        l0-=l1
                    else:
                        #print("l0 after l")
                        res+=[[n0-s+d,s+l-n0]]
                        l1=s+l-n0
                        n0+=l1
                        l0-=l1
                else:
                    #print("n0 after l")
                    pass
            #print(f"res={res}")
        if res==[]:
            res=[r]
        res0+=res
    return res0

def trans2(r,mm):
    for m in mm:
        r=trans(r,m)
    return r

def parse(s):
    d={}
    l=s.splitlines()
    #print(f"s={l[0]}")
    (u,v)=l[0].split(":")
    z=[int(x) for x in v.split(" ")[1:]]
    d["seeds"]=z
    section=""
    a=[]
    for s in l[2:]:
        #print(f"s={s}")
        if section=="":
            section=s.split(":")[0].split(" ")[0]
        else:
            if s=="":
                d[section]=a
                section=""
                a=[]
            else:
                z=[int(x) for x in s.split(" ")]
                #print(f"z={z}")
                a+=[z]
    if section:
        #print(f"section={section} a={a}")
        d[section]=a
        section=""
    #print(f"d={d}")
    return d
INP01="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

import unittest
class T000(unittest.TestCase):
    def test_trans004(self):
        d=parse(open("input1","rt").read())
        #print(f"res={d}")
        r=[[x,y]for x,y in zip(d["seeds"][::2],d["seeds"][1::2])]
        mm=[]
        mm+=[sorted(d["seed-to-soil"],key=lambda x:x[1])]
        mm+=[sorted(d["soil-to-fertilizer"],key=lambda x:x[1])]
        mm+=[sorted(d["fertilizer-to-water"],key=lambda x:x[1])]
        mm+=[sorted(d["water-to-light"],key=lambda x:x[1])]
        mm+=[sorted(d["light-to-temperature"],key=lambda x:x[1])]
        mm+=[sorted(d["temperature-to-humidity"],key=lambda x:x[1])]
        mm+=[sorted(d["humidity-to-location"],key=lambda x:x[1])]
        r=trans2(r,mm)
        minf=min(r,key=lambda x:x[0])[0]
        self.assertEqual(78775051,minf)
    def Ztest_trans003(self):
        d=parse(INP01)
        #print(f"res={d}")
        r=[[x,y]for x,y in zip(d["seeds"][::2],d["seeds"][1::2])]
        mm=[]
        mm+=[sorted(d["seed-to-soil"],key=lambda x:x[1])]
        mm+=[sorted(d["soil-to-fertilizer"],key=lambda x:x[1])]
        mm+=[sorted(d["fertilizer-to-water"],key=lambda x:x[1])]
        mm+=[sorted(d["water-to-light"],key=lambda x:x[1])]
        mm+=[sorted(d["light-to-temperature"],key=lambda x:x[1])]
        mm+=[sorted(d["temperature-to-humidity"],key=lambda x:x[1])]
        mm+=[sorted(d["humidity-to-location"],key=lambda x:x[1])]
        r=trans2(r,mm)
        minf=min(r,key=lambda x:x[0])[0]
        self.assertEqual(46,minf)
    def Ztest_trans002(self):
        r=[[82,1]]
        mm=[]
        mm+=[sorted(d["seed-to-soil"],key=lambda x:x[1])]
        mm+=[sorted(d["soil-to-fertilizer"],key=lambda x:x[1])]
        mm+=[sorted(d["fertilizer-to-water"],key=lambda x:x[1])]
        mm+=[sorted(d["water-to-light"],key=lambda x:x[1])]
        mm+=[sorted(d["light-to-temperature"],key=lambda x:x[1])]
        mm+=[sorted(d["temperature-to-humidity"],key=lambda x:x[1])]
        mm+=[sorted(d["humidity-to-location"],key=lambda x:x[1])]
        r=trans2(r,mm)
        self.assertEqual([[46,1]],r)
    def Ztest_trans001(self):
        r=[[82,1]]
        r=trans(r,sorted(d["seed-to-soil"],key=lambda x:x[1]))
        self.assertEqual([[84,1]],r)
        r=trans(r,sorted(d["soil-to-fertilizer"],key=lambda x:x[1]))
        self.assertEqual([[84,1]],r)
        r=trans(r,sorted(d["fertilizer-to-water"],key=lambda x:x[1]))
        self.assertEqual([[84,1]],r)
        r=trans(r,sorted(d["water-to-light"],key=lambda x:x[1]))
        self.assertEqual([[77,1]],r)
        r=trans(r,sorted(d["light-to-temperature"],key=lambda x:x[1]))
        self.assertEqual([[45,1]],r)
        r=trans(r,sorted(d["temperature-to-humidity"],key=lambda x:x[1]))
        self.assertEqual([[46,1]],r)
        r=trans(r,sorted(d["humidity-to-location"],key=lambda x:x[1]))
        self.assertEqual([[46,1]],r)
        #0/0
    def Ztest_trans000(self):
        d0=sorted(d["seed-to-soil"],key=lambda x:x[1])
        self.assertEqual([[84,1]],trans([[82,1]],d0))
        self.assertEqual([[48,2]],trans([[48,2]],d0))
        self.assertEqual([[52,2]],trans([[50,2]],d0))
        self.assertEqual([[0,50]],trans([[0,50]],d0))
        self.assertEqual([[0,50],[52,1]],trans([[0,51]],d0))
        self.assertEqual([[52,48]],trans([[50,48]],d0))
        self.assertEqual([[0,50],[52,48],[50,2]],trans([[0,100]],d0))
        self.assertEqual([[98,2],[50,1]],trans([[96,3]],d0))
        self.assertEqual([[50,1]],trans([[98,1]],d0))
        self.assertEqual([[51,1]],trans([[99,1]],d0))
        self.assertEqual([[50,2]],trans([[98,2]],d0))
        self.assertEqual([[98,2],[50,1]],trans([[96,3]],d0))
        #0/0

def foo():
    ranges=[[82, 1]]
    res=trans(ranges[0], d["seed-to-soil"])
    print(f"ranges={ranges} res={res}")
    assert [[84, 1]] == res
