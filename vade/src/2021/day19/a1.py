f=open('input1')
scanners=[]
for l in f.readlines():
    l=l.rstrip()
    if l=='':continue
    # print(f'l={l}')
    if l.startswith('--- scanner '):
        n=l.split('--- scanner ')[1].split()[0]
        print(f'scanner {n}')
        scanner={n:[]}
        scanners+=[scanner]
    else:
        x,y,z=l.split(',')
        scanner[n]+=[[int(x),int(y),int(z)]]
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
    for c in scanner:
        print(c)
#left-hand
#x+: [x+,y+,z+] [x+,z-,y+] [x+,y-,z-] [x+,z+,y-]
#x-: [x-,y-,z+] [x-,z+,y+] [x-,y+,z-] [x-,z-,y-]
#y+: [y+,x-,z+] [y+,z-,x-] [y+,x+,z-] [y+,z+,x+]
#y-: [y-,x+,z+] [y-,z-,x+] [y-,x-,z-] [y-,z+,x-]
#z+: [z+,x+,y+] [z+,y-,x+] [z+,x-,y-] [z+,y+,x-]
#z-: [z-,x-,y+] [z-,y-,x-] [z-,x+,y-] [z-,y+,x+]

#x+: [-1,-1,1] [-1,1,1] [-1,1,-1] [-1,-1,-1]
rmat=[
    [1,2,3],[1,-3,2],[1,-2,-3],[1,3,-2],
    [-1,-2,3],[-1,3,2],[-1,2,-3],[-1,-3,-2],
    [2,-1,3],[2,-3,-1],[2,1,-3],[2,3,1],
    [-2,1,3],[-2,-3,1],[-2,-1,-3],[-2,3,-1],
    [3,1,2],[3,-2,1],[3,-1,-2],[3,2,-1],
    [-3,-1,2],[-3,-2,-1],[-3,1,-2],[-3,2,1]
]
import math
def rot(s):
    # disp(s)
    for r in rmat:
        print(f'r={r}')
        for c in s:
            c2=[int(c[abs(r[0])-1]*math.copysign(1,r[0])),int(c[abs(r[1])-1]*math.copysign(1,r[1])),int(c[abs(r[2])-1]*math.copysign(1,r[2]))]
            print(c2)
        # break
for s in scanners:
    for n in s:
        # print(f'Scanner {n} : {s[n]}')
        # disp(s[n])
        print(f'n={n}')
        rot(s[n])
    break
