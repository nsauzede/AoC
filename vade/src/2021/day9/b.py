def explore(lines, i, j):
    h=len(lines)
    w=len(lines[0])
    print(f'i={i} j={j} w={w} h={h} : ', end='')
    v=lines[j][i]
    if v==9:print('returning on max');return 0
    ret=1
    print(f'POINT {v}')
    lines[j][i]=9
    if j>0:
        print(f'trying up i={i} j={j}')
        ret+=explore(lines, i, j-1)
    if j<h-1:
        print(f'trying down i={i} j={j}')
        ret+=explore(lines, i, j+1)
    if i>0:
        print(f'trying left i={i} j={j}')
        ret+=explore(lines, i-1, j)
    if i<w-1:
        print(f'trying right i={i} j={j}')
        ret+=explore(lines, i+1, j)
    return ret

f=open('input')
lines_=f.readlines()
lines=[]
for l in lines_:
    li=[]
    for c in l.rstrip():
        li+=[int(c)]
    lines+=[li]
w=len(lines[0])
h=len(lines)
print(f'w={w} h={h}')
print(lines)
lows=[]
risk=0
for j in range(h):
    for i in range(w):
        v=lines[j][i]
        low=True
        a=[]
        if i>0:a+=[lines[j][i-1]]
        if i<w-1:a+=[lines[j][i+1]]
        if j>0:a+=[lines[j-1][i]]
        if j<h-1:a+=[lines[j+1][i]]
        for adj in a:
            if v >= adj:low=False;break
        if low:lows+=[[i,j]];risk+=v+1
print(f'risk={risk}')
basins=[]
for e in lows:
    print('NEW BASIN !!')
    basins+=[explore(lines, e[0], e[1])]
print(f'basins={basins}')
s=sorted(basins)[-3:]
total=s[0]*s[1]*s[2]
print(f'total={total}')
