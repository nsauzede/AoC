import unittest
INP01="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
INP01_={'32T3K': 765,
'T55J5': 684,
'KK677': 28,
'KTJJT': 220,
'QQQJA': 483,
}
RES01=6440
#RES1=253837629 # too high
#RES1=250386150 # too high
RES1=250347426
RES02=5905
HIGH='HIGH';ONE='ONE';TWO='TWO';THREE='THREE';FULL='FULL';FOUR='FOUR';FIVE='FIVE'
A='A';K='K';Q='Q';J='J';T='T'
VALS=['2','3','4','5','6','7','8','9',T,J,Q,K,A]
VALS2=[J,'2','3','4','5','6','7','8','9',T,Q,K,A]
def get_type(hand,part=0):
    if part==0:
        return get_type0(hand)
    else:
        return get_type1(hand)
def get_type1(hand):
    d={}
    for c in hand:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    v=sorted(d.values())
    print(f"v={v} d={d}")
    if v==[1,1,1,1,1]:
        return HIGH
    elif v==[1,1,1,2]:
        return ONE
    elif v==[1,2,2]:
        return TWO
    elif v==[1,1,3]:
        return THREE
    elif v==[1,4]:
        return FOUR
    elif v==[2,3]:
        return FULL
    elif v==[5]:
        return FIVE
    else:0/0
def get_type0(hand):
    d={}
    for c in hand:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    v=sorted(d.values())
    print(f"v={v} d={d}")
    if v==[1,1,1,1,1]:
        return HIGH
    elif v==[1,1,1,2]:
        return ONE
    elif v==[1,2,2]:
        return TWO
    elif v==[1,1,3]:
        return THREE
    elif v==[1,4]:
        return FOUR
    elif v==[2,3]:
        return FULL
    elif v==[5]:
        return FIVE
    else:0/0
def insert(l, t, part=0):
    print(f"l={l}")
    for i,t0 in enumerate(l):
        print(f"i={i} t0={t0} t={t}")
        for j,c0 in enumerate(t0[0]):
            valc0=val(c0,part)
            valt=val(t[0][j],part)
            print(f"j={j} valt={valt} valc0={valc0}")
            if valt==valc0:
                continue
            elif valt>valc0:
                break
            print(f"INSERTING {i}")
            l.insert(i,t)
            #print(f"l={l}")
            return l
    print(f"APPENDING")
    l+=[t]
    #print(f"l={l}")
    return l
def val(c,part=0):
    if part==1:
        return VALS2.index(c)
    return VALS.index(c)
def compute(inp:dict,part=0)->int:
    res = 0
    d={HIGH:[],ONE:[],TWO:[],THREE:[],FULL:[],FOUR:[],FIVE:[],}
    for (hand,bid) in inp.items():
        ty=get_type(hand,part)
        insert(d[ty],(hand,bid),part)
        #print(f"hand={hand} bid={bid} : type={ty}")
    print(f"d={d}")
    rank=1
    for _,ty in d.items():
        #print(f"ty={ty}")
        for e in ty:
            #print(f"e={e}")
            res+=rank*e[1]
            rank+=1
    return res
def parse(inp):
    res={}
    for l in inp.splitlines():
        h,b=l.split(" ")
        b=int(b)
        res[h]=b
    return res
class T000(unittest.TestCase):
    def test_0100_val0(self):
        self.assertEqual(0,val('2'))
        self.assertEqual(1,val('3'))
        self.assertEqual(2,val('4'))
        self.assertEqual(3,val('5'))
        self.assertEqual(4,val('6'))
        self.assertEqual(5,val('7'))
        self.assertEqual(6,val('8'))
        self.assertEqual(7,val('9'))
        self.assertEqual(8,val('T'))
        self.assertEqual(9,val('J'))
        self.assertEqual(10,val('Q'))
        self.assertEqual(11,val('K'))
        self.assertEqual(12,val('A'))
    def test_0100_insert0(self):
        self.assertEqual([('32T3K',765)],insert([],('32T3K',765)))
        self.assertEqual([('KTJJT',220),('KK677',28)],insert([('KK677',28)],('KTJJT',220)))
        self.assertEqual([('KTJJT',220),('KK677',28)],insert([('KTJJT',220)],('KK677',28)))
        self.assertEqual([('T55J5',684),('QQQJA',483)],insert([('T55J5',684)],('QQQJA',483)))
        self.assertEqual([('T55J5',684),('QQQJA',483)],insert([('QQQJA',483)],('T55J5',684)))
        self.assertEqual([('32T3K',765),('KK677',28)],insert([('KK677',28)],('32T3K',765)))
        self.assertEqual([('32T3K',765),('KK677',28)],insert([('32T3K',765)],('KK677',28)))
    def test_0100_insert1(self):
        d={HIGH:[],ONE:[],TWO:[],THREE:[]}
        self.assertEqual([('32T3K',765),('KK677',28)],insert([('32T3K',765)],('KK677',28)))
    def test_0100_type0(self):
        self.assertEqual(ONE,get_type('32T3K'))
        self.assertEqual(TWO,get_type('KK677'))
        self.assertEqual(TWO,get_type('KTJJT'))
        self.assertEqual(THREE,get_type('T55J5'))
        self.assertEqual(THREE,get_type('QQQJA'))
        self.assertEqual(FOUR,get_type('2222T'))
        self.assertEqual(FULL,get_type('TATAT'))
    def test_0100_(self):
        self.assertEqual(RES01+0,compute(INP01_))
    def test_0100(self):
        self.assertEqual(RES01+0,compute(parse(INP01)))
    def test_1000(self):
        self.assertEqual(RES1,compute(parse(open("input1","rt").read())))
    def Ztest_0200(self):
        self.assertEqual(RES02+0,compute(INP01_,1))
