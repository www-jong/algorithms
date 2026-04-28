from itertools import combinations
def solution(numbers):
    answer = -10**9
    for x,y in combinations(numbers,2):
        answer=max(answer,x*y)
    return answer