def solution(numLog):
    answer = ''
    b=numLog[0]
    for a in numLog[1:]:
        if a-b==1:
            answer+='w'
        elif a-b==-1:
            answer+='s'
        elif a-b==10:
            answer+='d'
        elif a-b==-10:
            answer+='a'
        b=a
    return answer