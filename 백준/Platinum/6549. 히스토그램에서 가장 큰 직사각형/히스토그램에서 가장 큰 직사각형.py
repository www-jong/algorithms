import sys
input=sys.stdin.readline

while True:
    li=list(map(int,input().split()))
    res=0
    if li[0]==0:break
    else:li.pop(0) 
    stk=[]
    ch_idx=0
    for i in li:
        if not stk:
            stk.append((i,ch_idx))
            ch_idx+=1
        else:
            if stk[-1][0]<i:
                stk.append((i,ch_idx))
                ch_idx+=1
            else:
                tmp_li=[]
                while stk[-1][0]>=i:
                    now_val,now_idx=stk.pop()
                    if not stk:
                        res=max(res,now_val*(ch_idx))
                        break
                    else:
                        res=max(res,now_val*(ch_idx-stk[-1][1]-1))
                stk.append((i,ch_idx))
                ch_idx+=1
    while stk:
        now_val,now_idx=stk.pop()
        if not stk:
            res=max(res,now_val*(ch_idx))
        else:
            res=max(res,now_val*(ch_idx-stk[-1][1]-1))
    print(res)
