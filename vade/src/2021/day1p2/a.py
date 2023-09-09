# f=open('input0')
f=open('../day1p1/input')
ll=f.readlines()
n=len(ll)
o=-1
incr=0
for i in range(n):
    l=ll[i]
    v=int(l)
    print(v)
    if i <= n-3:
        a=int(ll[i+0])
        b=int(ll[i+1])
        c=int(ll[i+2])
        d=0
        s=a+b+c
        if o!=-1:
            d=s-o
        print(f'{a} {b} {c} => {s} ({d})')
        if d>0:
            incr+=1
        o=s
print(f'incr={incr}')
