def solution(sequence, k):
    answer = [10**9,10**10]
    st,v=0,0
    for end in range(len(sequence)):
        v+=sequence[end]
        while v>k:
            v-=sequence[st]
            st+=1
        if v==k:
            if answer[1]-answer[0]>end-st:
                answer=[st,end]
        
    return answer