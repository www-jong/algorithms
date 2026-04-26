def solution(arr, delete_list):
    d=set(delete_list)
    answer = []
    for i in arr:
        if i not in d:
            answer.append(i)
    return answer