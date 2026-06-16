def solution(topping):
    answer=0
    all={}
    a=0
    for i in topping:
        if i in all:
            all[i]+=1
        else:
            all[i]=1
            a+=1
    now={}
    b=0
    for i in range(len(topping)):
        if topping[i] in now:
            now[topping[i]]+=1
        else:
            now[topping[i]]=1
            b+=1
        if all[topping[i]]==1:
            del all[topping[i]]
            a-=1
        else:
            all[topping[i]]-=1
        if a==b:
            answer+=1
    return answer