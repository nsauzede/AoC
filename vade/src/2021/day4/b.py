def fun(fi):
    f=open(fi)
    numbers=[int(e) for e in f.readline().split(',')]
    print(numbers)
    board=0
    grid=5
    boards=[[]]
    n=0
    while True:
        l=f.readline()
        if l=='':break
        if l=='\n':continue
        if n==grid:
            n=0
            board+=1
            boards+=[[]]
        l=l.rstrip()
        l = [int(e) for e in l.strip(' ').replace('  ',' ').split(' ')]
        boards[board]+=[l]
        # print(l)
        n+=1
    for i,b in enumerate(boards):
        print(f'board {i} {b}')

    bn=-1
    win=False
    nwin=0
    nb=len(boards)
    bwin=[False]*nb
    for n in numbers:
        print(f'n={n}')
        for bn,b in enumerate(boards):
            hor=[0]*grid
            ver=[0]*grid
            for i in range(grid):
                for j in range(grid):
                    if b[i][j]==n:
                        b[i][j]*=-1
                        b[i][j]-=1
                    if b[i][j]<0:
                        hor[j]+=1
                        ver[i]+=1
                        if hor[j]==grid or ver[i]==grid:
                            if not bwin[bn]:
                                win=True
                                nwin+=1
                                bwin[bn]=True
                                print(f'WIN!!! n={n} bn={bn}')
                                if nwin==nb:break
                if nwin==nb:break
            print(f'hor={hor} ver={ver}')
            if nwin==nb:break
        if nwin==nb:break
    if win:
        score=0
        for i in range(grid):
            for j in range(grid):
                if b[i][j]>0:
                    score+=b[i][j]
        final=score*n
        print(f'WIN!!! n={n} bn={bn} score={score} final={final}')

# l=['input0']
l=('input0','input')
for f in l:
    fun(f)
