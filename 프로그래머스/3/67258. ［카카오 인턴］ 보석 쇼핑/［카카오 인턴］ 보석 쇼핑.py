def solution(gems):
    N=len(gems)
    s=list(set(gems))
    d={}
    for i in range(len(s)):
        d[s[i]]=i
    now=[0]*len(s)
    for i in gems:
        now[d[i]]+=1
    st=0
    end=N-1
    while st<end:
        le,ri=d[gems[st]],d[gems[end]]
        if now[ri]>=2:
            now[ri]-=1
            end-=1
        elif now[le]>=2:
            now[le]-=1
            st+=1
        else:
            break
    answer=[st+1,end+1]
    while st<end:
        le=d[gems[st]]
        now[le]-=1
        st+=1
        while now[le]==0 and end<N-1:
            end+=1
            now[d[gems[end]]]+=1
        if now[le]==0:
            break
        if end-st<answer[1]-answer[0]:
            answer=[st+1,end+1]
    return answer