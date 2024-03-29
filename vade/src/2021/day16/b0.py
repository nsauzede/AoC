def h2b(packet):
    pack=''
    for q in packet:
        n=int(q,16)
        for i in range(4):
            pack+=str((n&(1<<(4-i-1)))>>(4-i-1))
    return pack

versions=0
stack=[]
def decode(packet,pos=0):
    global versions
    global stack
    pos0=pos
    # print(f'packet={packet} pos={pos}')
    while pos<len(packet)-7:
        print(f'pos={pos}')
        v=int(packet[pos:pos+3],2)
        pos+=3
        t=int(packet[pos:pos+3],2)
        pos+=3
        print(f'version={v} type={t}: ',end='')
        versions+=v
        if t==4:#literal
            print(f'literal: (pos={pos}) ',end='')
            v=''
            while pos<=len(packet)-5:
                print(f'pos={pos}')
                n=int(packet[pos:pos+5],2)
                print(f'n={n}')
                v+=f'{n&0xf:x}'
                pos+=5
                if n&0x10==0:break
            print(f'v={v}')
#1100001000000000101101000000101010000010
#0123456789012345678901234567890123456789
#0         1         2         3
            v=int(v,16)
            print(f'v={v}')
            stack+=[v]
        else:#operator?
            if t==0:
                op='SUM'
            elif t==1:
                op='PROD'
            elif t==2:
                op='MIN'
            elif t==3:
                op='MAX'
            elif t==5:
                op='GT'
            elif t==6:
                op='LT'
            elif t==7:
                op='EQ'
            else:
                raise Exception(f'operator type {t} notimp')
            print(op)
            gstack=stack.copy()
            stack=[op]
            i=int(packet[pos:pos+1],2)
            pos+=1
            if i==0:
                l15=int(packet[pos:pos+15],2)
                # print(f'n={n}')
                print(f'operator lenID={i} len15={l15} ',end='')
                # print(f'len15={l15}')
                pos+=15
                while pos<len(packet)-7:
                    # print(f'decoding at pos={pos}')
                    pos=decode(packet,pos)
                    # print(f'decoding returned pos={pos}')
            else:
                n11=int(packet[pos:pos+11],2)
                # print(f'n={n}')
                print(f'operator lenID={i} num11={n11}')
                pos+=11
                for i in range(n11):
                    # print(f'decoding at pos={pos}')
                    pos=decode(packet,pos)
                    # print(f'decoding returned pos={pos}')
            gstack+=[stack]
            stack=gstack
        if pos0!=0:break
    return pos

def compute0(stack):
    pos=0
    while pos < len(stack):
        if stack[pos]=='SUM':
            pos+=1
            st=[]
            v=0
            while pos<len(stack):
                if type(stack[pos])!=int:break
                v+=stack[pos]
                pos+=1
            print(f'res={v}')
        elif stack[pos]=='PROD':
            pos+=1
            st=[]
            v=1
            while pos<len(stack):
                if type(stack[pos])!=int:break
                v*=stack[pos]
                pos+=1
            print(f'res={v}')
        elif stack[pos]=='MIN':
            pos+=1
            st=[]
            while pos<len(stack):
                if type(stack[pos])!=int:break
                st+=[stack[pos]]
                pos+=1
            v=min(st)
            print(f'res={v}')
        elif stack[pos]=='MAX':
            pos+=1
            st=[]
            while pos<len(stack):
                if type(stack[pos])!=int:break
                st+=[stack[pos]]
                pos+=1
            v=max(st)
            print(f'res={v}')
        elif stack[pos]=='LT':
            pos+=1
            v=int(stack[pos]<stack[pos+1])
            pos+=2
            print(f'res={v}')
        elif stack[pos]=='GT':
            pos+=1
            v=int(stack[pos]>stack[pos+1])
            pos+=2
            print(f'res={v}')
        elif stack[pos]=='EQ':
            pos+=1
            v=int(stack[pos]==stack[pos+1])
            pos+=2
            print(f'res={v}')
        else:
            raise Exception(f'operator {stack[pos]} notimp')

def compute1(stack,pos=0):
    pos0=pos
    v=None
    while pos < len(stack):
        if stack[pos]=='SUM':
            pos+=1
            st=[]
            v=0
            while pos<len(stack):
                if type(stack[pos])!=int:break
                v+=stack[pos]
                pos+=1
            print(f'res={v}')
        elif stack[pos]=='PROD':
            pos+=1
            st=[]
            v=1
            while pos<len(stack):
                if type(stack[pos])!=int:break
                v*=stack[pos]
                pos+=1
            print(f'res={v}')
        elif stack[pos]=='MIN':
            pos+=1
            st=[]
            while pos<len(stack):
                if type(stack[pos])!=int:break
                st+=[stack[pos]]
                pos+=1
            v=min(st)
            print(f'res={v}')
        elif stack[pos]=='MAX':
            pos+=1
            st=[]
            while pos<len(stack):
                if type(stack[pos])!=int:break
                st+=[stack[pos]]
                pos+=1
            v=max(st)
            print(f'res={v}')
        elif stack[pos]=='LT':
            pos+=1
            pos,v1=compute(stack,pos)
            pos,v2=compute(stack,pos)
            v=int(v1<v2)
            print(f'res={v}')
        elif stack[pos]=='GT':
            pos+=1
            pos,v1=compute(stack,pos)
            pos,v2=compute(stack,pos)
            v=int(v1>v2)
            print(f'res={v}')
        elif stack[pos]=='EQ':
            pos+=1
            pos,v1=compute(stack,pos)
            pos,v2=compute(stack,pos)
            v=int(v1==v2)
            print(f'res={v}')
        else:
            raise Exception(f'operator {stack[pos]} notimp')
        if pos0!=0:break
    return pos,v

