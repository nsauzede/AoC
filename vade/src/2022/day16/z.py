import copy
def process(m:list,s0:list,i:int):
    print(f"s0={s0} i={i}")
    s=copy.deepcopy(s0)
    if s['rem']>0:
        s['rem']-=1
        s['total']+=m[i]
        r=[]
        for c in range(len(m)):
            print(f"Call process for (c={c})")
            r0=process(m,s,c)
            print(f"Got r0={r0} (c={c})")
            r+=r0
        print(f"Returning r={r}")
        return r
    else:
        print(f"Returning s['total']={s['total']}")
        return [s['total']]

r=process([0,1,2],{'rem':3,'total':0},0)
print(r)
