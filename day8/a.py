f=open('input')
ll=f.readlines()
cnt=0
for l in ll:
    if l=='' or l==None:break
    p,o=l.replace('\n','').split('|')
    patterns=p.split()
    output=o.split()
    # print(f'p={patterns} o={output}')
    # for e in patterns:
    #     if len(e)==2 or len(e)==3 or len(e)==4 or len(e)==7:
    #         # print(e)
    #         cnt+=1
    for e in output:
        if len(e)==2 or len(e)==3 or len(e)==4 or len(e)==7:
            # print(e)
            cnt+=1
print(f'cnt={cnt}')
