from collections import defaultdict
digital_logic = input()
K, M = map(int, input().split())
N=len(digital_logic)
d=defaultdict(int)

st,end=0,K-1
now=int(digital_logic[st:end+1],2)
d[now]+=1
tmp=(1<<K)-1
while end+1<N:
    end+=1
    now=((now<<1)&tmp)|int(digital_logic[end])
    d[now]+=1
for k,v in d.items():
    if v>=M:
        print(1)
        break
else:
    print(0)