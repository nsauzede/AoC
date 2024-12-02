
input0__=[
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]
input0_ = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
def is_safe(r: list)->bool:
    slope = 0
    last = r[0]
    safe = True
    for l in r[1:]:
        #print(f"{l=}")
        if last > l:
            if slope > 0:
                print(f"ERROR: slope changed from inc to dec {d}")
                safe = False
                break
            slope = -1
            d = last - l
            if d > 3:
                print(f"ERROR: dec delta too high {d}")
                safe = False
                break
        elif last < l:
            if slope < 0:
                print(f"ERROR: slope changed from dec to inc {d}")
                safe = False
                break
            slope = 1
            d = l - last
            if d > 3:
                print(f"ERROR: inc delta too high {d}")
                safe = False
                break
        else:
            print(f"ERROR: same consecutive level {l}")
            safe = False
            break
        last = l
    return safe
def count_safe(inp: list)->int:
    ret = 0
    for i,r in enumerate(inp):
        print(f"L{i+1:4} {r=} ", end="")
        safe = is_safe(r)
        if safe:
            ret += 1
            print(f"SAFE")
            #print(f"{r=} SAFE L{i+1}")
        else:
            #print(f"UNSAFE")
            pass
    return ret
def count_safe2(inp: list)->int:
    ret = 0
    for i,r in enumerate(inp):
        print(f"L{i+1:4} {r=} ", end="")
        safe = is_safe(r)
        if safe:
            ret += 1
            print(f"SAFE")
            #print(f"{r=} SAFE L{i+1}")
            continue
        else:
            #print(f"UNSAFE")
            pass
        for j in range(len(r)):
            safe = is_safe(r[:j] + r[j + 1:])
            if safe:
                ret += 1
                print(f"SAFE {j=}")
                #print(f"{r=} SAFE L{i+1}")
                break
    return ret
def test01__():
    ret = count_safe(input0__)
    assert ret == 2
def mkinput(inp)->list:
    l1 = []
    for li in inp.splitlines():
        #print(f"{li=}")
        l = [int(e) for e in li.split(' ')]
        #print(f"{l=}")
        l1 += [l]
    return l1
def getinput(fname:str):
    inp = ""
    with open(fname, 'rt') as f:
        inp = mkinput(f.read())
    return inp
def test01_():
    ret = count_safe(mkinput(input0_))
    assert ret == 2
def test01():
    ret = count_safe(getinput('input0'))
    assert ret == 2
def test1():
    ret = count_safe(getinput('input1'))
    assert ret == 549

def test02():
    ret = count_safe2(getinput('input0'))
    assert ret == 4
def test2():
    ret = count_safe2(getinput('input1'))
    assert ret == 589

# The bis variants are for GH user nicolas-sauzede
def test1bis():
    ret = count_safe(getinput('input1bis'))
    assert ret == 572
def test2bis():
    ret = count_safe2(getinput('input1bis'))
    assert ret == 612
