def solution(l, r):
    answer = []
    s,e='1'*len(str(l)),'1'*len(str(r))
    for i in range(1,int(e,2)+1):
        now=int(bin(i)[2:].replace('1','5'))
        if l<=now<=r:
            answer.append(now)
    answer.sort()
    return answer if answer else [-1]