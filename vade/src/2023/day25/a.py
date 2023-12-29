
def eq(pt:tuple)->(float,float):
    A,D=pt
    B=tuple(a+b for a,b in zip(A,D))
    xa,ya=A[0:2]
    xb,yb=B[0:2]
    m=(yb-ya)/(xb-xa)
    p=ya-m*xa
    print(f"m={m} p={p}")
    return m,p

def inter(a,b)->(float,float):
    if a==b:xj,yj=None,None
    elif a[0]==b[0]:xj,yj=None,None
    elif a[0]==0:xj,yj=(a[1]-b[1])/a[0],a[1]
    elif b[0]==0:xj,yj=(b[1]-a[1])/b[0],b[1]
    else:
        xj=(b[1]-a[1])/(a[0]-b[0])
        yj=a[0]*xj+a[1]
    print(f"xj={xj} yj={yj}")
    return xj,yj

A=((19, 13, 30), (-2,  1, -2))
B=((18, 19, 22), (-1, -1, -2))

a=eq(A)
b=eq(B)
inter(a,b)
