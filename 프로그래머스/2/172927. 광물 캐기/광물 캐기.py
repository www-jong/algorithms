def solution(picks, minerals):
    answer = 0
    li=[]
    for i in range(0,min(len(minerals),sum(picks)*5),5):
        tmp=[]
        for j in minerals[i:min(i+5,len(minerals))]:
            tmp.append(25 if j=='diamond' else (5 if j=='iron' else 1))
        li.append(tmp)
    li.sort(key=lambda x:-sum(x))
    for i in li:
        pick=0
        if picks[0]:
            picks[0]-=1
            pick=25
        elif picks[1]:
            picks[1]-=1
            pick=5
        elif picks[2]:
            pick=1
        else:
            break
        answer+=sum(max(j//pick,1) for j in i)
    return answer