def solution(begin, end):
    answer = []
    
    def func(x):
        if x==1:
            return 0
        tmp=1
        for i in range(2,int(x**(0.5)+1)):
            if x%i==0:
                now=x//i
                if now<=10**7:
                    return now
                tmp=max(tmp,i)
        
                
        return tmp
                       
                       
    for i in range(begin,end+1):
        answer.append(func(i))
    return answer