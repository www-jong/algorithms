def solution(wallpaper):
    answer = []
    ax,ay,bx,by=50,50,0,0
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y]=='#':
                ax=min(ax,x)
                ay=min(ay,y)
                bx=max(bx,x+1)
                by=max(by,y+1)
    return [ax,ay,bx,by]