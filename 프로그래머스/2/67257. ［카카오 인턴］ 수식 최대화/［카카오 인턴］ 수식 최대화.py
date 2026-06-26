from itertools import permutations
from collections import deque
def solution(expression):
    expression+='_'
    answer = 0
    li=[]
    idx,flag=0,0
    tmp=''
    for i in expression:
        if i.isnumeric():
            if flag:
                li.append(tmp)
                tmp=i
                flag=0
            else:
                tmp+=i
        else:
            li.append(int(tmp))
            tmp=i
            flag=1
            idx+=1
    for i in permutations([0,1,2],3): # *+-
        r=0
        tmp=li[::]

        for j in i:
            idx=0
            while idx<len(tmp):
                if j==0 and tmp[idx]=='*':
                    v=tmp[idx-1]*tmp[idx+1]
                    tmp[idx]=v
                    tmp.pop(idx-1)
                    tmp.pop(idx)
                    idx-=1
                elif j==1 and tmp[idx]=='+':
                    v=tmp[idx-1]+tmp[idx+1]
                    tmp[idx]=v
                    tmp.pop(idx-1)
                    tmp.pop(idx)
                elif j==2 and tmp[idx]=='-':
                    v=tmp[idx-1]-tmp[idx+1]
                    tmp[idx]=v
                    tmp.pop(idx-1)
                    tmp.pop(idx)
                else:
                    idx+=1
        answer=max(answer,abs(tmp[0]))
    return answer

