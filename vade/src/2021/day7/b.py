f=open('input')
l=list(map(int,f.read().split(',')))
# print(f'l={l}')
n=len(l)+1
c=[0]*n
for i in range(n):
    o=[0]*n
    for j in range(len(l)):
        d=abs(i-l[j])
        # print(f'delta from {l[j]} to {i} : {d}')
        for k in range(d):o[j]+=k+1
        # print(f'move from {l[j]} to {i} : {o[j]}')
    c[i]=sum(o)
    # print(f'pos {i} sum {c[i]} deltas : {o}')
mi=min(c)
pos=c.index(mi)
print(f'optimal pos {pos} cost {mi}')