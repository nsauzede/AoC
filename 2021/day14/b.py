def comp(dic,last_pair):
    counts=counts0.copy()
    d=dic.copy()
    last_pair2=''
    for k in dic:
        n=dic[k]
        if n==0:continue
        d[k]-=n
        c=rules[k]
        pair=k[0]+c
        d[pair]+=n
        pair=c+k[1]
        d[pair]+=n
        counts[k[0]]+=n
        counts[c]+=n
        if k==last_pair:
            counts[k[1]]+=1
            last_pair2=pair
    return counts,d,last_pair2

f=open('input')
lines=[l.rstrip() for l in f.readlines()]
template=lines[0]

del lines[0:2]
rules={}
pairs0={}
counts0={}
for l in lines:
    a,b=l.split(' -> ')
    rules[a]=b
    pairs0[a]=0
    counts0[b]=0
dic0={}
for k in rules:
    dic0[k]=0
dic=dic0.copy()
print(f'template={template}')
last_pair=''
for i in range(len(template)-1):
    pair=template[i:i+2]
    dic[pair]+=1
    last_pair=pair
for step in range(40):
    counts,d,last_pair2=comp(dic,last_pair)
    mi=min(counts,key=counts.get)
    ma=max(counts,key=counts.get)
    delta=counts[ma]-counts[mi]
    print(f'After step {step+1}: n={sum(counts.values())} counts={counts} delta={delta}')
    dic=d
    last_pair=last_pair2
