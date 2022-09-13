ll=[
'...>...',
'.......',
'......>',
'v.....>',
'......>',
'.......',
'..vvv..',
]
ll=[]
f=open('input')
for l in f.readlines():
    ll+=[l.rstrip()]
m=[]
for l in ll:
    m+=[list(l)]

import copy

def disp(m):
    for l in m:
        print(f"{''.join(l)}")
def run(m):
    w=len(m[0])
    h=len(m)
    m0=copy.deepcopy(m)
    # m0=m.copy()
    # print('before pass1')
    # disp(m)
    for j in range(h):
        i=0
        while i<w:
            c=m0[j][i]
            if c=='>':
                if i==w-1:
                    if m0[j][0]=='.':
                        m[j][0]=c
                        m[j][i]='.'
                else:
                    if m0[j][i+1]=='.':
                        m[j][i+1]=c
                        m[j][i]='.'
                        i+=1
            i+=1
    # print('after pass1')
    # disp(m)
    m0=copy.deepcopy(m)
    # m0=m.copy()
    # print('after pass1 m0')
    # disp(m0)
    for i in range(w):
        j=0
        while j<h:
            # print(f'j={j} i={i} m0={m0[0][i]}')
            c=m0[j][i]
            if c=='v':
                if j==h-1:
                    # print(f'j={j} i={i} m0={m0[0][i]}')
                    # print('in pass2 m0')
                    # disp(m0)
                    if m0[0][i]=='.':
                        m[0][i]=c
                        m[j][i]='.'
                else:
                    if m0[j+1][i]=='.':
                        m[j+1][i]=c
                        m[j][i]='.'
                        j+=1
            j+=1

print(f'Initial state:')
disp(m)
ref=[
    [
'v...>>.vv>',
'.vv>>.vv..',
'>>.>v>...v',
'>>v>>.>.v.',
'v>v.vv.v..',
'>.>>..v...',
'.vv..>.>v.',
'v.v..>>v.v',
'....v..v.>',
    ],
    [
'....>.>v.>',
'v.v>.>v.v.',
'>v>>..>v..',
'>>v>v>.>.v',
'.>v.v...v.',
'v>>.>vvv..',
'..v...>>..',
'vv...>>vv.',
'>.v.v..v.v',

    ],
    [
'>.v.v>>..v',
'v.v.>>vv..',
'>v>.>.>.v.',
'>>v>v.>v>.',
'.>..v....v',
'.>v>>.v.v.',
'v....v>v>.',
'.vv..>>v..',
'v>.....vv.',

    ]
]
'''
Initial state:
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>

After 1 step:
....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v

After 2 steps:
>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv.

After 3 steps:
v>v.v>.>v.
v...>>.v.v
>vv>.>v>..
>>v>v.>.v>
..>....v..
.>.>v>v..v
..v..v>vv>
v.v..>>v..
.v>....v..

After 4 steps:
v>..v.>>..
v.v.>.>.v.
>vv.>>.v>v
>>.>..v>.>
..v>v...v.
..>>.>vv..
>.v.vv>v.v
.....>>vv.
vvv>...v..

After 5 steps:
vv>...>v>.
v.v.v>.>v.
>.v.>.>.>v
>v>.>..v>>
..v>v.v...
..>.>>vvv.
.>...v>v..
..v.v>>v.v
v.v.>...v.
'''
def cmp(m,r,die=False):
    # print(f'm={m}')
    equ=True
    i=0
    a=None
    b=None
    for i in range(len(m)):
        a=''.join(m[i])
        b=''.join(r[i])
        if a!=b:
            equ=False
            if die:raise Exception(f'DIFFERENT! i={i} a={a} b={b}')
            break
    # if equ:
    #     print('EQUAL!')
    # else:
    #     print(f'DIFFERENT! i={i} a={a} b={b}')
    return equ
# cmp(m,ref[0],True)
old=copy.deepcopy(m)
for step in range(99999):
    run(m)
    print(f'After {step+1} steps:')
    # disp(m)
    # if step<=1:cmp(m,ref[step+1],True)
    if cmp(m,old):raise Exception('NO MOVEMENT!!')
    old=copy.deepcopy(m)
