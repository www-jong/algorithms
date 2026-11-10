n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]
cnt=1
d={}
for i in words[1:]:
    d[i]=cnt
    cnt+=1
d2={v:k for k,v in d.items()}
for i in queries:
    if i.isnumeric():
        print(d2[int(i)])
    else:
        print(d[i])
