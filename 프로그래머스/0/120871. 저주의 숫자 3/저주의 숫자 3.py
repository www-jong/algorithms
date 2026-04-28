def solution(n):
    l=[0]+[i for i in range(200) if str(3) not in str(i) and i%3]
    print(l)
    print(l[10])
    answer = 0
    return l[n]