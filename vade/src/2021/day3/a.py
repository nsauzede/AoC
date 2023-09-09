def fun(fi):
    f=open(fi)
    ll=f.readlines()
    n=len(ll)
    w=0
    g=[]
    gr = 0
    for i in range(n):
        l=ll[i].rstrip()
        if w==0:
            w = len(l)
            g=[0]*w
        for j,c in enumerate(l):
            if c=='1':
                g[j]+=1
    print(f'g={g}')
    for i,e in enumerate(g):
        if e>n/2:
            gr += 1 << (len(g)-i-1)
    er = gr ^ ((1 << len(g)) - 1)
    prod = gr * er
    print(f'gamma rate={gr}')
    print(f'epsilon rate={er}')
    print(f'prod={prod}')

for f in ('input0','input'):
    fun(f)
