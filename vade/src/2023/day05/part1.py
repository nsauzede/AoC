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
RES02=46
#RES2=1561682361 # too high
RES2=0
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
                #print(f"z={z}")
                a+=[z]
    if section:
        print(f"section={section} a={a}")
        d[section]=a
        section=""
    #print(f"d={d}")
    return d

def trans(n, m)->int:
    for (d,s,l) in m:
        #print(f"d={s} s={s} l={l}")
        if n>=s and n<s+l:
            return n-s+d
    return n
def trans2(t00, m)->list:
    print(f"t00={t00} m={m}")
    res0=[]
    for t0 in t00:
        print(f"t0={t0}")
        (n0, l0)=t0
        res=[]
        for (d,s,l) in m:
            print(f"d={d} s={s} l={l} - n0={n0} l0={l0}")
            if n0<=s:
                print(f"n0 before s")
                if n0+l0>=s:
                    print(f"l0 after s")
                    if n0+l0>=s+l:
                        print(f"l0 after l")
                        res += [[s,l]]
                    else:
                        print(f"l0 before l")
                        res += [[s,n0+l0-s]]
                else:
                    print(f"l0 before s")
                    #res+=[[n0,l0]]
            elif n0 < s+l:
                print(f"n0 before l")
                if n0+l0>=s+l:
                    res+=[[n0,s+l-n0]]
                else:
                    res+=[[n0-s+d,l0]]
            else:
                print(f"n0 after l")
                #res+=[[n0,l0]]
        if res==[]:
            res=[t0]
        res0+=res
    print(f"res={res}")
    return res
