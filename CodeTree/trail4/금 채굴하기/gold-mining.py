
n, m = map(int, input().split())

grid = [[0]*(n+1)] + [
    [0]+list(map(int, input().split())) for _ in range(n)
]

def q(x, y, k):
    tmp = 0

    for nx in range(max(1, x-k), min(n, x+k)+1):
        for ny in range(max(1, y-k), min(n, y+k)+1):
            if abs(nx-x) + abs(ny-y) <= k:
                tmp += grid[nx][ny]

    return tmp

answer = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(2*(n-1)+1):
            gold = q(i, j, k)
            cost = k*k + (k+1)*(k+1)

            if gold*m >= cost:
                answer = max(answer, gold)

print(answer)
