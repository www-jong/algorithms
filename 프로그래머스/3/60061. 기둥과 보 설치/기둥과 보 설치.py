def solution(n, build_frame):
    answer = [[]]
    s=set()
    def check():
        for x,y,a in s:
            if a==0:
                if y==0 or (x,y-1,0) in s or (x-1,y,1) in s or (x,y,1) in s:
                    continue
                return 0
            else:
                if (x,y-1,0) in s or (x+1,y-1,0) in s or ((x-1,y,1) in s and (x+1,y,1) in s):
                    continue
                return 0
        return 1
    
    for x,y,a,b in build_frame:
        now=(x,y,a)
        if b==1:
            s.add(now)
            if not check():
                s.remove(now)
        else:
            s.remove(now)
            if not check():
                s.add(now)
    
    
    return [list(i) for i in sorted(s)]