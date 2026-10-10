def solution(sequence):
    li=[]
    c=1
    for i in sequence:
        li.append(i*c)
        c*=-1
    dp=[0]*len(li)
    answer=max(li[0],-li[0])
    now=[li[0],-li[0]]
    for x in li[1:]:
        now=[max(x,now[0]+x),max(-x,now[1]-x)]
        answer=max(answer,now[0],now[1])
    
    return answer