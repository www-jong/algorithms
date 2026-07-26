def solution(n):
    res=[]
    def func(n,a,b,c,res):
        if n==1:
            res.append([a,b])
            return
        else:
            func(n-1,a,c,b,res)
            res.append([a,b])
            func(n-1,c,b,a,res)
    func(n,1,3,2,res)
    return res