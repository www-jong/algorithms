def solution(ineq, eq, n, m):
    answer = [0,1][eval(str(n)+ineq+('' if eq=='!' else eq)+str(m))]
    return answer
