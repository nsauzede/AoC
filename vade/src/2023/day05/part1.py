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
RES01=35
RES1=227653707
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
                print(f"z={z}")
                a+=[z]
    if section:
        d[section]=a
        section=""
    print(f"d={d}")
    return d

def trans(n, m)->int:
    for (d,s,l) in m:
        if n>=s and n<s+l:
            return n-s+d
    return n
def compute(d):
    print(f"seeds={d['seeds']}")
    minres=9999999999
    for s in d['seeds']:
        print(f"s={s}")
        res=trans(s,d["seed-to-soil"])
        print(res)
        res=trans(res,d["soil-to-fertilizer"])
        print(res)
        res=trans(res,d["fertilizer-to-water"])
        print(res)
        res=trans(res,d["water-to-light"])
        print(res)
        res=trans(res,d["light-to-temperature"])
        print(res)
        res=trans(res,d["temperature-to-humidity"])
        print(res)
        res=trans(res,d["humidity-to-location"])
        print(res)
        if res<minres:minres=res
        print(f"res={res} minres={minres}")
    return minres
import unittest
class T000(unittest.TestCase):
    def test_trans000(self):
        res=trans(79,d["seed-to-soil"])
        self.assertEqual(81,res)
        res=trans(res,d["soil-to-fertilizer"])
        self.assertEqual(81,res)
        res=trans(res,d["fertilizer-to-water"])
        self.assertEqual(81,res)
        res=trans(res,d["water-to-light"])
        self.assertEqual(74,res)
        res=trans(res,d["light-to-temperature"])
        self.assertEqual(78,res)
        res=trans(res,d["temperature-to-humidity"])
        self.assertEqual(78,res)
        res=trans(res,d["humidity-to-location"])
        self.assertEqual(82,res)
    def test_compute000(self):
        res=compute(d)
        self.assertEqual(RES01,res)
    def test_part1000(self):
        res=compute(parse(INP01))
        self.assertEqual(RES01,res)
    def test_part1001(self):
        res=compute(parse(open("input1","rt").read()))
        self.assertEqual(RES1,res)
