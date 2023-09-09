x13=1
z=0

def comp(vars,xi,digit):
    div1,add1,add2=digit
    vars['w']=xi
    vars['x']=vars['z']%26+add1
    vars['z']//=div1
    vars['x']= 0 if vars['x']==vars['w'] else 1
    vars['y']=25*vars['x']+1
    vars['z']*=vars['y']
    vars['y']=(vars['w']+add2)*vars['x']
    vars['z']+=vars['y']

inps=[
11119199191999,
]
digits=[
[1,	10,	2],
[1,	15,	16],
[1,	14,	9],
[1,	15,	0],
[26,	-8,	1],
[1,	10,	12],
[26,	-16,	6],
[26,	-4,	6],
[1,	11,	3],
[26,	-3,	5],
[1,	12,	9],
[26,	-7,	3],
[26,	-15,	2],
[26,	-7,	3],
]
# for inp in inps:
#     vars={'w':0,'x':0,'y':0,'z':0}
#     input=str(inp)
#     for i in range(len(input)):
#         comp(vars,int(input[i]),digits[i])
#         print(vars)

# for j,digit in enumerate(digits):
#     for i in range(9):
#         vars={'w':0,'x':0,'y':0,'z':0}
#         comp(vars,i+1,digits[j])
#         print(f'digit={j} i={i+1} vars={vars}')

for i in range(9):
    vars={'w':0,'x':0,'y':0,'z':0}
    comp(vars,i+1,digits[0])
    print(f'd0 i{i+1} z{vars["z"]}: ',end='')
    for ii in range(9):
        comp(vars,ii+1,digits[1])
        print(f'd1 i{ii+1} z{vars["z"]}',end='')
    print('')
