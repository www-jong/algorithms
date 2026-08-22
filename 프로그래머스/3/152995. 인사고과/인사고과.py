def solution(scores):
    answer = 0
    li=[(a,b,a+b) for a,b in scores]
    x,y=scores[0]
    li.sort(key=lambda x:(-x[0],x[1]))
    tmp=0
    for a,b,c in li:
        if x<a and y<b:
            return -1
        if b>=tmp:
            tmp=b
            if c>x+y:
                answer+=1
    return answer+1