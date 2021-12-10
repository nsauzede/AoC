f=open('input')
l=list(map(int,f.read().split(',')))
# print(f'l={l}')
n=len(l)+1
o=[0]*n
c=[0]*n
for i in range(n):
    for j in range(len(l)):
        o[j]=abs(i-l[j])
    c[i]=sum(o)
    # print(f'pos {i} sum {c[i]} deltas : {o}')
mi=min(c)
pos=c.index(mi)
print(f'optimal pos {pos} cost {mi}')