def solution(lines):
    answer = 0
    lines.sort(key=lambda x:(x[0],-x[1]))
    print(lines)
    st,end=-100,-100
    for x,y in lines:
        print(x,y,st,end,answer)
        if x<end:
            answer+=min(end,y)-max(st,x)
            st,end=min(end,y),max(end,y)
        else:
            st,end=x,y
    return answer