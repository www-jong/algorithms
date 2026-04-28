def solution(keyinput, board):
    d={'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y=0,0
    for i in keyinput:
        dx,dy=d[i]
        nx,ny=x+dx,y+dy
        if abs(nx)<=(board[0]-1)//2 and abs(ny)<=(board[1]-1)//2:
            x,y=nx,ny
    print(x,y)
            
    return [x,y]