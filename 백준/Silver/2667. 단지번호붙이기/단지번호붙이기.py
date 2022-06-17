import sys

def DFS(start):
    dx = [1, -1, 0, 0]
    dy = [0,0,1,-1]

    x, y = start
    check[x][y] = True
    global cnt
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<N and not check[nx][ny] and MAP[nx][ny]:
            DFS([nx,ny])


N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
check = [[False]*N for _ in range(N)]
result = []

cnt = 0
for i in range(N):
    for j in range(N):
        if MAP[i][j] and not check[i][j]:
            DFS([i,j])
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
print("\n".join(map(str,result)))