f=open('input0')
enh=f.readline().rstrip()
f.readline()
img=[]
first=True
for l in f.readlines():
    ll=['.']+list(l.rstrip())+['.']
    if first:
        w=len(ll)
        img+=[['.']*w]
        first=False
    img+=[ll]
w=len(img[0])
img+=[['.']*w]
print(f'enh={enh}')
print(f'img={img}')
def enhance(enh,img):
    w=len(img[0])
    h=len(img)
    img2=[]
    for j in range(h+2):
        img2+=[list('.'*(w+2))]
    img20=[]
    for j in range(h+2):
        img20+=[list('.'*(w+2))]
    for j in range(h):
        for i in range(w):
            img20[1+j][1+i]=img[j][i]
    for j in range(h):
        for i in range(w):
            s=''
            s+=img20[1+j-1][1+i-1]
            s+=img20[1+j-1][1+i]
            s+=img20[1+j-1][1+i+1]
            s+=img20[1+j][1+i-1]
            s+=img20[1+j][1+i]
            s+=img20[1+j][1+i+1]
            s+=img20[1+j+1][1+i-1]
            s+=img20[1+j+1][1+i]
            s+=img20[1+j+1][1+i+1]
            s=s.replace('.','0')
            s=s.replace('#','1')
            n=int(s,2)
            if i==3 and j==3:
                print(f's={s} n={n}')
            img2[j+1][i+1]=enh[n]
            # img20[j+1][i+1]=enh[n]
            # img2[j+1][i+1]=img[j][i]
    # img2=img20
    return img2
def disp(img):
    ret=0
    for l in img:
        print(''.join(l))
        ret+=l.count('#')
    return ret
img2=img
disp(img)
n=2
for i in range(n):
    img2=enhance(enh,img2)
    # print(f'step {i+1} img={img2}')
    print(f'step {i+1} img=:')
    nl=disp(img2)
    print(f'nlit={nl}')
# for n in [0,10,20,30,34,40,50,60,70]:
#     print(f'c[{n}={enh[n]}')
