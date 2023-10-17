arr=list(input())
count=0
i=0
l1=['c=','c-','d-','lj','nj','s=','z=']
while True:
    if ''.join(arr[i:i+2]) in l1:
        count+=1
        i+=2
    elif ''.join(arr[i:i+3])=='dz=':
        count+=1
        i+=3
    else:
        count+=1
        i+=1
    if i==len(arr):
        print(count)
        break