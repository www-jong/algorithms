from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = Counter(arr)
res = 0

for i in range(n):
    d[arr[i]] -= 1

    for j in range(i):
        target = k - arr[i] - arr[j]
        res += d[target]

print(res)