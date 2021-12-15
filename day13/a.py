f=open('input')
lines=[l.rstrip() for l in f.readlines()]
coords=[]
folds=[]
iscoord=True
w=0
h=0
for l in lines:
    if iscoord:
        if l=='':
            iscoord=False
            continue
            l=list(map(int,inp.split(',')))
        c=list(map(int, l.split(',')))
        if c[0]>w:w=c[0]
        if c[1]>h:h=c[1]
        coords+=[c]
    else:
        if l=='':break
        a,b=l.split('fold along ')[1].split('=')
        folds+=[[a,int(b)]]
w+=1;h+=1
print(f'w={w} h={h}')
# print(f'coords={coords}')
# print(f'folds={folds}')
dots=[]
for i in range(h):
    dots+=[[0]*w]
for c in coords:
    dots[c[1]][c[0]]=1
# print(f'dots={dots}')
for f in folds:
    # print(f'f={f}')
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
    break
# print(f'dots={dots}')
total=0
for j in range(h):
    for i in range(w):
        print('.#'[dots[j][i]],end='')
        if dots[j][i]==1:total+=1
    print('')
print(f'Total {total} dots')
# 732 too high
