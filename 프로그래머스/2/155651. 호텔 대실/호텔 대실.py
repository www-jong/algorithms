def solution(book_time):
    li=[]
    for a,b in book_time:
        st,end=0,0
        h,m=a.split(":")
        st+=int(h)*60+int(m)
        h,m=b.split(":")
        end+=int(h)*60+int(m)+10
        li.append((st,end))
    li.sort(key=lambda x:(x[0],x[1]))
    room=1
    tmp=[0]*(1001)
    for st,end in li:
        check=0
        for j in range(room):
            if tmp[j]<=st or not tmp[j]:
                tmp[j]=end
                check=1
                break
        if not check:
            room+=1
            tmp[room-1]=end
    return room