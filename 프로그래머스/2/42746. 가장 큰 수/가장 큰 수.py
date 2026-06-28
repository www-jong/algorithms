def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*3,reverse=True)
    res=''
    res+=''.join(numbers)
    if res.replace('0','')=='':
        return '0'
    
    return res