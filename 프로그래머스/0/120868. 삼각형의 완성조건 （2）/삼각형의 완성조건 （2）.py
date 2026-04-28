def solution(sides):
    sides.sort()
    answer = (sum(sides)-max(sides)-1)+(sides[1]-(sides[1]-sides[0]))
    return answer