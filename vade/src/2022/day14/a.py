def _flow(m:list,u:list):
    w,h=len(m),len(m[0])
    if not self._unit:return
    rest=0
    while self._unit and not self.over:

        x,y=u
        if x<0 or x>=w-1 or y>=h-1:
            return -rest-1
        next=m[y+1][x]
        if next=='.':
            u[1]+=1
            continue
        elif next=='#':
            pass
        continue
        rest=[6,8]
        self.map[rest[1]][rest[0]]='o'
        self.rests+=[rest]
        self._unit=None
    return rest

def flow(m:list, u:list):
    if can_flow(m,u):
        return flow(m,u)

# if can flow, returns next u to flow to
# if next u is outside m, means fall forever
# else return None (current u can rest)
def can_flow(m:list, u:list)->bool:
    x,y=u
    print(f"can_flow x={x} y={y}")
    w,h=len(m),len(m[0])
    if x<0 or x>=w-1 or y>=h-1:
        return None
    next=m[y+1][x]
    if next=='.':
        return [x,y+1]
    elif next=='#':
        next2=m[y+2][x-1]
        if next=='.':
            return can_flow(m, [x-1,y+1])
    raise Exception("Kaboom")

import unittest
m0=[
['.','+','.'],
['.','.','.'],
['#','#','#'],
]
m1=[
['.','.','+','.'],
['.','.','.','.'],
['.','.','#','.'],
['#','#','#','#'],
]
def source(m:list,src='+')->list:return [[l.index(src),i] for i,l in enumerate(m) if src in l][0]
@unittest.skip
class TestCreation(unittest.TestCase):
    def test_canFlowOneFreeUnit(self):
        m=m0
        u=source(m)
        print(f"u={u}")
        r=can_flow(m,u)
        self.assertEqual([1,1],r)

    def test_twoFlowsReturnNone(self):
        m=m0
        u=source(m)
        r=can_flow(m,u)
        self.assertEqual([1,1],r)
        r=can_flow(m,r)
        self.assertEqual(None,r)

@unittest.skip
class TestFlowLeft(unittest.TestCase):
    def test_flowGoingLeft(self):
        m=m1
        u=source(m)
        print("calling can_flow")
        r=can_flow(m,u)
        self.assertEqual([2,1],r)
        print("calling can_flow")
        r=can_flow(m,r)
        self.assertEqual([1,2],r)
        print("calling can_flow")
        r=can_flow(m,r)
        self.assertEqual(None,r)

    def Ztest_createGame(self):
        m=[
['.','.','.'],
['.','.','.'],
['#','#','#'],
]
        rest=_flow(m,[1,0])
        print(f"rest={rest} m={m}")
        self.assertEqual(1,rest)

class T0(unittest.TestCase):
    def test_010(self):
        self.assertEqual(1,1)

