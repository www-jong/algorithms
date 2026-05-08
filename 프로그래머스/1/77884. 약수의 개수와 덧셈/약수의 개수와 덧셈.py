def solution(left, right):
    return sum(i*(i**.5%1>0 or -1) for i in range(left,right+1))