from math import gcd
def solution(arrayA, arrayB):
    answer = 0
    
    gcd_a,gcd_b=arrayA[0],arrayB[0]
    for i in arrayA[1:]:
        gcd_a=gcd(gcd_a,i)
    for i in arrayB[1:]:
        gcd_b=gcd(gcd_b,i)
    
    check_a,check_b=0,0
    for i in arrayA:
        if i%gcd_b==0:
            check_a=1
            break
    if not check_a:
        answer=max(answer,gcd_b)
    
    for i in arrayB:
        if i%gcd_a==0:
            check_b=1
            break
    if not check_b:
        answer=max(answer,gcd_a)
    
    return answer