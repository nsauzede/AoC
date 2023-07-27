MAXMIN=6
def browse(st:dict, d:dict, v:str, minute:int):
    mov=len(openable_valves(d))
    print(f"== Minute {minute} == in {v} st={st}")
    if minute>=MAXMIN:
        print("Stop!")
        return
    p=0
    l=[]
    for k,rate in st['open'].items():
        l+=k
        p+=rate
    if len(l)>0:
        print(f"Valves {l} are open, releasing {p} pressure.");
        if len(l)==mov:
            for rem in range(minute,MAXMIN):
                st['pressure']+=p
            print(f"ALL OPENABLE VALVES ARE OPEN!! RESULT AT {MAXMIN} WOULD BE {st['pressure']}")
            return
        st['pressure']+=p
    else:
        print("No valves are open.")
    if v not in st['open'] and d[v]['rate']>0:
        st['open'][v]=d[v]['rate']
        print(f"You open valve {v}.")
    else:
        v=d[v]['next'][0]
        print(f"You move to valve {v}.")
    minute+=1
    browse(st, d,v,minute)

def openable_valves(d:dict)->list:
    l=[]
    for k,v in d.items():
        if v['rate']>0:
            l+=[k]
    return l

d={
'A':{'rate':1,'next':['B']},
'B':{'rate':2,'next':['A']},
}
st={
'open':{},
'pressure':0,
}
mov=len(openable_valves(d))
print(f"There are {mov} max openable valves")
browse(st, d,'A',1)
