def e(n,r):
 print(n)
 print(r)
 for a in(w:=[*range(l:=len(n))])*r:
    w.insert((n[w.pop(c:=w.index(a))]+c)%(l-1),a)
    print(w)
 return sum((c:=[n[i]for i in w])[(c.index(0)+o*1000)%l]for o in[1,2,3])
print(e(p:=[*map(int,open("inp"))],1),e([n*811589153 for n in p],10))
