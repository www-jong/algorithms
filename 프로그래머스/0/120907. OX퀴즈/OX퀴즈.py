def solution(quiz):
    answer = []
    for i in quiz:
        a,b,c,d,e=i.split()
        if eval(a+b+c)==int(e):
            answer.append('O')
        else:
            answer.append('X')
    return answer