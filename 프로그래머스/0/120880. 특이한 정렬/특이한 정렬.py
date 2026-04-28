def solution(numlist, n):
    li=[]
    for i in numlist:
        li.append((i,abs(i-n)))
    li.sort(key=lambda x:(x[1],-x[0]))
    answer=[i for i,_ in li]
    return answer