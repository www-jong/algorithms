def solution(e, starts):
    answer = [0]*len(starts)
    li=[0]*(e+1)
    for i in range(1,int(e**0.5)+1):
        li[i*i]+=1
        for j in range(i*(i+1),e+1,i):
            li[j]+=2
    tmp=[]
    for i in range(len(starts)):
        tmp.append((starts[i],i))
    tmp.sort(key=lambda x:-x[0])
    now=[li[e],e]
    idx=e
    for i,j in tmp:
        while idx!=i:
            idx-=1
            if li[idx]>=now[0]:
                now=[li[idx],idx]
        answer[j]=now[1]
    return answer