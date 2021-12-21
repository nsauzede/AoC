f=open('input')
l=f.readline().rstrip().split('target area: x=')[1]
l=l.split(', y=')
x=l[0].split('..')
y=l[1].split('..')
t=[[int(i) for i in x],[int(i) for i in y]]
print(f't={t}')
vs=[]
# vs+=[[7,2]]
# vs+=[[6,3]]
# vs+=[[9,0]]
# vs+=[[17,-4]]
# vs+=[[6,9]]

# vs+=[[23,-10]]

for vy0 in range(t[1][0]-1,1000+1):
    # vy=vy0-500
    vy=vy0
    for vx in range(6,t[0][1]+1):
        vs+=[[vx,vy]]

# for vy0 in range(1,1000+1):
#     vy=vy0-500
#     for vx in range(1,t[0][0]+1):
#         vs+=[[vx,vy]]
highest=0
highestv=None
meet=[]
for v in vs:
    v0=v.copy()
    # print(f'v0={v0}')
    pos=[0,0]
    step=0
    end=False
    hh=0
    while not end:
        # print(f'v0={v0} pos={pos} v={v}')
        if pos[1]>hh:
            hh=pos[1]
        if pos[0]>=t[0][0] and pos[0]<=t[0][1] and pos[1]>=t[1][0] and pos[1]<=t[1][1]:
            meet+=[v0]
            # print(f'Target hit at {pos} with {v0} high {hh} highest {highest}')
            end=True
            if hh>highest:
                highest=hh
                highestv=v0
                # print(f'Target hit at {pos} with {v0} HIGHEST')
            break
        if pos[0]>t[0][1] and pos[1]<t[1][0]:
            # print(f'Target MISSED')
            end=True
            break
        if pos[0]>2*t[0][1] or pos[1]<2*t[1][0]:
            # print(f'Velocity X stalled')
            end=True
            break
        pos[0]+=v[0]
        pos[1]+=v[1]
        if v[0]>0:v[0]-=1
        elif v[0]<0:v[0]+=1
        v[1]-=1
        step+=1
        # print(f'At end of step {step} pos={pos}')
print(f'{len(meet)} met criteria:')
# 55 too low
# print(f'{meet}')
if highestv:
    print(f'Reached {highest} with {highestv}')
#           1         2         3
# 0123456789012345678901234567890
#3.............#....#............3
#2.......#..............#........2
#1...............................1
#0S........................#.....0
#1...............................1
#2...............................2
#3...........................#...3
#4...............................4
#5....................TTTTTTTTTTT5
#6....................TTTTTTTTTTT6
#7....................TTTTTTTT#TT7
#8....................TTTTTTTTTTT8
#9....................TTTTTTTTTTT9
#0....................TTTTTTTTTTT0
# 0123456789012345678901234567890
