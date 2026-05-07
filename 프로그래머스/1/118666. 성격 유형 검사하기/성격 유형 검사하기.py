def solution(survey, choices):
    li=[0]*8
    d1,d2=[0,3,2,1,0,1,2,3],'RTCFJMAN'
    answer = ''
    def func(idx):
        a,b=survey[idx][0],survey[idx][1]
        if choices[idx]<4:
            li[d2.index(a)]+=d1[choices[idx]]
        else:
            li[d2.index(b)]+=d1[choices[idx]]    
    for i in range(len(choices)):
        func(i)
    for i in range(0,8,2):
        if li[i]==li[i+1]:
            answer+=min(d2[i],d2[i+1])
        else:
            answer+=d2[i+1] if li[i]<li[i+1] else d2[i]
    print(li)
    return answer