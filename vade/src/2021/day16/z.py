def compute(o):
    if type(o)==int:return o
    elif type(o)==dict:
        for op in o:
            if op=='ADD':
                l=[]
                for e in o[op]:
                    l+=[compute(e)]
                return sum(l)
            else:
                raise Exception(f'op {op} notimp')
    else:
        raise Exception(f'type {type(e)} notimp')
# stack=[]
# stack+=[123]
# stack+=[{'ADD':[11, 12]}]
# stack={'ADD':[11, 12]}
stack={'ADD':[11, {'ADD':[4,5,6]}]}
# stack=123
# print(f'stack={stack}')
l=
def build(l):
    for e in l:

stack=build(l)
n=compute(stack)
print(f'final n={n}')
