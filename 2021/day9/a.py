f=open('input')
lines=f.readlines()
w=len(lines[0].rstrip())
h=len(lines)
print(f'w={w} h={h}')
lows=[]
risk=0
for j in range(h):
    for i in range(w):
        v=int(lines[j][i])
        # print(v,end='')
        low=True
        a=[]
        if i>0:a+=[lines[j][i-1]]
        if i<w-1:a+=[lines[j][i+1]]
        if j>0:a+=[lines[j-1][i]]
        if j<h-1:a+=[lines[j+1][i]]
        for adj in a:
            if v >= int(adj):low=False;break
        if low:lows+=[[i,j]];risk+=v+1
    # print('')
print(f'risk={risk}')