def compute(stack):
    v=None
    while pos < len(stack):
        if stack[pos]=='SUM':
            pos+=1
            st=[]
            v=0
            while pos<len(stack):
                if type(stack[pos])!=int:break
                v+=stack[pos]
                pos+=1
            print(f'res={v}')
        elif stack[pos]=='PROD':
            pos+=1
            st=[]
            v=1
            while pos<len(stack):
                if type(stack[pos])!=int:break
                v*=stack[pos]
                pos+=1
            print(f'res={v}')
        elif stack[pos]=='MIN':
            pos+=1
            st=[]
            while pos<len(stack):
                if type(stack[pos])!=int:break
                st+=[stack[pos]]
                pos+=1
            v=min(st)
            print(f'res={v}')
        elif stack[pos]=='MAX':
            pos+=1
            st=[]
            while pos<len(stack):
                if type(stack[pos])!=int:break
                st+=[stack[pos]]
                pos+=1
            v=max(st)
            print(f'res={v}')
        elif stack[pos]=='LT':
            pos+=1
            pos,v1=compute(stack,pos)
            pos,v2=compute(stack,pos)
            v=int(v1<v2)
            print(f'res={v}')
        elif stack[pos]=='GT':
            pos+=1
            pos,v1=compute(stack,pos)
            pos,v2=compute(stack,pos)
            v=int(v1>v2)
            print(f'res={v}')
        elif stack[pos]=='EQ':
            pos+=1
            pos,v1=compute(stack,pos)
            pos,v2=compute(stack,pos)
            v=int(v1==v2)
            print(f'res={v}')
        else:
            raise Exception(f'operator {stack[pos]} notimp')
        if pos0!=0:break
    return pos,v

