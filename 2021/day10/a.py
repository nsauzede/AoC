f=open('input0')
lines=[l.rstrip() for l in f.readlines()]
stack=[]
op='([{<'
cl=')]}>'
scores=[3,57,1197,25137]
score=0
for ll in lines:
    # print(f'{ll}', end='')
    l=[c for c in ll]
    # print(f'len {len(l)}')
    for c in l:
        if c in op:
            stack+=[c]
            pass
        elif c in cl:
            last=stack.pop()
            # print(f'c={c} last={last}')
            la=op.index(last)
            cu=cl.index(c)
            if la!=cu:
                # raise Exception(f'la={la} cu={cu}')
                print(f'{ll}', end='')
                print(f' - Expected {cl[la]}, but found {cl[cu]} instead.', end='')
                print('')
                score+=scores[cu]
        else:
            raise Exception(f"unhandled char '{c}'")
    # print('')
print(f'score={score}')