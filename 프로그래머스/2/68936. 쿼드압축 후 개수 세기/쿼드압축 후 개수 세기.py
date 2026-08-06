def solution(arr):
    answer = [0, 0]
    def func(x,y,n):
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j]!=arr[x][y]:
                    n//=2
                    func(x,y,n)
                    func(x+n,y,n)
                    func(x,y+n,n)
                    func(x+n,y+n,n)
                    return
        answer[arr[x][y]]+=1
    func(0,0,len(arr))
    return answer
