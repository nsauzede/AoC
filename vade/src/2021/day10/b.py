f=open('input')
lines=[l.rstrip() for l in f.readlines()]
op='([{<'
cl=')]}>'
corrupted_scores=[3,57,1197,25137]
incomplete_scores=[1,2,3,4]
score=0
scores=[0]
for ll in lines:
    # print(f'{ll}', end='')
    l=[c for c in ll]
    # print(f'len {len(l)}')
    stack=[]
    discard=False
    for c in l:
        if c in op:
            stack+=[c]
        elif c in cl:
            last=stack.pop()
            # print(f'c={c} last={last}')
            la=op.index(last)
            cu=cl.index(c)
            if la!=cu:
                # print(f'{ll} - Expected {cl[la]}, but found {cl[cu]} instead.')
                discard=True
                # score+=corrupted_scores[cu]
        else:
            raise Exception(f"unhandled char '{c}'")
    if discard:continue
    sco=0;
    if len(stack)>0:
        print(f'{ll} - Complete by adding ', end='')
        for c in list(reversed((stack))):
            id=op.index(c)
            cu=cl[op.index(c)]
            print(f'{cu}',end='')
            sco*=5
            sco+=incomplete_scores[id]
        print(f' - {sco} total points.')
        scores+=[sco]
scores.sort()
print(f'score={scores[len(scores)//2]}')