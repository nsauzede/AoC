infinity=9999999999999999999
# External provided routines:
# d(current,neighbor) is the weight of the edge from current to neighbor
# d is the heuristic function. h(n) estimates the cost to reach goal from node n.
def astar_d(maze:list,fro:list,to:list)->int:
    t=maze[to[1]][to[0]]
    f=maze[fro[1]][fro[0]]
    v=t-f
    if v==0:v+=1        # increase cost of same levels moves to avoid pseudo zero cost
    if v>=2:v=infinity  # prevent ever choosing 2+ levels edges
    return v

# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def astar_h(maze:list,n:list)->int:
    v=maze[n[1]][n[0]]
    return v

def astar_reconspath(camefrom,current):
    total=[current]
    while current in camefrom:
        current=camefrom[current][0]
        total.insert(0,current)
    return total
def astar_visit(maze,fro,to,t,g,h):pass
def astar(maze:list,start:list,goal:list,h=astar_h,d=astar_d,reconspath=astar_reconspath,visit=astar_visit)->list:
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
    fscore={start:h(maze,start)}
    prev=tuple(start)
    while len(openset)>0:
        #print(f"openset={openset}")
        fsmin=infinity
        for e in openset:
            fs=fscore[e]
            if fs<fsmin:
                current=e
                fsmin=fs
        if current==goal:
            print("FOUND!!")
            return reconspath(camefrom,current)
        #print(f"DEL OPENSET CURRENT={current}: {openset[current]}")
        del openset[current]
        #print(f"openset={openset}")
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
            extra=0
            if current in camefrom:
                if prev[0]>current[0]:
                    #print(f"prev R")
                    camefrom[current][1]+=1
                elif prev[0]<current[0]:
                    #print(f"prev L")
                    camefrom[current][3]+=1
                elif prev[1]>current[1]:
                    #print(f"prev D")
                    camefrom[current][2]+=1
                elif prev[1]<current[1]:
                    #print(f"prev U")
                    camefrom[current][4]+=1
                if neighbor[0]>current[0]:
                    #print(f"neighbor R")
                    if camefrom[current][1]>2:
                        extra+=1000
                elif neighbor[0]<current[0]:
                    #print(f"neighbor L")
                    if camefrom[current][3]>2:
                        extra+=1000
                elif neighbor[1]>current[1]:
                    #print(f"neighbor D")
                    if camefrom[current][2]>2:
                        extra+=1000
                elif neighbor[1]<current[1]:
                    #print(f"neighbor U")
                    if camefrom[current][4]>2:
                        extra+=1000
                #print(f"neighbor={neighbor} prev={prev} current={current} extra={extra} camefrom={camefrom[current]}")
                pass
            tentgscore=gscore[current]+d(maze,current,neighbor,camefrom)+extra
            if tentgscore<gscore[neighbor]:
                if neighbor not in camefrom:
                    camefrom[neighbor]=[None,0,0,0,0] # pos R D L U
                camefrom[neighbor][0]=current
                if neighbor[0]>current[0]:
                    camefrom[neighbor][1]+=1
                elif neighbor[0]<current[0]:
                    camefrom[neighbor][3]+=1
                elif neighbor[1]>current[1]:
                    camefrom[neighbor][2]+=1
                elif neighbor[1]<current[1]:
                    camefrom[neighbor][4]+=1
                #print(f"camefrom={camefrom[neighbor]}")
                #visit(maze,current,neighbor,tentgscore,gscore[neighbor],h(maze,neighbor))
                gscore[neighbor]=tentgscore
                fscore[neighbor]=tentgscore+h(maze,neighbor)
                if neighbor not in openset:
                    #openset[neighbor]=0
                    openset[neighbor]=camefrom[neighbor]
                    #print(f"CLEAR OPENSET NEIGHBOR={neighbor}")
        prev=tuple(current)
    return []   # failure
