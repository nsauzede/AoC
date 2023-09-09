f=open('input')
inp=f.read()
l=list(map(int,inp.split(',')))
d=[0]*9
for f in range(len(l)):
    d[l[f]]+=1
print(f'Initial state: {d}')
for t in range(256):
    parents=0
    for f in range(len(d)):
        if f==0:
            parents=d[f]
        else:
            d[f-1]=d[f]
        d[f]=0
    d[8]+=parents
    d[6]+=parents
    print(f'After {t:2d} day: {d}')
    # print(f'day {t}')
print(f'total {sum(d)} fish')