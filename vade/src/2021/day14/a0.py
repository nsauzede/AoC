f=open('input0')
lines=[l.rstrip() for l in f.readlines()]
template=lines[0]
del lines[0:2]
rules={}
pairs0={}
for l in lines:
    a,b=l.split(' -> ')
    rules[a]=b
    pairs0[a]=0
print(f'rules={rules}')
print(f'Template: {template}')
pairs1=pairs0.copy()
for step in range(4):
    s=''
    for i in range(len(template)-1):
        pair=template[i]+template[i+1]
        pairs1[pair]+=1
        print(f'pair={pair}')
        c=rules[pair]
        print(f'c={c}')
        s+=template[i]+c
    s+=template[i+1]
    template=s
    counts={}
    for c in template:
        if c not in counts:
            counts[c]=1
        else:
            counts[c]+=1
    # print(f'template={template}')
    # print(f'counts={counts}')
    kma=max(counts,key=counts.get)
    kmi=min(counts,key=counts.get)
    # print(f'kma={kma}')
    # print(f'kmi={kmi}')
    ma=counts[kma]
    mi=counts[kmi]
    # print(f'ma={ma} mi={mi}')
    b,c,h,n=template.count('B'),template.count('C'),template.count('H'),template.count('N')
    print(f'After step {step+1}: {template} ({len(template)}, B={b}, C={c}, H={h}, N={n}, delta={ma-mi})')
    # print(f'After step {step+1}: ({len(template)}, B={b}, C={c}, H={h}, N={n}, delta={ma-mi})')
    print('Pairs:',end='')
    for p in pairs1:
        if pairs1[p]>0:
            print(f' {p}({pairs1[p]})',end='')
    print('')
#1030 too low
