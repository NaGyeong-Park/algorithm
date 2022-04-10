from collections import deque

N, K = map(int, input().split())
arr = [0]*N
q = []
for i in range(N):
    arr[i] = list(map(int, input().split()))
    for j in range(N):
        if arr[i][j]:
            q.append((arr[i][j],i,j))
q.sort()
q = deque(q)
S, X, Y = map(int, input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0

if not q:
    print(0)
else:
    while q:
        if cnt == S:
            print(arr[X - 1][Y - 1])
            break
        num, nx, ny = q.popleft()
        for d in range(4):
            x = nx + dx[d]
            y = ny + dy[d]
            if 0 <= x < N and 0 <= y < N and arr[x][y] == 0:
                q.append((arr[x][y], x, y))
                arr[x][y] = arr[nx][ny]
        if arr[nx][ny] == K:
            if not q:
                break
            elif arr[q[0][0]][q[0][1]] != arr[nx][ny]:
                cnt += 1