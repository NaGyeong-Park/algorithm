import sys

sys.stdin = open('input.txt')

T = 4

def DFS(graph, v, visited):         # DFS
    visited[v] = True               # 방문 위치 True
    print(v,end=' ')                # 방문 위치 출력
    for i in graph[v]:              # 방문 위치 연결된 리스트
        if not visited[i]:          # 리스트 요소중 방문 하지 않은 곳이 있다면
            DFS(graph, i, visited)  # DFS 돌기

def BFS(graph, v, visited):         # BFS
    queue = [v]                     # queue 리스트 만들기
    visited[v] = True               # 방문 위치 True
    while queue:                    # queue에 리스트가 있을 때까지
        v = queue[0]                # 방문 위치
        queue = queue[1:]           # queue 맨 앞 요소 pop
        print(v, end=' ')           # 방문 위치 출력
        for i in graph[v]:          # 방문 위치 연결 리스트
            if not visited[i]:      # 리스트 요소중 방문 하지 않은 곳이 있다면
                queue.append(i)     # queue에 요소를 넣고
                visited[i] = True   # 방문 mark


for tc in range(1, T + 1):
    # N+1 사용 이유 : 리스트 인덱스를 정점 번호랑 맞추기 위해서 0 인덱스를 사용하지 않음
    N, M, V = map(int, input().split())   # 정점수 N, 간선 수 M, 탐색시작번호 V
    lst = [0]*(N+1)                       # graph 만들 기초
    visited1 = [False]*(N+1)              # 방문 흔적 남길 리스트
    visited2 = [False]*(N+1)              # 방문 흔적 남길 리스트
    for i in range(1,N+1):                # list형태로 바꿔줌
        lst[i] = []
    for _ in range(M):                    # a, b 정점 방문한 곳을 그래프형태로 바꿔줌
        a, b = map(int, input().split())
        if not b in lst[a]:               # 중복 허용 안함
            lst[a].append(b)
        if not a in lst[b]:
            lst[b].append(a)

    for i in range(N+1):                  # 그래프 요소들 정렬
        if type(lst[i]) == list:
            lst[i].sort()
    print(lst)
    print(f'#{tc}')
    DFS(lst, V, visited1)
    print()
    BFS(lst, V, visited2)
    print()

