import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
stk=[]
res=0
dic={}
high=0
def dict_ctl(val,type=0):
    global dic
    if type:
        if val not in dic:
            dic[val]=1
        else:
            dic[val]+=1
    else:
        if val in dic:
            del dic[val]

for i in range(N):
    high=max(high,li[i])
    if not stk:
        stk.append((li[i],i))
        dict_ctl(li[i],1)
        continue

    if li[i]<stk[-1][0]: # 더 작은키가 들어올때,
        #stk.append((li[i],i))
        res+=1
    elif li[i]==stk[-1][0]:
        if stk:
            if high==li[i]:
                res+=dic[li[i]]
            else:
                res+=dic[li[i]]+1
    else: # 더 큰키가 들어올 때,
        while stk:
            if stk[-1][0]<li[i]:
                dict_ctl(stk[-1][0],0)
                stk.pop()
                res+=1
            elif stk[-1][0]==li[i]:
                if high==li[i]:
                    res+=dic[li[i]]
                else:
                    res+=dic[li[i]]+1
                break
            else:
                res+=1
                break

    dict_ctl(li[i],1)
    stk.append((li[i],i))
print(res)