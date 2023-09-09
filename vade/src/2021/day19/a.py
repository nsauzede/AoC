f=open('input0')
scanners=[]
for l in f.readlines():
    l=l.rstrip()
    if l=='':continue
    # print(f'l={l}')
    if l.startswith('--- scanner '):
        n=l.split('--- scanner ')[1].split()[0]
        # print(f'scanner {n}')
        scanner={n:[]}
        scanners+=[scanner]
    else:
        x,y=l.split(',')
        scanner[n]+=[[int(x),int(y)]]
# print(f'scanners={scanners}')
def disp(scanner):
    infinity=9999999999999999999
    xmi,xma=infinity,-infinity
    ymi,yma=infinity,-infinity
    for c in scanner:
        if c[0]<xmi:xmi=c[0]
        if c[0]>xma:xma=c[0]
        if c[1]<ymi:ymi=c[1]
        if c[1]>yma:yma=c[1]
    w=xma-xmi+1
    h=yma-ymi+1
    print(f'width={w} height={h} rx:{xmi},{xma} ry:{ymi},{yma}')
    for j in range(h-1,0-1,-1):
        for i in range(w):
            if [i+xmi,j+ymi] in scanner:print('B',end='')
            else:print('.',end='')
        print('')
for s in scanners:
    for n in s:
        print(f'Scanner {n} : {s[n]}')
        disp(s[n])
