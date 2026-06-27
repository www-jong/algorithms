def solution(brown, yellow):
    x,y=0,0
    for i in range(1,yellow+1):
        if yellow%i==0:
            x=int(yellow/i)
            y=i
            if x*2+y*2+4==brown:
                return sorted([x+2,y+2],reverse=True)