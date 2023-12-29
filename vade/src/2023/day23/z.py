import re
class Block:
    def __init__(self,x,y,z,b): self.x,self.y,self.z,self.brick = x,y,z,b
    def is_supported(self): return self.z==1 or (blocks.get((self.x,self.y,self.z-1), self).brick != self.brick)

class Brick:
    def __init__(self,s,e): self.blocks = [Block(x,y,z,self) for x in absrange(s[0],e[0]) for y in absrange(s[1],e[1]) for z in absrange(s[2],e[2])]
    def is_falling(self): return not any(b.is_supported() for b in self.blocks)

def collapse(bricks):
    dropped = set()
    for br in bricks:
        while br.is_falling():
            for b in br.blocks:
                blocks[b.x,b.y,b.z-1] = blocks.pop((b.x,b.y,b.z))
                b.z -= 1
            dropped.add(br)
    return len(dropped)

aocdata = sorted([[int(x) for x in re.findall('(\d+)', line)] for line in open("input1")], key=lambda a:min(a[2],a[5]))
bricks = [Brick((a,b,c),(d,e,f)) for a,b,c,d,e,f in aocdata]
blocks = {(b.x,b.y,b.z): b for br in bricks for b in br.blocks}
collapse(bricks)
saveloc = {b:k for k,b in blocks.items()}

part1 = part2 = 0
for i,br in enumerate(bricks):
    for b in saveloc: b.x,b.y,b.z = saveloc[b]
    blocks = {saveloc[b]:b for b in saveloc if b.brick != br}
    dropped = collapse(bricks[:i]+bricks[i+1:])
    part1 += dropped==0
    part2 += dropped
print(f"part1={part1}")