def solution(sides):
    answer = 0
    return [2,1][sum(sorted(sides)[:2])>sorted(sides)[-1]]