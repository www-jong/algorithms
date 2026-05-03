def solution(data, ext, val_ext, sort_by):
    answer = []
    d={'code':0,'date':1,'maximum':2,'remain':3}
    for i in data:
        if i[d[ext]]<val_ext:
            answer.append(i)
    print(answer)
    answer.sort(key=lambda x:x[d[sort_by]])
    return answer