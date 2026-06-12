def solution(elements):
    answer = set()
    N=len(elements)
    elements+=elements
    for i in range(N):
        c=0
        for j in range(N):
            c+=elements[i+j]
            answer.add(c)
    return len(answer)