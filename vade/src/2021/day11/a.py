def explode(lines, i, j):
    ret = 0
    h=len(lines)
    w=len(lines[0])
    if lines[j][i]>0:
        # print(' XP', end='')
        lines[j][i]+=1
        if lines[j][i]>=10:
            ret=1
            lines[j][i]=0
            if j>0:
                if i>0:
                    ret += explode(lines, i-1, j-1)
                ret += explode(lines, i, j-1)
                if i<w-1:
                    ret += explode(lines, i+1, j-1)
            if i>0:
                ret += explode(lines, i-1, j)
            if i<w-1:
                ret += explode(lines, i+1, j)
            if j<h-1:
                if i>0:
                    ret += explode(lines, i-1, j+1)
                ret += explode(lines, i, j+1)
                if i<w-1:
                    ret += explode(lines, i+1, j+1)
    return ret

f=open('input0')
lines_=f.readlines()
lines=[
[1,1,1,1,1],
[1,9,9,9,1],
[1,9,1,9,1],
[1,9,9,9,1],
[1,1,1,1,1]
]
lines=[[int(c) for c in l.rstrip()] for l in lines_]
w=len(lines[0])
h=len(lines)
n=100
total=0
step=0
for step in range(n):
    print(f'step {step}')
    for l in lines:
        print(f'{l}')
    lines=[[e+1 for e in l] for l in lines]
    # print(f'step {step}+')
    # for l in lines:
    #     print(f'{l}')
    while True:
        exp=0
        for j in range(h):
            for i in range(w):
                if lines[j][i]==10:
                    lines[j][i]-=1
                    xp = explode(lines,i,j)
                    exp+=xp
        if exp==0:
            break
        else:
            # exp=0
            # for j in range(h):
            #     for i in range(w):
            #         if lines[j][i]==0:exp+=1
            print(f'{exp} flashes')
            total+=exp
step+=1
print(f'step {step}')
for l in lines:
    print(f'{l}')
print(f'total of {total} flashes')