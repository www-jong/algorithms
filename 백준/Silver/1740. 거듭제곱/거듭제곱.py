def solution(n,q):
    rev=''
    while n>0:
        n,mod=divmod(n,q)
        rev+=str(mod)
    return rev[::-1]
N=int(input())
print(solution(int(str(bin(N))[2:],3),10))