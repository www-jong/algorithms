def solution(array, n):
    answer = -200
    for i in array:
        if abs(n-i)<abs(n-answer):
            answer=i
        elif abs(n-i)==abs(n-answer):
            answer=min(i,answer)
    return answer