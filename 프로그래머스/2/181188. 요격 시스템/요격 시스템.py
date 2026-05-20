def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    now=-1
    for x,y in targets:
        if x<now<y:
            continue
        else:
            answer+=1
            now=y-0.5
    return answer