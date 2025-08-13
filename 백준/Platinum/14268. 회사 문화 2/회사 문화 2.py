import sys

# 재귀 깊이 제한을 늘려줍니다.
sys.setrecursionlimit(10**6)
# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    백준 14268번 문제를 해결하는 메인 함수
    """
    # 1. 입력 처리 및 트리 구성
    n, m = map(int, input().split())
    # 직속 상사 정보. 0번 인덱스는 사용하지 않으므로 앞에 [0] 추가
    parents = [0] + list(map(int, input().split()))

    # 인접 리스트로 트리 구성 (상사 -> 부하 직원)
    adj = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        adj[parents[i]].append(i)

    # 2. DFS를 이용한 트리 평탄화 (오일러 투어)
    start = [0] * (n + 1)
    end = [0] * (n + 1)
    counter = 0

    def dfs(u):
        nonlocal counter
        counter += 1
        start[u] = counter
        for v in adj[u]:
            dfs(v)
        end[u] = counter

    # 루트 노드(1번)부터 DFS 시작
    dfs(1)

    # 3. 펜윅 트리(BIT) 설정
    # 크기는 n+2로 넉넉하게 설정 (end[i]+1 인덱스 접근 때문)
    tree = [0] * (n + 2)

    def update(idx, val):
        """펜윅 트리의 idx 위치에 val을 더합니다."""
        while idx <= n + 1:
            tree[idx] += val
            idx += idx & -idx

    def query(idx):
        """펜윅 트리의 1부터 idx까지의 누적합을 구합니다."""
        s = 0
        while idx > 0:
            s += tree[idx]
            idx -= idx & -idx
        return s

    # 4. M개의 쿼리 처리
    for _ in range(m):
        line = list(map(int, input().split()))
        query_type = line[0]

        if query_type == 1:
            # 칭찬 쿼리 (1 i w)
            i, w = line[1], line[2]
            # 차분 배열 원리 적용: start[i]에 w 더하고, end[i]+1에 w 빼기
            update(start[i], w)
            update(end[i] + 1, -w)

        elif query_type == 2:
            # 칭찬 조회 쿼리 (2 i)
            i = line[1]
            # i번 직원의 총 칭찬 = 평탄화 배열 start[i]의 누적합
            total_praise = query(start[i])
            print(total_praise)

solve()