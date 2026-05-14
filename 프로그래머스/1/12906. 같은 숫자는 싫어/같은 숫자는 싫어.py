def solution(arr):
    answer = []
    now=-1
    for i in arr:
        if now!=i:
            now=i
            answer.append(i)
    return answer