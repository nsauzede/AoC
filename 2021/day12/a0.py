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

tree={'start':['A','b'],'A':['b','c','end'],'b':['A','d','end'],'c':['A'],'d':['b']}
n=walk(tree,'start',[])
print(f'Total {n} paths')