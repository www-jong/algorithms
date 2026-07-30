from itertools import permutations

def solution(numbers):
    res=[]
    N=len(numbers)
    nums=[i for i in numbers]
    li=[]
    for i in range(1,N+1):
        li+=list(permutations(nums,i))
    nums2=[int(''.join(i)) for i in li]

    for i in nums2:
        if i<2:
            continue
        check=1
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                check=0
                break
        if check:
            res.append(i)
    return len(set(res))
