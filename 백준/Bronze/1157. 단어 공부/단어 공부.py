a=list(input().lower())
arr=[0 for i in range(26)]
check=0
for i in a:
    arr[ord(i)-97]+=1
for j,i in enumerate(arr):
    if i>=max(arr):
        if j!=arr.index(max(arr)):
            check=1
            break
if check==0:
    print(chr(65+arr.index(max(arr))))
else:
    print("?")