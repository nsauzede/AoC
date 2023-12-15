import unittest
INP01="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""
RES01=1320
RES1=510801
RES02=145
RES2=212763
def compute0(s:str,part=0)->int:
    cur=0
    for c in s:
        if c=="\n":continue
        cur+=ord(c)
        cur*=17
        cur%=256
    return cur
def compute(l:list,part=0)->int:
    if part==1:return compute1(l)
    res=0
    for step in l:
        res+=compute0(step,part)
    return res
def parse(s:str,part=0)->list:
    s=s.replace("\n","")
    return s.split(",")
def mkmat(cnt=3)->list:
    return [None]*cnt
def disp(l:list):
    for i,r in enumerate(l):
        #print(f"i={i} r={r}")
        if r:
            s=" ".join([f"[{e[0]} {e[1]}]"for e in r])
            print(f"Box {i}: {s}")
def compute1(l:list)->int:
    boxes=mkmat(256)
    #print(f"boxes={boxes}")
    res=0
    for i,e in enumerate(l):
        #print(f"i={i} e={e}")
        #print(f'\nAfter "{e}":')
        if "="in e:
            label,focal=e.split("=")
            h=compute0(label)
            if not boxes[h]:
                boxes[h] = [[label,focal]]
            else:
                done=False
                for slot in boxes[h]:
                    if slot[0]==label:
                        slot[1]=focal
                        done=True
                if not done:
                    boxes[h]+=[[label,focal]]
        else:
            label,_=e.split("-")
            h=compute0(label)
            for slots in boxes:
                if not slots:continue
                for (i,(label0,_)) in enumerate(slots):
                    #print(f"label0={label0} label={label}")
                    if label0==label:
                        del slots[i]
                        break
        #disp(boxes)
    for i,b in enumerate(boxes):
        #print(f"box {i}")
        if not b:continue
        for j,s in enumerate(b):
            #print(f"slot {j}")
            label,focal=s
            focal=int(focal)
            nb=i+1
            ns=j+1
            res0=nb*ns*focal
            #print(f"{type(label)}: {type(nb)} * {type(ns)} * {type(focal)} = {res0}")
            res+=res0
            #print(f"{label}: {nb} * {ns} * {focal} = {res0}")
    return res
class T000(unittest.TestCase):
    def test_0101(self):
        self.assertEqual(30,compute0("rn=1"))
        self.assertEqual(253,compute0("cm-"))
        self.assertEqual(52,compute0("HASH"))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1+0,compute(parse(open("input1","rt").read())))
    def test_0200(self):
        self.assertEqual(RES02+0*1000,compute(parse(INP01),part=1))
    def test_2000(self):
        self.assertEqual(RES2+0*1000,compute(parse(open("input1","rt").read()),part=1))