def compute(d,part=0):
    minres=9999999999
    seeds=d['seeds']
    print(f"seeds={seeds} before")
    if part==0:
        nseeds=[]
        for s in seeds:
            nseeds+=[s]
            nseeds+=[1]
        seeds=nseeds
    print(f"seeds={seeds} after")
    for i in range(len(seeds)//2):
        #print(f"i={i} seeds={seeds}")
        tupl = seeds[2*i:2*i+2]
        print(f"i={i} seeds[2*i:2]={tupl}")
        s,l = tupl
        for s in range(s,s+l):
            print(f"s={s}")
            res=trans(s,d["seed-to-soil"])
            #print(res)
            res=trans(res,d["soil-to-fertilizer"])
            #print(res)
            res=trans(res,d["fertilizer-to-water"])
            #print(res)
            res=trans(res,d["water-to-light"])
            #print(res)
            res=trans(res,d["light-to-temperature"])
            #print(res)
            res=trans(res,d["temperature-to-humidity"])
            #print(res)
            res=trans(res,d["humidity-to-location"])
            #print(res)
            if res<minres:
                minres=res
            print(f"res={res} minres={minres}")
    return minres
import unittest
class T000(unittest.TestCase):
    def Ztest_trans000(self):
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
    def Ztest_trans2000(self):
        res=trans2([79,1],d["seed-to-soil"])
        self.assertEqual([[79,1]],res)
    def Ztest_trans2001(self):
        seeds=list(range(79,79+14))
        res=[]
        for s in seeds:
            res+=[trans(s,d["seed-to-soil"])]
        print(f"seeds={seeds} res={res}")
        res=trans2([79,14],d["seed-to-soil"])
        self.assertEqual([[81,14]],res)



    def check_soil(self,expected_res2,r, d):
        seeds=list(range(r[0],r[0]+r[1]))
        res1=[]
        for s in seeds:
            res1+=[trans(s,d["seed-to-soil"])]
        res=trans2(r,d["seed-to-soil"])
        res2=[]
        for l in res:
            res2+=list(range(l[0],l[0]+l[1]))
        assert res1==res2
        self.assertEqual(expected_res2,res)
    def Ztest_trans2001(self):
        self.check_soil([[81,14]], [79,14], d)
    def Ztest_trans2002(self):
        self.check_soil([[57,13]], [55,13], d)

    def check2(self,expected_res2,r, d):
        seeds=list(range(r[0],r[0]+r[1]))
        res1=[]
        print(f"seeds={seeds}")
        for s in seeds:
            #print(f"s={s}")
            res10=trans(s,d["seed-to-soil"])
            #print(f"res10={res10}")
            res10=trans(res10,d["soil-to-fertilizer"])
            res1+=[res10]
        print(f"res1={res1}")
        res0=trans2([r],d["seed-to-soil"])
        res=trans2(res0,d["soil-to-fertilizer"])
        res2=[]
        for l in res:
            res2+=list(range(l[0],l[0]+l[1]))
        assert res1==res2
        self.assertEqual(expected_res2,res)
    def Ztest_trans2003(self):
        self.check2([[81,14]], [79,14], d)

    def check3(self,expected_res2,r, d):
        seeds=list(range(r[0],r[0]+r[1]))
        res1=[]
        print(f"seeds={seeds}")
        for s in seeds:
            #print(f"s={s}")
            res10=trans(s,d["seed-to-soil"])
            #print(f"res10={res10}")
            res10=trans(res10,d["soil-to-fertilizer"])
            #print(f"res10={res10}")
            res10=trans(res10,d["fertilizer-to-water"])
            #print(f"res10={res10}")
            res1+=[res10]
        print(f"res1={res1}")
        res0=[r]
        res0=trans2(res0,d["seed-to-soil"])
        res0=trans2(res0,d["soil-to-fertilizer"])
        res0=trans2(res0,d["fertilizer-to-water"])
        res=res0
        res2=[]
        for l in res:
            res2+=list(range(l[0],l[0]+l[1]))
        assert res1==res2
        self.assertEqual(expected_res2,res)
    def Ztest_trans2030(self):
        self.check3([[81,14]], [79,14], d)

    def check4(self,expected_res2,r, d):
        seeds=list(range(r[0],r[0]+r[1]))
        res1=[]
        print(f"seeds={seeds}")
        for s in seeds:
            #print(f"s={s}")
            res10=trans(s,d["seed-to-soil"])
            #print(f"res10={res10}")
            res10=trans(res10,d["soil-to-fertilizer"])
            #print(f"res10={res10}")
            res10=trans(res10,d["fertilizer-to-water"])
            #print(f"res10={res10}")
            res10=trans(res10,d["water-to-light"])
            #print(f"res10={res10}")
            res1+=[res10]
        print(f"res1={res1}")
        res0=[r]
        res0=trans2(res0,d["seed-to-soil"])
        res0=trans2(res0,d["soil-to-fertilizer"])
        res0=trans2(res0,d["fertilizer-to-water"])
        res0=trans2(res0,d["water-to-light"])
        res=res0
        res2=[]
        for l in res:
            res2+=list(range(l[0],l[0]+l[1]))
        assert res1==res2
        #self.assertEqual(expected_res2,res)
    def Ztest_trans2040(self):
        self.check4([[81,14]], [79,14], d)

    def trans(self,rseeds,d):
        res=[]
        seeds=[]
        for r in rseeds:
            seeds+=list(range(r[0],r[0]+r[1]))
        for s in seeds:
            r=s
            r=trans(r,d["seed-to-soil"])
            r=trans(r,d["soil-to-fertilizer"])
            r=trans(r,d["fertilizer-to-water"])
            r=trans(r,d["water-to-light"])
            r=trans(r,d["light-to-temperature"])
            r=trans(r,d["temperature-to-humidity"])
            r=trans(r,d["humidity-to-location"])
            res+=[[r,1]]
        return res

    def Ztest_trans9000(self):
        #res=self.trans([79, 14, 55, 13],d)
        res=[[79, 1],[14, 1],[55, 1],[13,1]]
        res=self.trans(res,d)
        #self.assertEqual([81, 14, 57, 13],res)
        #self.assertEqual([81, 53, 57, 52],res)
        #self.assertEqual([81, 49, 53, 41],res)
        #self.assertEqual([74, 42, 46, 34],res)
        #self.assertEqual([78, 42, 82, 34],res)
        #self.assertEqual([78, 43, 82, 35],res)
        self.assertEqual([[82,1], [43,1], [86,1], [35,1]],res)

    def trans2(self,rseeds,d):
        res=[]
        for r in rseeds:
            r=[r]
            print(f"r={r}")
            r=self.trans20(r,d["seed-to-soil"]);print(f"r={r}")
            #r=self.trans20(r,d["soil-to-fertilizer"]);print(f"r={r}")
            #r=trans2(r,d["fertilizer-to-water"])
            #r=trans2(r,d["water-to-light"])
            #r=trans2(r,d["light-to-temperature"])
            #r=trans2(r,d["temperature-to-humidity"])
            #r=trans2(r,d["humidity-to-location"])
            res+=r
        return res

    def Ztest_trans9001(self):
        res=[[79, 1],[14, 1],[55, 1],[13,1]]
        res=self.trans2(res,d)
        self.assertEqual([[81,1], [14,1], [57,1], [13,1]],res)
        #self.assertEqual([[81,1], [53,1], [57,1], [52,1]],res)
        #self.assertEqual([[82,1], [43,1], [86,1], [35,1]],res)

    def trans20(self,t00, m)->list:
        print(f"t00={t00} m={m}")
        res0=[]
        for t0 in t00:
            print(f"t0={t0}")
            (n0, l0)=t0
            res=[]
            for (d,s,l) in m:
                print(f"d={d} s={s} l={l} - n0={n0} l0={l0}")
                if n0<s:
                    print(f"n0 before s")
                    if n0+l0-1<s:
                        print(f"l0 before s")
                        res += [[n0,l0]]
                    elif n0+l0-1<=s+l-1:
                        print(f"l0 before l")
                        res += [[s,n0+l0-s]]
                        res += [[s,n0+l0-s]]
                        #res += [n0,l0]
                    else:
                        print(f"l0 after l")
                        res += [[s,l]]
                elif n0 < s+l-1:
                    print(f"n0 before l")
                    if n0+l0>=s+l:
                        res += [[n0,s+l-n0]]
                    else:
                        res += [[n0-s+d,l0]]
                else:
                    print(f"n0 after l")
                    #res+=[[n0,l0]]
            if res==[]:
                res=[t0]
            print(f"res={res}")
            res0+=res
        print(f"res0={res0}")
        return res0

    def Ztest_trans2002(self):
        r=[55,13]
        expected_res2=[[57,13]]
        seeds=list(range(r[0],r[0]+r[1]))
        res1=[]
        for s in seeds:
            res1+=[trans(s,d["seed-to-soil"])]
        print(f"seeds={seeds} res1={res1}")
        res=trans2(r,d["seed-to-soil"])
        res2=list(range(res1[0],res1[0]+res1[1]))
        assert res1==res2
        self.assertEqual(expected_res2,res)
    def Ztest_compute000(self):
        res=compute(d)
        self.assertEqual(RES01,res)
    def test_part1000(self):
        res=compute(parse(INP01))
        self.assertEqual(RES01,res)
    def test_part1001(self):
        res=compute(parse(open("input1","rt").read()))
        self.assertEqual(RES1,res)
    def Ztest_part2000(self):
        d=parse(INP01)
        print(d["seeds"])
        res=compute(d,1)
        self.assertEqual(RES02,res)
    def Ztest_part2001(self):
        res=compute(parse(open("input1","rt").read()),1)
        self.assertEqual(RES2,res)
