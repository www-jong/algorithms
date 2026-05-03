def solution(n, m, section):
    answer = 0
    st=-1
    while section:
        if st==-1:
            st=section.pop()
        else:
            next=section.pop()
            if st-next+1<=m:
                continue
            else:
                answer+=1
                st=next
    if st:
        answer+=1
    return answer