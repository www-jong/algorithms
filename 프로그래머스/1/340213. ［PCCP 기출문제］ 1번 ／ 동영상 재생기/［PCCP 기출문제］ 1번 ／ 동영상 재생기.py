def rev(time):
    a,b=time.split(":")
    tmp=int(a)*60+int(b)
    return tmp
    
def solution(video_len, pos, op_start, op_end, commands):
    video_len,pos,op_start,op_end=rev(video_len),rev(pos),rev(op_start),rev(op_end)
    def move(now):
        if op_start<=now<=op_end:
            now=max(now,op_end)
        if now<10:
            now=max(now,0)
        if video_len-10<now:
            now=video_len
        return now
    pos=move(pos)
    for command in commands:
        print(pos)
        if command=="next":
            pos+=10
        else:
            pos-=10
        print(pos)
        pos=move(pos)
        print(command,pos)
    return str(pos//60).zfill(2)+":"+(str(pos%60)).zfill(2)

