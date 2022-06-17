import sys
from collections import deque

def BFS(start):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0

    q = deque([start])
    check[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        cnt +=1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and not check[nx][ny] and MAP[nx][ny]:
                q.append([nx,ny])
                check[nx][ny] = True
    result.append(cnt)

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
check = [[False]*N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] and not check[i][j]:
            BFS([i,j])
result.sort()
print(len(result))
print("\n".join(map(str,result)))