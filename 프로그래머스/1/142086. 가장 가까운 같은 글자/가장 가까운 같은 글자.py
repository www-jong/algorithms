def solution(s):
    answer = []
    d={}
    for i,j in enumerate(s):
        if j not in d:
            answer.append(-1)
            d[j]=i
        else:
            answer.append(i-d[j])
            d[j]=i
    return answer