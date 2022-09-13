f=open('input')
players={}
for i in range(2):
    l=f.readline().rstrip().split(':')[1]
    players[i]={'pos':int(l)-1,'score':0}
print(f'players={players}')
die=0
def dice():
    global die
    die=(die%100)+1
    return die
ndice=0
ss0=0
for step in range(1000):
    ss=0
    for i in range(len(players)):
        d=[dice()]
        d+=[dice()]
        d+=[dice()]
        ndice+=3
        s=sum(d)
        p=((players[i]['pos']+s)%10)
        players[i]['pos']=p
        players[i]['score']+=p+1
        ss=players[i]['score']
        print(f'Player {i+1} rolls {d[0]}+{d[1]}+{d[2]} and moves to space {p+1} for a total score of {ss}')
        if ss>=1000:
            # print('stop')
            break
        ss0=ss
    if ss>=1000:
        # print('stop')
        print(f'step={step} ndice={ndice} ss0={ss0} total={ndice*ss0}')
        break
