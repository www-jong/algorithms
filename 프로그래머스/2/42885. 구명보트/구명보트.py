def solution(people, limit):
    res=0
    people.sort()
    st,end=0,len(people)-1
    while st<=end:
        if people[st]+people[end]<=limit:
            st+=1
            end-=1
        else:
            end-=1
        res+=1
    return res