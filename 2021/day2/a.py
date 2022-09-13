def fun(fi):
    f=open(fi)
    ll=f.readlines()
    n=len(ll)
    hpos=0
    depth=0
    aim=0
    for i in range(n):
        l=ll[i]
        a,v=l.split()
        v=int(v)
        if a=='forward':hpos+=v;depth+=aim*v
        elif a=='down':aim+=v
        elif a=='up':aim-=v
    prod=hpos*depth
    print(f'hpos={hpos} depth={depth} prod={prod}')

for f in ('input0','input'):
    fun(f)
