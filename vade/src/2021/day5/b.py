def pr(mat):
    for r in mat:
        for c in r:
            if c==0:print('.',end='')
            else: print(c,end='')
        print('')
def fun(fi):
    # print(f'file={fi}')
    f=open(fi)
    lines=[]
    dim = 0
    nlines=0
    while True:
        l=f.readline()
        if l=='':break
        if l=='\n':continue
        line=[e.split(',') for e in l.rstrip().split(' -> ')]
        nlines+=1
        li=list(map(int,sum(line,[])))
        # print(f'li={li}')
        a,b,c,d=li
        # print(a,b,c,d)
        # if a==c or b==d:
        # print(f'line={line}')
        # li=[list(map(int,e)) for e in line]
        m=max(li)
        # if m==989:print(m, line)
        if m>dim:dim=m
        lines+=[li]
    # print(f'dim={dim}')
    dim+=1
    # print(f'nlines={nlines}')
    # print(f'lines={len(lines)}')
    print(f'dim={dim}')
    mat=[[0]*dim for i in range(dim)]
    for li in lines:
        a,b,c,d=li
        # print(a,b,c,d)
        if a==c:
            mi,ma=min(b,d),max(b,d)
            # print(mi,ma)
            # print(f'len {len(mat),len(mat[0])}')
            for i in range(mi,ma+1):
                mat[i][a]+=1
        elif b==d:
            mi,ma=min(a,c),max(a,c)
            # print(mi,ma)
            for i in range(mi,ma+1):
                mat[b][i]+=1
        else:
            # print(f'li={li}')
            dx=1;dy=1
            if a>c:dx=-1
            if b>d:dy=-1
            # print(f'dx={dx} dy={dy}')
            while True:
                if a>=dim or b>=dim:break
                if a<0 or b<0:break
                mat[b][a]+=1
                if a==c and b==d:break
                a+=dx
                b+=dy
        # pr(mat)
    danger=0
    for j in range(dim):
        for i in range(dim):
            if mat[j][i]>=2:danger+=1
    # pr(mat)
    print(f'danger={danger}')

# l=['input0']
# l=('input0','input')
l=['input']
for f in l:
    fun(f)
# wrong answer 17170 too low
# wrong answer 19754 too high
# good answer 1793
