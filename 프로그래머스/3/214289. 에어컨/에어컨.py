from collections import defaultdict
def solution(temperature, t1, t2, a, b, onboard):
    n=len(onboard)
    d=[defaultdict(lambda:1000001) for _ in range(n)] # dp[i][j]=k , i시간에 온도가 j일때 최소전력량 k
    d[0][temperature]=0
    
    for idx in range(1,n):
        for temp,watt in d[idx-1].items():
            if onboard[idx]:
                if not (t1<=temp-1<=t2 or t1<=temp+1<=t2): #손님있는데 에어컨 틀어도 온도안맞을경우
                    continue
            if watt==1000001:
                continue

            if temp<temperature: #밖이 더 더울때
                if (onboard[idx] and t1<=temp+1<=t2) or not onboard[idx]: #에어컨x
                    d[idx][temp+1]=min(watt,d[idx][temp+1])
                if (onboard[idx] and t1<=temp<=t2) or not onboard[idx]:   #에어컨, 온도 유지
                    d[idx][temp]=min(watt+b,d[idx][temp])
                if (onboard[idx] and t1<=temp-1<=t2) or not onboard[idx]: #에어컨, 온도 내리기
                    d[idx][temp-1]=min(watt+a,d[idx][temp-1])
            elif temp>temperature: # 밖이 더 시원할떄
                if (onboard[idx] and t1<=temp-1<=t2) or not onboard[idx]: #에어컨x
                    d[idx][temp-1]=min(watt,d[idx][temp-1])    
                if (onboard[idx] and t1<=temp<=t2) or not onboard[idx]:   #에어컨, 온도 유지
                    d[idx][temp]=min(watt+b,d[idx][temp])
                if (onboard[idx] and t1<=temp+1<=t2) or not onboard[idx]: #에어컨, 온도 올리기
                    d[idx][temp+1]=min(watt+a,d[idx][temp+1])
            else: #밖이랑 현재온도 같을때
                if (onboard[idx] and t1<=temp<=t2) or not onboard[idx]:   #에어컨x
                    d[idx][temp]=min(watt,d[idx][temp])
                if (onboard[idx] and t1<=temp<=t2) or not onboard[idx]:   #에어컨, 온도 유지
                    d[idx][temp]=min(watt+b,d[idx][temp])
                if (onboard[idx] and t1<=temp+1<=t2) or not onboard[idx]: #에어컨, 온도 내리기
                    d[idx][temp+1]=min(watt+a,d[idx][temp+1])
                if (onboard[idx] and t1<=temp-1<=t2) or not onboard[idx]: #에어컨, 온도 내리기
                    d[idx][temp-1]=min(watt+a,d[idx][temp-1])
    
    res=1000001
    for k,v in d[n-1].items():
        res=min(res,v)
    return res