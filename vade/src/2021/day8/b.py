f=open('input')
inps=f.readlines()
total=0
for inp in inps:
    patterns_,outputs_=inp.split('|')
    patterns=patterns_.split()
    outputs=outputs_.split()
    l0=patterns
    l=l0.copy()
    l.sort(key = lambda x: len(x))
    # print(l)
    dic=[]
    four=[]
    one=[]
    twoseen=False
    fiveseen=False
    threeseen=False
    nineseen=False
    sixseen=False
    zeroseen=False
    for e in l:
        if len(e)==2:# 1
            # print(f'e={e} 2')
            x={}
            x[e[0]]='c'
            x[e[1]]='f'
            dic+=[x]
            x={}
            x[e[0]]='f'
            x[e[1]]='c'
            dic+=[x]
            one+=[e[0]]
            one+=[e[1]]
            # print(f'2dic={dic}')
        elif len(e)==3:# 7
            # print(f'e={e} 3')
            for d in dic:
                for c in e:
                    if c not in d:
                        d[c]='a'
                        # print(f'{c} known 3')
                        break
            # print(f'3dic={dic}')
        elif len(e)==4:# 4
            # print(f'e={e} 4')
            dic+=[dic[0].copy()]
            dic+=[dic[1].copy()]
            t=['b','d']
            for c in e:
                if c not in dic[0]:
                    dic[0][c]=t[0]
                    dic[1][c]=t[0]
                    dic[2][c]=t[1]
                    dic[3][c]=t[1]
                    t=['d','b']
                    four+=[c]
                    # print(f'{c} known 4')
            # print(f'4dic={dic}')
        elif len(e)==5:# 3 or 2 or 5
            # print(f'e={e} 5')
            if not fiveseen and four[0]in e and four[1]in e:
                # print('is 5')
                fiveseen=True
                for c in 'abcdefg':
                    if c not in e:
                        if c in one:
                            v='c'
                            # print(f'{c} must be {v}')
                            for i,d in enumerate(dic):
                                if c in d and d[c]!=v:
                                    # raise Exception(f'BOOM {i}')
                                    del dic[i]
                                d[c]=v
                        else:
                            v='e'
                            # print(f'{c} must be {v}')
                            for i,d in enumerate(dic):
                                if c in d and d[c]!=v:
                                    raise Exception(f'BOOM {i}')
                                    # del dic[i]
                                d[c]=v
            elif not threeseen and one[0]in e and one[1] in e:
                # print('is 3')
                threeseen=True
                for c in 'abcdefg':
                    if c not in e:
                        if c in four:
                            v='b'
                            # print(f'{c} must be {v}')
                            for i,d in enumerate(dic):
                                if c in d and d[c]!=v:
                                    # raise Exception(f'BOOM {i}')
                                    del dic[i]
                                d[c]=v
                        else:
                            v='e'
                            # print(f'{c} must be {v}')
                            for i,d in enumerate(dic):
                                if c in d and d[c]!=v:
                                    raise Exception(f'BOOM {i}')
                                d[c]=v
            elif not twoseen:# 2
                # print('is 2')
                twoseen=True
                for c in 'abcdefg':
                    if c not in e:
                        if c in one:
                            v='f'
                            # print(f'{c} must be {v}')
                            for i,d in enumerate(dic):
                                if c in d and d[c]!=v:
                                    # raise Exception(f'BOOM {i}')
                                    del dic[i]
                                d[c]=v
                        else:
                            v='b'
                            # print(f'{c} must be {v}')
                            for i,d in enumerate(dic):
                                if c in d and d[c]!=v:
                                    # raise Exception(f'BOOM {i}')
                                    del dic[i]
                                d[c]=v
            # print(f'5dic={dic}')
        elif len(e)==6:# 9, 6 or 0
            # print(f'e={e} 6')
            for c in e:
                if c not in dic[0]:
                    # print(f'{c} must be g')
                    for d in dic:
                        d[c]='g'
                    break
            # print(f'6dic={dic}')
    # print(dic)
    digits=['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    outs=[]
    outs+=outputs
    output=''
    for outp in outs:
        # print(f'testing {outp}')
        seen={}
        for d in dic:
            s=''
            for c in outp:
                if c not in d:s+='.'
                else:s+=d[c]
            s=''.join(sorted(s))
            # print(f's={s}')
            if s in digits:dig=digits.index(s)
            else:dig='0'
            if len(outp)!=6 and dig=='0':
                continue
            if len(outp)==8 and dig!='8':
                continue
            if outp in seen:continue
            # print(f"s={outp} dig={dig}")
            output+=str(dig)
            seen[outp]=1
    out=int(output)
    print(f'output={out}')
    total+=out
print(f'total={total}')
