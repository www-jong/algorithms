def solution(arr):
    before=arr[:]
    after=arr[:]
    idx=0
    while True:
        
        for i in range(len(after)):
            if after[i]>=50 and after[i]%2==0:
                after[i]//=2
            elif after[i]<50 and after[i]%2:
                after[i]=after[i]*2+1
        
        if before==after:
            return idx
        before=after[:]
        idx+=1