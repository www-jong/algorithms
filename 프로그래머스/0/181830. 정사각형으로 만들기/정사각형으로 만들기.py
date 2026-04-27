def solution(arr):
    answer = [[]]
    f=0
    m=[0,len(arr)]
    for i in arr:
        m[0]=max(m[0],len(i))
    print(m)
    if m[0]>m[1]:
        arr+=[[0]*max(m) for _ in range(m[0]-m[1])]
    else:
        pass
    for i in range(len(arr)):
        arr[i]+=[0]*(max(m)-len(arr[i]))        
    return arr