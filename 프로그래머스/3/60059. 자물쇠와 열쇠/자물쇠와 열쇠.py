def solution(key, lock):
    answer = False
    d=[0,0,1,-1]
    def rotate(x,y,f):
        t=[(x,y),(y,N-1-x),(N-1-x,N-1-y),(N-1-y,x)]
        return t[f]
    M,N=len(key),len(lock)
    tmp=set()
    dkey_original=set()
    dkey=[]
    xmin,ymin=30,30
    for i in range(M):
        for j in range(M):
            if key[i][j]==1:
                xmin=min(xmin,i)
                ymin=min(ymin,j)
                tmp.add((i,j))
    for x,y in tmp:
        dkey_original.add((x-xmin,y-ymin))
    
    x_bnd,y_bnd=N,N
    for i in range(0,x_bnd):
        for j in range(0,y_bnd):
            tmp=set()
            for x,y in dkey_original:
                tmp.add((x+i,y+j))
            dkey.append(tmp)
    dlock_original=set()
    dlock=[]
    for i in range(N):
        for j in range(N):
            if lock[i][j]==0:
                dlock_original.add((i,j))
    for i in range(4):
        tmp=[]
        for x,y in dlock_original:
            nx,ny=rotate(x,y,i)
            tmp.append((nx,ny))
        dlock.append(tmp)

    for f in range(4):
        l = {
            rotate(x, y, f)
            for x, y in dlock_original
        }

        for dx in range(-M, N+1):
            for dy in range(-M, N+1):
                k = {
                    (x+dx, y+dy)
                    for x, y in dkey_original
                    if 0 <= x+dx < N
                    and 0 <= y+dy < N
                }

                if k == l:
                    return True
    return False