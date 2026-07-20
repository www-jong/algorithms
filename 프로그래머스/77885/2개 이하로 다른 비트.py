def solution(numbers):
    def func(x):
        if x%2==0:
            return x^1
        else:
            tmp='0'+bin(x)[2:]
            for i in range(len(tmp)-1,-1,-1):
                if tmp[i:i+2]=='01':
                    return int(tmp[:i]+'10'+tmp[i+2:],2)
    answer = [func(i) for i in numbers]
    return answer
