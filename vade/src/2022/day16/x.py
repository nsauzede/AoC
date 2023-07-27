import copy
tmax=-1
def process(m:dict,s0:dict,i:int):
    #print(f"s0={s0} i={i}")
    if len(s0['opens'])==len(s0['totals']):
        raise Exception(f"Kaboom all valves are open s0={s0}")
    s=copy.deepcopy(s0)
    if s['rem']>0:
        #print(f"rem={s['rem']}")
        s['rem']-=1
        for k,v in s['opens'].items():
            s['totals'][k]+=v
        r=[]
        for j in m[i]['t']:
            #print(f"Call process for j={j} s={s}")
            r0=process(m,s,j)
            #print(f"Got r0={r0} (j={j})")
            r+=r0
        if i not in s['opens'] and m[i]['r']!=0:
            s['opens'][i]=m[i]['r']
            s['totals'][i]=0
            #print(f"Call process for i={i} s={s}")
            r0=process(m,s,i)
            #print(f"Got r0={r0} (i={i})")
            r+=r0
        #print(f"Returning r={r}")
        return r
    else:
        t=0
        for k,v in s['totals'].items():
            t+=v
        global tmax
        if t>tmax:
            tmax=t
            print(f"tmax={tmax} s0={s0}")
            #print(f"Returning s['totals']={s} t={t}")
            return [s['totals']]
        else:
            #print("Skip empty/min result")
            return []
A=0;B=1;C=2;D=3;E=4;F=5;G=6;H=7;I=8;J=9
print(f"Processing..")
r=process({
A:{'r':0,'t':[D,I,B]},
B:{'r':13,'t':[C,A]},
C:{'r':2,'t':[D,B]},
D:{'r':20,'t':[C,A,E]},
E:{'r':3,'t':[F,D]},
F:{'r':0,'t':[E,G]},
G:{'r':0,'t':[F,H]},
H:{'r':22,'t':[G]},
I:{'r':0,'t':[A,J]},
J:{'r':21,'t':[I]},
},{'rem':10,'opens':{},'totals':{B:0,C:0,D:0,E:0,H:0,J:0}},0)
#print(r)
tmax=0
print(f"Maxing..")
for e in r:
    t=0
    for k,v in e.items():
        t+=v
    if t>tmax:tmax=t
print(f"tmax={tmax}")
