def explode(lines, i, j):
    ret = 0
    h=len(lines)
    w=len(lines[0])
    if lines[j][i]>0:
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

f=open('input')
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
n=2000
total=0
step=0
print(f'Before any steps:')
for l in lines:
    print(f'{l}')
firstflash=None
for step in range(n):
    lines=[[e+1 for e in l] for l in lines]
    mustbreak=False
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
            print(f'{exp} flashes')
            total+=exp
        if exp==w*h:
            # raise Exception('SYNCHRO FLASH!!')
            print('SYNCHRO FLASH!!')
            # if step>193:
            # if True:
            #     mustbreak=True
            #     break
            if firstflash==None:firstflash=step+1
    print(f'After step {step+1}:')
    for l in lines:
        print(f'{l}')
    if mustbreak:break
print(f'total of {total} flashes')
print(f'First synchro flash at {firstflash}')