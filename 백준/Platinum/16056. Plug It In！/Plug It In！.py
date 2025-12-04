import sys
input = sys.stdin.readline

def dfs(x, li, match, vis):
    if vis[x]:
        return 0
    vis[x] = 1
    for y in li[x]:
        if match[y] == -1 or dfs(match[y], li, match, vis):
            match[y] = x
            return 1
    return 0

M, N, K = map(int, input().split())
li0 = [[] for _ in range(M + 1)]
for _ in range(K):
    x, y = map(int, input().split())
    li0[x].append(y)

# 1) 기본 최대매칭
match = [-1] * (N + 1)
for x in range(1, M + 1):
    vis = [0] * (M + 1)
    dfs(x, li0, match, vis)

base = sum(1 for y in range(1, N + 1) if match[y] != -1)

# 2) 멀티탭: 각 소켓 s를 "추가 2구"로 보고 최대 증가량 계산
best_add = 0
for s in range(1, M + 1):
    # 왼쪽 노드를 M+2까지 확장: s_copy1=M+1, s_copy2=M+2 로 사용
    li = [lst[:] for lst in li0] + [li0[s], li0[s]]  # 인접리스트 복제
    tmp_match = match[:]  # 기본 매칭에서 시작(재배치 허용)

    added = 0
    # copy1
    vis = [0] * (M + 3)
    added += dfs(M + 1, li, tmp_match, vis)
    # copy2
    vis = [0] * (M + 3)
    added += dfs(M + 2, li, tmp_match, vis)

    if added > best_add:
        best_add = added
        if best_add == 2:
            break

print(base + best_add)
