players={
    0:{'pos':4,'score':0},
    1:{'pos':8,'score':0}
    }
wins={0:0,1:0}
rolls=0
def play(players,die=0):
    global rolls
    global wins
    # print(f'rolls={rolls} die={die} players={players}')
    p=(rolls//3)%2
    d=rolls%3
    if die==0:
        play(players.copy(),1)
        play(players.copy(),2)
        play(players.copy(),3)
    else:
        rolls+=1
        print(f'{die}({rolls})',end='')
        players[p]['pos']+=die
        if d==2:
            players[p]['pos']%=10
            players[p]['score']+=players[p]['pos']+1
            print(f' rolls={rolls} die={die} players={players}')
        
        if players[p]['score']>=21:
            sc=players[p]['score']
            print(f' player {p} won score {sc}')
            wins[p]+=1
        else:
            play(players)

play(players)
print(f'wins={wins} players={players}')