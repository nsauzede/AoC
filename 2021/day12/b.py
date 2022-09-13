def walk(tree,node,visited,roundtrip):
    ret=0
    if node.islower():
        if node in visited:
            if roundtrip==1:
                # print(f'*back*');
                return 0
            else:
                roundtrip=1
    visited2=visited+[node]
    if node=='end':print(visited2);return 1
    for n in tree[node]:
        if n=='start':continue
        # print(f'n={n}')
        r=walk(tree,n,visited2,roundtrip)
        ret+=r
    return ret

f=open('input')
lines=[l.rstrip() for l in f.readlines()]
tree={}
for l in lines:
    a,b=l.split('-')
    if a not in tree:tree[a]=[b]
    else:tree[a]+=[b]
    if b not in tree:tree[b]=[a]
    else:tree[b]+=[a]
# print(f'tree={tree}')
n=walk(tree,'start',[],0)
print(f'Total {n} paths')