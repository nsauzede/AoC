ROCK='A'
PAPER='B'
SCISSOR='C'
LOOSE='X'
DRAWS='Y'
WIN='Z'
def score0(l:int,r:int)->int:
    # you play r
    score=0
    if l==1:
        if r==1:score+=3#draw
        elif r==2:score+=6#won
        elif r==3:score+=0#lost
    elif l==2:
        if r==1:score+=0#lost
        elif r==2:score+=3#draw
        elif r==3:score+=6#won
    elif l==3:
        if r==1:score+=6#won
        elif r==3:score+=3#draw
    score+=r
    return score

conv={
    'A':1,'B':2,'C':3,
    'X':1,'Y':2,'Z':3,
}
def score(l:int,r:int)->int:
    l=conv[l]
    r=conv[r]
    return score0(l,r)

def run1(inp:str)->int:
    s=0
    for l in inp.splitlines():
        #print(f"l={l}")
        l,r=l.split(" ")
        #print(f"l={l} r={r}")
        s+=score(l,r)
        #print(f"score={score}")
    return s

# 1 Rock 2 Paper 3 Scissor
# 0 lost 3 draw 6 won
# X loose Y draw Z win
def play(l:str,r:str)->str:
    if r==LOOSE:
        if l==ROCK:r=SCISSOR
        elif l==PAPER:r=ROCK
        elif l==SCISSOR:r=PAPER
    elif r==DRAWS:
        if l==ROCK:r=ROCK
        elif l==PAPER:r=PAPER
        elif l==SCISSOR:r=SCISSOR
    elif r==WIN:
        if l==ROCK:r=PAPER
        elif l==PAPER:r=SCISSOR
        elif l==SCISSOR:r=ROCK
    return r

def run2(inp:str)->int:
    s=0
    for l in inp.splitlines():
        #print(f"l={l}")
        l,r=l.split(" ")
        #print(f"l={l} r={r}")
        s+=score(l,play(l,r))
        #print(f"score={score}")
    return s

import unittest
def load(name)->str:
    f=open(name,"rt")
    return f.read()
res0 = 15
res1 = 12740
res0_2 = 12
res1_2 = 11980
class T(unittest.TestCase):
    def test_play_A_X(self):
        self.assertEqual(SCISSOR, play(ROCK,LOOSE))
    def test_play_B_X(self):
        self.assertEqual(ROCK, play(PAPER,LOOSE))
    def test_play_C_X(self):
        self.assertEqual(PAPER, play(SCISSOR,LOOSE))
    def test_play_A_Y(self):
        self.assertEqual(ROCK, play(ROCK,DRAWS))
    def test_play_B_Y(self):
        self.assertEqual(PAPER, play(PAPER,DRAWS))
    def test_play_C_Y(self):
        self.assertEqual(SCISSOR, play(SCISSOR,DRAWS))
    def test_play_A_Z(self):
        self.assertEqual(PAPER, play(ROCK,WIN))
    def test_play_B_Z(self):
        self.assertEqual(SCISSOR, play(PAPER,WIN))
    def test_play_C_Z(self):
        self.assertEqual(ROCK, play(SCISSOR,WIN))

    def test_score0_1_1(self):
        self.assertEqual(4, score0(1,1))#draw
    def test_score0_1_2(self):
        self.assertEqual(8, score0(1,2))#won
    def test_score0_1_3(self):
        self.assertEqual(3, score0(1,3))#lost
    def test_score0_2_1(self):
        self.assertEqual(1, score0(2,1))#lost
    def test_score0_2_2(self):
        self.assertEqual(5, score0(2,2))#draw
    def test_score0_2_3(self):
        self.assertEqual(9, score0(2,3))#won
    def test_score0_3_1(self):
        self.assertEqual(7, score0(3,1))#won
    def test_score0_3_2(self):
        self.assertEqual(2, score0(3,2))#lost
    def test_score0_3_3(self):
        self.assertEqual(6, score0(3,3))#draw

    def test_inp0ReturnsRes0(self):
        inp0=load("input0")
        self.assertEqual(res0, run1(inp0))
    def test_inp1ReturnsRes1(self):
        inp1=load("input1")
        self.assertEqual(res1, run1(inp1))
    def test_inp0ReturnsRes0_2(self):
        inp0=load("input0")
        self.assertEqual(res0_2, run2(inp0))
    def test_inpReturnsRes1_2(self):
        inp1=load("input1")
        self.assertEqual(res1_2, run2(inp1))
