def mkmat(row=[1,2,3],count=3)->list:
    mat=[]
    for i in range(count):mat+=[row.copy()]
    return mat
def load(name):return open(name,"rt").read()
def mapstr(m:list)->str:return "\n".join(["".join(str(i) for i in sublist) for sublist in m])+"\n"
def rowstr(r:list, w=28)->str:return "".join(r)[:w]
def strmap(inp:str)->list:
    return [[c for c in s] for s in inp.split("\n")][:-1]
def draw(m:list):print(mapstr(m))

def browse_first(l:dict, s:dict, k:str):
    s["minute"]+=1
    print(f"== Minute {s['minute']} == in {k}")
    if s["minute"]>=31:
        print(f"CUR_PRESSURES={s['cur_pressures']}")
        return
    rate=l[k]["rate"]
    #print(" ", end="")
    if len(s["open"]) == 0:
        print("No valves are open.")
    else:
        n=0
        ov=[]
        for e in s["open"].items():
            #print(f"e={e}")
            if e[1]>0:
                #print(f"+{e[0]}",end="")
                n+=e[1]
                ov+=[e[0]]
        #print(f"={n}", end="")
        s["cur_pressures"]+=n
        print(f"Valves {ov} are open, releasing {n} pressure.")
    next_k = k
    if rate>0 and k not in s["open"]:
        #print(f" OPEN {k}", end="")
        print(f"You open valve {k}.")
        s["open"][k]=rate
    else:
        next_k = l[k]["tunnels"][0]
        print(f"You move to valve {next_k}.")
    print()
    browse_first(l,s, next_k)

res0 = 1651
res1 = 0
res0_2 = 0
res1_2 = 0
import copy
import unittest
#@unittest.skip
class T110(unittest.TestCase):
    def Ztest_100(self):
        l=copy.deepcopy(layout00)
        stat={
        "minute":0,
        "cur_pressures":0,
        "total_pressures":[],
        "open":{},
        }
        browse_first(l,stat,"AA")
        self.assertEqual(-1,0)
    def Ztest_110(self):
        l=copy.deepcopy(layout00)
        l["AA"]["rate"]+=10
        rate=l["AA"]["rate"]
        print(f"rate={rate}")
        self.assertEqual(10,rate)
    def Ztest_120(self):
        l=copy.deepcopy(layout00)
        l["AA"]["rate"]+=100
        rate=l["AA"]["rate"]
        print(f"rate={rate}")
        self.assertEqual(100,rate)

#@unittest.skip
class T010(unittest.TestCase):
    def test_010(self):
        l=copy.deepcopy(layout00_)
        l[0][0]+=10
        rate=l[0][0]
        print(f"rate={rate}")
        self.assertEqual(10,rate)
    def test_020(self):
        l=copy.deepcopy(layout00_)
        l[0][0]+=100
        rate=l[0][0]
        print(f"rate={rate}")
        self.assertEqual(100,rate)

def parse(s:str)->list:
    scan=[]
    for line in s.splitlines():
        pass
    return scan
inp00="""\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
layout00={
"AA":{"rate":0, "tunnels":["DD", "II", "BB"]},
"BB":{"rate":13, "tunnels":["CC", "AA"]},
"CC":{"rate":2, "tunnels":["DD", "BB"]},
"DD":{"rate":20, "tunnels":["CC", "AA", "EE"]},
"EE":{"rate":3, "tunnels":["FF", "DD"]},
"FF":{"rate":0, "tunnels":["EE", "GG"]},
"GG":{"rate":0, "tunnels":["FF", "HH"]},
"HH":{"rate":22, "tunnels":["GG"]},
"II":{"rate":0, "tunnels":["AA", "JJ"]},
"JJ":{"rate":21, "tunnels":["II"]}
}
layout00_=[
[0, [3,8,1]],
[13, [2, 0]],
[2, [3, 1]],
[20, [2, 0, 4]],
[3, [5, 3]],
[0, [4, 6]],
[0, [5, 7]],
[22, [6]],
[0, [0, 9]],
[21, [8]],
]
