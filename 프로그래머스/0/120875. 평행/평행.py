def solution(dots):
    answer = 0
    for a in range(4):
        for b in range(a+1,4):
            c,d=[i for i in range(4) if i not in [a,b]]
            print(a,b,c,d)
            print(abs(dots[b][1]-dots[a][1])/abs(dots[b][0]-dots[a][0]))
            if abs(dots[b][1]-dots[a][1])/abs(dots[b][0]-dots[a][0])==abs(dots[d][1]-dots[c][1])/abs(dots[d][0]-dots[c][0]):
                return 1
    return answer