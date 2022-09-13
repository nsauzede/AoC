f=open('input0')
steps=[]
for l in f.readlines():
    t,l=l.split()
    _,l=l.split('x=')
    x,l=l.split(',y=')
    x=x.split('..')
    y,z=l.split(',z=')
    y=y.split('..')
    z=z.split('..')
    steps+=[t,x,y,z]
    # print(f't={t} l={l}')
print(f'stesp={steps}')