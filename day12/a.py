def walk(tree,node,visited):
    ret=0
    if node.islower() and node in visited:
        # print(f'*back*');
        return 0
    visited2=visited+[node]
    if node=='end':print(visited2);return 1
    for n in tree[node]:
        # print(f'n={n}')
        r=walk(tree,n,visited2)
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
n=walk(tree,'start',[])
print(f'Total {n} paths')