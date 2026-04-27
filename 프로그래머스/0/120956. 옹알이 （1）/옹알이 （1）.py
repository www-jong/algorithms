def solution(babbling):
    answer = 0
    d=['aya','ye','woo','ma']
    for i in babbling:
        for j in d:
            i=i.replace(j,'@')
        i=i.replace('@','')
        if not i:
            answer+=1
        print(i)
    return answer