def solution(arr):
    idxs=[]
    for i in range(len(arr)):
        if arr[i]==2:
            idxs.append(i)
    if len(idxs)<1:
        return [-1]
    elif len(idxs)==1:
        return [arr[idxs[0]]]
    else:
        return[arr[i] for i in range(idxs[0],idxs[-1]+1)]