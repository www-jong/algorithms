def solution(arr1, arr2):
    if len(arr1[0])!=len(arr2):
        arr1,arr2=arr2,arr1
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for x in range(len(answer)):
        for y in range(len(answer[0])):
            for z in range(len(arr1[0])):
                answer[x][y]+=arr1[x][z]*arr2[z][y]
    return answer
