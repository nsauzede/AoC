infinity=9999999999999999999
def reconspath(camefrom,current):
    total=[current]
    while current in camefrom:
        current=camefrom[current]
        total.insert(0,current)
    return total
def d(fro,to):
    global cavern
    v=cavern[to[1]][to[0]]
    return v
def astar(start,goal,h):
    global infinity
    global ww,hh
    openset={start:0}
    camefrom={}
    gscore={}
    for y in range(hh):
        for x in range(ww):
            gscore[(x,y)]=infinity
    gscore[start]=0
    fscore={start:h(start)}
    while len(openset)>0:
        fsmin=infinity
        for e in openset:
            fs=fscore[e]
            if fs<fsmin:
                current=e
                fsmin=fs
        # print(f'current={current}')
        if current==goal:
            return reconspath(camefrom,current)
        del openset[current]
        x,y=current
        neighbors=[]
        if x>0:neighbors+=[(x-1,y)]
        if y>0:neighbors+=[(x,y-1)]
        if x<ww-1:neighbors+=[(x+1,y)]
        if y<hh-1:neighbors+=[(x,y+1)]
        for neighbor in neighbors:
            tentgscore=gscore[current]+d(current,neighbor)
            if tentgscore<gscore[neighbor]:
                camefrom[neighbor]=current
                gscore[neighbor]=tentgscore
                fscore[neighbor]=tentgscore+h(neighbor)
                if neighbor not in openset:
                    openset[neighbor]=0
    return []   # failure
def h(n):
    global cavern
    v=cavern[n[1]][n[0]]
    # print(f'h: n={n} v={v}')
    return v

f=open('input')
template=[[int(c) for c in l.rstrip()] for l in f.readlines()]
ww0=len(template[0])
hh0=len(template)
cavern=[[0]*ww0*5 for i in range(hh0*5)]
for j in range(5):
    for i in range(5):
        for y in range(hh0):
            for x in range(ww0):
                v=template[y][x]+i+j
                if v>9:v=v-9
                cavern[j*hh0+y][i*ww0+x]=v
ww=len(cavern[0])
hh=len(cavern)
start=(0,0)
goal=(ww-1,hh-1)
p=astar(start,goal,h)
# print(f'path={p}')
total=0
for j in range(hh):
    for i in range(ww):
        pos=(i,j)
        v=cavern[j][i]
        if pos in p:
            if pos!=start:
                total+=v
            # print(f'{v}',end='')
        else:pass
            # print(f'.',end='')
            # print(f'{v}',end='')
    # print('')
print(f'total risk={total}')
