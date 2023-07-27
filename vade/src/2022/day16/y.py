import copy
def process(m:dict,s0:dict,i:int):
    #print(f"s0={s0} i={i}")
    s=copy.deepcopy(s0)
    if s['rem']>0:
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
        if t>0:
            print(f"Returning s['totals']={s} t={t}")
            return [s['totals']]
        else:
            #print("Skip empty result")
            return []

r=process({0:{'r':0,'t':[1,2]},1:{'r':1,'t':[0,2]},2:{'r':2,'t':[0,1]}},{'rem':5,'opens':{},'totals':{}},0)
#print(r)
tmax=0
for e in r:
    t=0
    for k,v in e.items():
        t+=v
    if t>tmax:tmax=t
print(f"tmax={tmax}")
