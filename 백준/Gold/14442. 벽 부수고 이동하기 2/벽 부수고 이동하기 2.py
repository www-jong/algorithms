def main():
    import io
    import os
    import sys
    
    # 빠른 입력 처리
    input = io.BufferedReader(io.FileIO(0), 1 << 18).readline
    
    # 입력 받기
    N, M, K = map(int, input().split())
    
    # 맵 구성 (패딩 추가)
    R = M + 2
    mp = bytearray([49]) * ((N + 2) * R)  # ASCII '1'은 49
    for i in range(1, N + 1):
        mp[i * R + 1 : (i + 1) * R - 1] = input().rstrip()
        mp[i * R + R - 1] = 49  # 우측 패딩 추가
    
    # 방문 배열 초기화 (255를 무한대로 사용)
    v = bytearray([255]) * len(mp)
    v[:R] = bytearray(R)  # 상단 패딩
    v[-R:] = bytearray(R)  # 하단 패딩
    
    zero = bytearray(N)  # 0으로 초기화된 배열
    v[R : (N + 1) * R : R] = zero  # 좌측 패딩
    v[R + R - 1 : (N + 1) * R : R] = zero  # 우측 패딩
    
    # BFS 시작
    v[R + 1] = 0  # 시작점 초기화
    q = [R + 1]   # 시작점만 포함된 큐
    d = 1         # 시작점도 카운트하므로 1부터 시작
    end = N * R + M  # 도착점 위치
    
    # BFS 실행
    while q and v[end] > K:
        nxt = []
        append = nxt.append  # 로컬 함수 참조 캐싱으로 성능 향상
        
        for j in q:
            k = v[j]
            
            # 4방향 탐색 (아래, 오른쪽, 왼쪽, 위)
            # 아래
            t = j + R
            vn = k + (mp[t] & 1)  # 비트 연산으로 벽 여부 확인
            if K >= vn < v[t]:    # K 이하이고 현재 저장된 값보다 작으면
                v[t] = vn
                append(t)
            
            # 오른쪽
            t = j + 1
            vn = k + (mp[t] & 1)
            if K >= vn < v[t]:
                v[t] = vn
                append(t)
            
            # 왼쪽
            t = j - 1
            vn = k + (mp[t] & 1)
            if K >= vn < v[t]:
                v[t] = vn
                append(t)
            
            # 위
            t = j - R
            vn = k + (mp[t] & 1)
            if K >= vn < v[t]:
                v[t] = vn
                append(t)
        
        q = nxt  # 다음 레벨의 노드들로 큐 갱신
        d += 1   # 거리 증가
    
    # 결과 출력 (도착점에 저장된 값이 K보다 작으면 경로 존재)
    os.write(1, str(-1 if v[end] > K else d).encode("ascii"))
    os._exit(0)  # 빠른 종료

main()
