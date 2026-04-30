def solution(num, total):
    answer = []
    if num%2==0:
        r=total//(num//2)
        print(r,(r-num+1)//2)
        return [i for i in range((r-num+1)//2,(r-num+1)//2+num)]
    else:
        mid=int(total//(num/2)//2)
        st=mid-(num//2)
        print(mid,st)
        return [i for i in range(st,st+num)]
    return answer