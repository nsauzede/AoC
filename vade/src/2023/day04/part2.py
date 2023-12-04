import re
s="""Card    1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
def parse(inp:str)->dict:
    d={}
    a=[]
    for s in inp.splitlines():
        s = re.sub(r'\s+', ' ', s)
        l=s.split(":")
        _,card=l[0].split(' ')
        card=int(card)
        wins0,have0=l[1].split('|')
        wins=[]
        for w in wins0.split(' '):
            if w=='':continue
            wins+=[int(w)]
        have=[]
        if card not in d:d[card]=[]
        nwins=0
        for w in have0.split(' '):
            if w=='':continue
            have+=[int(w)]
            if int(w) in wins:
                nwins+=1
        for i in range(nwins):
            d[card]+=[card+1+i]
    return d
def compute(s):
    d=parse(s)
    res={}
    for e in d:
        if e not in res:
            res[e]=0
        res[e]+=1
        n=res[e]
        for c in d[e]:
            if c not in res:
                res[c]=0
            res[c]+=n
    return sum(res.values())
res=compute(s)
print(f"res={res}")
assert res==30
s=open("input1","rt").read()
res=compute(s)
print(f"res={res}")
assert res==11024379
