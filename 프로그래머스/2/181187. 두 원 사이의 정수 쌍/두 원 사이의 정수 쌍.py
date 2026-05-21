from math import floor,ceil
def solution(r1, r2):
    answer = 0
    R1,R2=r1**2,r2**2
    for x in range(1,r2+1):
        max_y=(R2-x**2)**0.5
        min_y=(R1-x**2)**0.5 if x<r1 else 0
        answer+=floor(max_y)-ceil(min_y)+1
    return answer*4