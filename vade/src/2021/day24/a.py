pr=[
    ['inp','x'],
    ['mul','x','-1'],
]
pr=[
['inp', 'z'],
['inp', 'x'],
['mul', 'z', '3'],
['eql', 'z', 'x'],
]
pr=[
['inp', 'w'],
['add', 'z', 'w'],
['mod', 'z', '2'],
['div', 'w', '2'],
['add', 'y', 'w'],
['mod', 'y', '2'],
['div', 'w', '2'],
['add', 'x', 'w'],
['mod', 'x', '2'],
['div', 'w', '2'],
['mod', 'w', '2'],
]
f=open('input')
pr=[]
for l in f.readlines():
    pr+=[l.rstrip().split()]
def eva(vars,pr,inp):
    ii=0
    step=0
    for ins in pr:
        # print(f'{step+1} vars={vars}');step+=1
        if ins[0]=='inp':
            # print(i, ii)
            vars[ins[1]]=int(inp[ii])
            ii+=1
        elif ins[0]=='mul':
            v=ins[2]
            if v>='w':
                v=vars[v]
            v=int(v)
            a=vars[ins[1]]
            b=v
            # print(f'a={type(a)} b={type(b)}')
            vars[ins[1]]=a*b
        elif ins[0]=='div':
            v=ins[2]
            if v>='w':
                v=vars[v]
            v=int(v)
            a=vars[ins[1]]
            b=v
            # print(f'a={type(a)} b={type(b)}')
            vars[ins[1]]=a//b
        elif ins[0]=='add':
            v=ins[2]
            if v>='w':
                v=vars[v]
            v=int(v)
            a=vars[ins[1]]
            b=v
            # print(f'a={type(a)} b={type(b)}')
            vars[ins[1]]=a+b
        elif ins[0]=='mod':
            v=ins[2]
            if v>='w':
                v=vars[v]
            v=int(v)
            a=vars[ins[1]]
            b=v
            # print(f'a={type(a)} b={type(b)}')
            vars[ins[1]]=a%b
        elif ins[0]=='eql':
            v=ins[2]
            if v>='w':
                v=vars[v]
            v=int(v)
            a=vars[ins[1]]
            b=v
            # print(f'a={type(a)} b={type(b)}')
            if a==b:vars[ins[1]]=1
            else:vars[ins[1]]=0
        else:
            raise Exception(f'unimp insn {ins[0]}')

inp='73345678912345'
inp='11111111111111'
i=99999999999999
# inp=99999862692664
# vars={'w': 4, 'x': 1, 'y': 7, 'z': 3703515043}
# inp=99999862692663
# vars={'w': 3, 'x': 1, 'y': 6, 'z': 3703515042}
i=99999862692664
li=[
11111111111111,     # vars={'w': 1, 'x': 1, 'y': 4, 'z': 43590018}
# 12345678912345,
11119199191999,     #vars={'w': 9, 'x': 1, 'y': 12, 'z': 1133486756}
# 11111111111112,
# 11111111111121,
# 11111111111211,
# 11111111112111,
# 11111111121111,
# 11111111211111,
# 11111112111111,
# 11111121111111,
# 11111211111111,
# 11112111111111,
# 11121111111111,
# 11211111111111,
# 12111111111111,
# 21111111111111,
]
ind=0
i=11111111111111
while i > 0:
    # if ind>=len(li):break
    # i=li[ind]
    # ind+=1
    inp=str(i)
    if '0' in inp:
        print(f'killing {inp}')
        # i-=10**(len(inp)-inp.index('0')-1)
        i+=10**(len(inp)-inp.index('0')-1)
        inp=str(i)
        if '0' not in inp:print(f'inp={inp}')
        continue
    if '0' in inp:raise Exception('0 VERBOTEN')
    vars={'w':0,'x':0,'y':0,'z':0}
    print(f'inp={inp}')
    eva(vars,pr,inp)
    print(f'vars={vars}')
    if vars['z']==0:
        raise Exception(f'largest model found !!!!!!!!!!!!')
    # i-=1
    i+=1
    # break
