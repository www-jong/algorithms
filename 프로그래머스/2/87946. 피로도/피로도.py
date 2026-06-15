from itertools import permutations
def solution(k, dungeons):
    answer = 0
    N=len(dungeons)
    
    for i in permutations(dungeons,len(dungeons)):
        tmp=[k,0]
        for a,b in i:
            if a<=tmp[0]:
                tmp[0]-=b
                tmp[1]+=1
        answer=max(answer,tmp[1])
    return answer