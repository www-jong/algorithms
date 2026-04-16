def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        v=10**9
        for i in range(s,e+1):
            if arr[i]>k and arr[i]<v:
                v=arr[i]
        answer.append(v if v!=10**9 else -1)
    return answer