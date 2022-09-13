f=open('input')
lines=[l.rstrip() for l in f.readlines()]
folds=[]
w=0
h=0
for l in lines:
    if l.startswith('fold along '):
        a,b=l.split('fold along ')[1].split('=')
        b = int(b)
        folds+=[[a,b]]
        if a=='y':
            hh=b*2+1
            if hh>h:h=hh
        if a=='x':
            ww=b*2+1
            if ww>w:w=ww
print(f'w={w} h={h}')
coords=[]
for l in lines:
    if l=='':
        break
    c=list(map(int, l.split(',')))
    coords+=[c]
# print(f'coords={coords}')
# print(f'folds={folds}')
dots=[]
for i in range(h):
    dots+=[[0]*w]
for c in coords:
    dots[c[1]][c[0]]=1
# print(f'dots={dots}')
for f in folds:
    print(f'f={f}')
    if f[0]=='y':
        for y in range(f[1]):
            for x in range(w):
                dots[y][x]|=dots[h-y-1][x]
        h=y+1
    elif f[0]=='x':
        for x in range(f[1]):
            for y in range(h):
                dots[y][x]|=dots[y][w-x-1]
        w=x+1
# print(f'dots={dots}')
total=0
for j in range(h):
    for i in range(w):
        print('.#'[dots[j][i]],end='')
        if dots[j][i]==1:total+=1
    print('')
print(f'Total {total} dots')
# 732 too high
# w 11 from x=5