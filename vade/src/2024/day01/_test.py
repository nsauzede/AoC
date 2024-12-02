
input0_ = """3   4
4   3
2   5
1   3
3   9
3   3
"""
input0__=[
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3]
]
def mkinput(inp)->list:
    l1 = []
    l2 = []
    for li in inp.splitlines():
        l = [int(e) for e in li.split('   ')]
        l1 += [l[0]]
        l2 += [l[1]]
    return [l1, l2]
def test01():
    input0 = input0__
    l1,l2 = input0
    l1 = sorted(l1)
    l2 = sorted(l2)
    cnt = 0
    for i in range(len(l1)):
        cnt += abs(l1[i] - l2[i])
    print(f"{cnt=}")
    assert cnt == 11+1*0
def getinput():
    inp = ""
    with open('input1', 'rt') as f:
        inp = mkinput(f.read())
    return inp
def test1():
    input0 = getinput()
    l1,l2 = input0
    l1 = sorted(l1)
    l2 = sorted(l2)
    cnt = 0
    for i in range(len(l1)):
        cnt += abs(l1[i] - l2[i])
    print(f"{cnt=}")
    assert cnt == 1189304
def test02():
    input0 = input0__
    l1,l2 = input0
    cnt = 0
    for e in l1:
        cnt += e * l2.count(e)
    assert cnt == 31+1*0
def test02():
    input0 = getinput()
    l1,l2 = input0
    cnt = 0
    for e in l1:
        cnt += e * l2.count(e)
    assert cnt == 24349736+1*0
