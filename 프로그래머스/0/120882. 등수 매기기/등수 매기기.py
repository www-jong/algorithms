def solution(score):
    answer = [0]*len(score)
    li=[]
    for i in range(len(score)):
        li.append((sum(score[i]),i))
    li.sort(key=lambda x:-x[0])
    b=0
    idx=0
    d=0
    for i in range(len(score)):
        if b!=li[i][0]:
            idx+=1+d
            answer[li[i][1]]=idx
            d=0
        else:
            answer[li[i][1]]=idx
            d+=1
        b=li[i][0]
    print(li)
    return answer