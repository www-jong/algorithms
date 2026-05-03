def solution(keymap, targets):
    answer = []
    d={}
    for i in keymap:
        for j in range(len(i)):
            if i[j] in d:
                d[i[j]]=min(d[i[j]],j+1)
            else:
                d[i[j]]=j+1
    for i in targets:
        now=0
        for j in i:
            if j not in d:
                answer.append(-1)
                break
            now+=d[j]
        else:
            answer.append(now)    
    return answer
