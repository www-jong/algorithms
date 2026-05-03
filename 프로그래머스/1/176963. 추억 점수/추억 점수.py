def solution(name, yearning, photo):
    answer=[]
    d={name[i]:yearning[i] for i in range(len(name))}
    for i in photo:
        answer.append(sum([d[j] for j in i if j in d]))
    return answer