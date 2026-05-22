def solution(board):
    def check(f):
        c='O' if f else 'X'
        for i in range(3):
            t1,t2=0,0
            for j in range(3):
                if board[i][j]==c:
                    t1+=1
            for j in range(3):
                if board[j][i]==c:
                    t2+=1
            
            if t1==3 or t2==3:
                return 1
        t1,t2=0,0
        for i in range(3):
            if board[i][i]==c:
                t1+=1
            if board[2-i][i]==c:
                t2+=1
        if t1==3 or t2==3:
            return 1
        return 0
    a,b=check(1),check(0)
    ca,cb=sum(sum(1 for j in i if j=='O')for i in board),sum(sum(1 for j in i if j=='X')for i in board)
    print(a,b,ca,cb)
    if (ca<cb or ca>cb+1) or (a and ca==cb) or (b and ca>cb):
        return 0
    return 1