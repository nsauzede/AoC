from _test import parse,disp,drawpath,astar_h,astar_d,astar_reconspath
infinity=9999999999999999999
def astar(maze:list,start:list,goal:list)->list:
    global infinity
    ww=len(maze[0])
    hh=len(maze)
    openset={start:0}
    camefrom={}
    gscore={}
    for y in range(hh):
        for x in range(ww):
            gscore[(x,y)]=infinity
    gscore[start]=0
    fscore={start:[astar_h(maze,start),[0,0,0,0]]}   # R D L U
    prev=tuple(start)
    while len(openset)>0:
        fsmin=infinity
        for e in openset:
            fs=fscore[e][0]
            if fs<fsmin:
                current=e
                fsmin=fs
        dirs=fscore[current][1]
        if current==goal:
            return astar_reconspath(camefrom,current)
        del openset[current]
        x,y=current
        neighbors=[]
        if x>0:
            if prev!=(x-1,y):
                neighbors+=[(x-1,y)]
        if y>0:
            if prev!=(x,y-1):
                neighbors+=[(x,y-1)]
        if x<ww-1:
            if prev!=(x+1,y):
                neighbors+=[(x+1,y)]
        if y<hh-1:
            if prev!=(x,y+1):
                neighbors+=[(x,y+1)]
        for neighbor in neighbors:
            tentgscore=gscore[current]+astar_d(maze,current,neighbor,camefrom)
            if tentgscore<gscore[neighbor]:
                camefrom[neighbor]=[current]
                gscore[neighbor]=tentgscore
                fscore[neighbor]=[tentgscore+astar_h(maze,neighbor),[0,0,0,0]]
                if neighbor not in openset:
                    openset[neighbor]=0
        prev=tuple(current)
    return []   # failure

INP011=r"""2413
3215
3255
3446
"""
SOL011="""2>>3
32v>
3255
3446
"""
RES011=11               # 5+1+1+4
m0=parse(INP011)
pos=(0,0)
goal=(3,1)
d={'m':m0,'pos':pos}
disp(d,"INITIAL")
v=astar(m0,pos,goal)
res=drawpath(d,v)
disp(d,f"FINAL -- res={res}")
