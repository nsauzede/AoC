infinity=9999999999999999999
def reconspath(camefrom,current):
    total=[current]
    while current in camefrom:
        current=camefrom[current]
        total.insert(0,current)
    return total
def d(fro,to):
    global maze
    v=maze[to[1]][to[0]]
    return v
maze=[
[1,1,6,3,7,5,1,7,4,2],
[1,3,8,1,3,7,3,6,7,2],
[2,1,3,6,5,1,1,3,2,8,],
[3,6,9,4,9,3,1,5,6,9],
[7,4,6,3,4,1,7,1,1,1],
[1,3,1,9,1,2,8,1,3,7],
[1,3,5,9,9,1,2,4,2,1],
[3,1,2,5,4,2,1,6,3,9],
[1,2,9,3,1,3,8,5,2,1],
[2,3,1,1,9,4,4,5,8,1],
]
ww=len(maze[0])
hh=len(maze)
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
    global maze
    v=maze[n[1]][n[0]]
    # print(f'h: n={n} v={v}')
    return v
start=(0,0)
goal=(ww-1,hh-1)
p=astar(start,goal,h)
# print(f'path={p}')
total=0
for j in range(hh):
    for i in range(ww):
        pos=(i,j)
        if pos in p:
            v=maze[j][i]
            if pos!=start:
                total+=v
            print(f'{v}',end='')
        else:
            print(f'.',end='')
    print('')
print(f'total risk={total}')