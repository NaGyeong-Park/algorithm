def BFS(graph, v, visited):         # BFS
    cnt = -1
    queue = [v]                     # queue 리스트 만들기
    visited[v] = True               # 방문 위치 True
    while queue:                    # queue에 리스트가 있을 때까지
        v = queue[0]                # 방문 위치
        queue = queue[1:]           # queue 맨 앞 요소 pop
        cnt += 1           # 방문 위치 출력
        for i in graph[v]:          # 방문 위치 연결 리스트
            if not visited[i]:      # 리스트 요소중 방문 하지 않은 곳이 있다면
                queue.append(i)     # queue에 요소를 넣고
                visited[i] = True   # 방문 mark
    return print(cnt)


N = int(input())
M = int(input())
lst = [0]*(N+1)
for i in range(1, N + 1):  # list형태로 바꿔줌
    lst[i] = []
for _ in range(M):  # a, b 정점 방문한 곳을 그래프형태로 바꿔줌
    a, b = map(int, input().split())
    if not b in lst[a]:  # 중복 허용 안함
        lst[a].append(b)
    if not a in lst[b]:
        lst[b].append(a)
visited = [0]*(N+1)
BFS(lst,1,visited)