packets=[]
# packets+=['D2FE28']
# packets+=['38006F45291200']
# packets+=['EE00D40C823060']
# packets+=['8A004A801A8002F478']
# packets+=['620080001611562C8802118E34']
# packets+=['C0015000016115A2E0802F182340']
# packets+=['A0016C880162017C3686B18A3D4780']
f=open('input')
# packets+=[f.readline().rstrip()]
# packets+=['6053231004C12DC26D00526BEE728D2C013AC7795ACA756F93B524D8000AAC8FF80B3A7A4016F6802D35C7C94C8AC97AD81D30024C00D1003C80AD050029C00E20240580853401E98C00D50038400D401518C00C7003880376300290023000060D800D09B9D03E7F546930052C016000422234208CC000854778CF0EA7C9C802ACE005FE4EBE1B99EA4C8A2A804D26730E25AA8B23CBDE7C855808057C9C87718DFEED9A008880391520BC280004260C44C8E460086802600087C548430A4401B8C91AE3749CF9CEFF0A8C0041498F180532A9728813A012261367931FF43E9040191F002A539D7A9CEBFCF7B3DE36CA56BC506005EE6393A0ACAA990030B3E29348734BC200D980390960BC723007614C618DC600D4268AD168C0268ED2CB72E09341040181D802B285937A739ACCEFFE9F4B6D30802DC94803D80292B5389DFEB2A440081CE0FCE951005AD800D04BF26B32FC9AFCF8D280592D65B9CE67DCEF20C530E13B7F67F8FB140D200E6673BA45C0086262FBB084F5BF381918017221E402474EF86280333100622FC37844200DC6A8950650005C8273133A300465A7AEC08B00103925392575007E63310592EA747830052801C99C9CB215397F3ACF97CFE41C802DBD004244C67B189E3BC4584E2013C1F91B0BCD60AA1690060360094F6A70B7FC7D34A52CBAE011CB6A17509F8DF61F3B4ED46A683E6BD258100667EA4B1A6211006AD367D600ACBD61FD10CBD61FD129003D9600B4608C931D54700AA6E2932D3CBB45399A49E66E641274AE4040039B8BD2C933137F95A4A76CFBAE122704026E700662200D4358530D4401F8AD0722DCEC3124E92B639CC5AF413300700010D8F30FE1B80021506A33C3F1007A314348DC0002EC4D9CF36280213938F648925BDE134803CB9BD6BF3BFD83C0149E859EA6614A8C']
#0110000001010011001000110001000000000100110000010010110111000010011011010000000001010010011010111110111001110010100011010010110000000001001110101100011101111001010110101100101001110101011011111001001110110101001001001101100000000000000010101010110010001111111110000000101100111010011110100100000000010110111101101000000000101101001101011100011111001001010011001000101011001001011110101101100000011101001100000000001001001100000000001101000100000000001111001000000010101101000001010000000000101001110000000000111000100000001001000000010110000000100001010011010000000001111010011000110000000000110101010000000000111000010000000000110101000000000101010001100011000000000011000111000000000011100010000000001101110110001100000000001010010000000000100011000000000000000001100000110110000000000011010000100110111001110100000011111001111111010101000110100100110000000001010010110000000001011000000000000001000010001000100011010000100000100011001100000000000000100001010100011101111000110011110000111010100111110010011100100000000010101011001110000000000101111111100100111010111110000110111001100111101010010011001000101000101010100000000100110100100110011100110000111000100101101010101000101100100011110010111101111001111100100001010101100000001000000001010111110010011100100001110111000110001101111111101110110110011010000000001000100010000000001110010001010100100000101111000010100000000000000001000010011000001100010001001100100011100100011000000000100001101000000000100110000000000000100001111100010101001000010000110000101001000100000000011011100011001001000110101110001101110100100111001111100111001110111111110000101010001100000000000100000101001001100011110001100000000101001100101010100101110010100010000001001110100000000100100010011000010011011001111001001100011111111101000011111010010000010000000001100100011111000000000010101001010011100111010111101010011100111010111111110011110111101100111101111000110110110010100101011010111100010100000110000000000101111011100110001110010011101000001010110010101010100110010000000000110000101100111110001010010011010010000111001101001011110000100000000011011001100000000011100100001001011000001011110001110010001100000000011101100001010011000110000110001101110001100000000011010100001001101000101011010001011010001100000000100110100011101101001011001011011100101110000010010011010000010000010000000001100000011101100000000010101100101000010110010011011110100111001110011010110011001110111111111110100111110100101101101101001100001000000000101101110010010100100000000011110110000000001010010010101101010011100010011101111111101011001010100100010000000000100000011100111000001111110011101001010100010000000001011010110110000000000011010000010010111111001001101011001100101111110010011010111111001111100011010010100000000101100100101101011001011011100111001110011001111101110011101111001000001100010100110000111000010011101101111111011001111111100011111011000101000000110100100000000011100110011001110011101110100100010111000000000010000110001001100010111110111011000010000100111101011011111100111000000110010001100000000001011100100010000111100100000000100100011101001110111110000110001010000000001100110011000100000000011000100010111111000011011110000100010000100000000011011100011010101000100101010000011001010000000000000101110010000010011100110001001100111010001100000000010001100101101001111010111011000000100010110000000000010000001110010010010100111001001001010111010100000000011111100110001100110001000001011001001011101010011101000111100000110000000001010010100000000001110010011001110010011100101100100001010100111001011111110011101011001111100101111100111111100100000111001000000000101101101111010000000001000010010001001100011001111011000110001001111000111011110001000101100001001110001000000001001111000001111110010001101100001011110011010110000010101010000101101001000000000110000000110110000000001001010011110110101001110000101101111111110001111101001101001010010100101100101110101110000000010001110010110110101000010111010100001001111110001101111101100001111100111011010011101101010001101010011010000011111001101011110100100101100000010000000001100110011111101010010010110001101001100010000100010000000001101010110100110110011111010110000000001010110010111101011000011111110100010000110010111101011000011111110100010010100100000000001111011001011000000000101101000110000010001100100100110001110101010100011100000000101010100110111000101001001100101101001111001011101101000101001110011001101001001001111001100110111001100100000100100111010010101110010000000100000000000011100110111000101111010010110010010011001100010011011111111001010110100100101001110110110011111011101011100001001000100111000001000000001001101110011100000000011001100010001000000000110101000011010110000101001100001101010001000000000111111000101011010000011100100010110111001110110000110001001001001110100100101011011000111001110011000101101011110100000100110011000000000111000000000000000100001101100011110011000011111110000110111000000000000010000101010000011010100011001111000011111100010000000001111010001100010100001101001000110111000000000000000010111011000100110110011100111100110110001010000000001000010011100100111000111101100100100010010010010110111101111000010011010010000000001111001011100110111101011010111111001110111111110110000011110000000001010010011110100001011001111010100110011000010100101010001100
#                        
#                      VVVTTTILLLLLLLLLLLLLLL
#V=6 T=1 I=0 L=0x4c=76
#VVVTTTILLLLLLLLLLLLLLL
#V=3 T=0 I=0 L=001010011001000=0x14c8=5320

packets+=['C200B40A82']
# packets+=['04005AC33890']
# packets+=['880086C3E88112']
# packets+=['CE00C43D881120']
# packets+=['D8005AC2A8F0']
# packets+=['F600BC2D8F']
# packets+=['9C005AC2F8F0']
# packets+=['9C0141080250320F1802104A08']
#
for packet in packets:
    print(f'packet={packet}')
    versions=0
    decode(h2b(packet))
    print(f'versions={versions}')
    print(f'stack={stack}')
_,v=compute(stack)
print(f'final v={v}')
