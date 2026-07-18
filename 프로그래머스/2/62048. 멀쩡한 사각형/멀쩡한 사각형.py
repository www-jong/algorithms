import math
def solution(w,h):
    w,h=min(w,h),max(w,h)
    answer = w*h
    gcd_v=math.gcd(w,h)
    x=(w+h)//gcd_v-1
    print(h/w,gcd_v,w/gcd_v,h/gcd_v,x,x*gcd_v)
    return answer-x*gcd_v