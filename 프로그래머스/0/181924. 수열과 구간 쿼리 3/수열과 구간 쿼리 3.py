def solution(arr, queries):
    for a,b in queries:
        arr[b],arr[a]=arr[a],arr[b]
    return arr