def filter(ll0, bval):
    ll=ll0.copy()
    w=len(ll[0])
    # print(f'll={ll}')
    for i in range(w):
        n=len(ll)
        if n==1:break
        cnt=0
        for j in range(n):
            l=ll[j]
            if l[i]=='1':
                cnt+=1
        # print(f'cnt={cnt}')
        j=0
        while j<len(ll):
            if (cnt>=n/2) ^ (ll[j][i]==bval):
                # print(f'del {j}')
                del ll[j]
            else:
                # print(f'keep {j}')
                j+=1
        # print(f'll={ll}')
    val=0
    for i,c in enumerate(ll[0]):
        if c=='1':
            val += 1 << w-i-1
    return val

def fun(fi):
    f=open(fi)
    ll=[e.rstrip() for e in f.readlines()]
    w=len(ll[0])
    oxr=filter(ll,'1')
    print(f'oxygen rate={oxr}')
    cor=filter(ll,'0')
    print(f'co2 rate={cor}')
    prod=oxr*cor
    print(f'prod={prod}')

# l=['input0']
l=('input0','input')
for f in l:
    fun(f)
