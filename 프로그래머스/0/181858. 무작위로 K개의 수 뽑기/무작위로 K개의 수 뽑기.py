def solution(arr, k):
    answer = []
    d=set()
    for i in arr:
        if i not in d:
            d.add(i)
            answer.append(i)
        if len(answer)==k:
            break
    answer+=[-1]*(k-len(answer))
    return answer