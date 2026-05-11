def solution(answers):
    answer=[0,0,0]
    a1,a2,a3=[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]
    for i,j in enumerate(answers):
        if a1[i%5]==j:
            answer[0]+=1
        if a2[i%8]==j:
            answer[1]+=1
        if a3[i%10]==j:
            answer[2]+=1
    r=0
    res=[]
    for i,j in enumerate(answer):
        if j>r:
            r=j
            res=[i+1]
        elif j==r:
            res.append(i+1)
    return  res