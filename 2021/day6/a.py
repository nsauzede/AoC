f=open('input')
inp=f.read()
l=list(map(int,inp.split(',')))
print(f'Initial state: {l}')
for t in range(80):
    for f in range(len(l)):
        if l[f]==0:
            l[f]=6
            l+=[8]
        else:
            l[f]-=1
    # print(f'After {t:2d} day: {l}')
print(f'total {len(l)} fish')