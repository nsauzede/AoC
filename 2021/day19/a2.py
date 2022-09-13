f=open('input2')
scanners=[]
for l in f.readlines():
    l=l.rstrip()
    if l=='':continue
    # print(f'l={l}')
    if l.startswith('--- scanner '):
        n=int(l.split('--- scanner ')[1].split()[0])
        # print(f'scanner {n}')
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
    res=[]
    # disp(s)
    for r in rmat:
        # print(f'r={r}')
        for c in s:
            c2=[int(c[abs(r[0])-1]*math.copysign(1,r[0])),int(c[abs(r[1])-1]*math.copysign(1,r[1])),int(c[abs(r[2])-1]*math.copysign(1,r[2]))]
            # print(c2)
            res+=[(r,c2)]
        # break
    return res
sp00=None
r00=None
n00=None
scannerspos={}
for n0 in range(len(scanners)):
    for s in scanners:
        res={}
        for n in s:
            # print(f'scanner {n}')
            if n==n0:
                rots=rot(s[n])
                # print(f'rots={rots}')
                break
        for n in s:
            # print(f'scanner {n}')
            if n==n0:
                # rots=rot(s[n])
                # print(f'rots={rots}')
                continue
            else:
                res[n]=[]
            pos={}
            for b in s[n]:
                # print(f'checking b={b}')
                for rr in rots:
                    rt=rr[0]
                    r=rr[1]
                    p=(r[0]-b[0],r[1]-b[1],r[2]-b[2])
                    if p not in pos:pos[p]=[]
                    pos[p]+=[(rt,b)]
                # print(f'pos={pos}')
                res[n]+=[pos]
            for p in pos:
                if len(pos[p])>=12:
                    # print(f'pos={p} len={len(pos[p])} {pos[p]}')
                    r=pos[p][0][0]
                    sp=[int(p[0]*math.copysign(1,r[0])),int(p[1]*math.copysign(1,r[1])),int(p[2]*math.copysign(1,r[2]))]
                    sp0=None
                    if sp00 and r00 :#and n0==n00):
                        sp0=sp00.copy()
                        sp0[abs(r[0])-1]+=int(sp[0]*math.copysign(1,r00[abs(r[0])-1]))
                        sp0[abs(r[1])-1]+=int(sp[1]*math.copysign(1,r00[abs(r[1])-1]))
                        sp0[abs(r[2])-1]+=int(sp[2]*math.copysign(1,r00[abs(r[2])-1]))
                    if n0==0:sp00=sp;r00=r;n00=n
                    if sp0 or n0==0 or True:
                        print(f'scanner {n} / {n0}: rpos={sp} r={r} rpos0={sp0}')
                        if n0==0:
                            scannerspos[n]=sp
                        else:
                            scannerspos[n]=sp0
            # print(f'scanner {n}: {len(res[n])}')
            # print(f'scanner {n}: {res[n]}')
