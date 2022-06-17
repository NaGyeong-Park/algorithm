import sys
from collections import deque

def BFS(start):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque([start])
    check[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == N-1 and ny == M-1:
                return MAP[x][y]+1
            elif 0<=nx<N and 0<=ny<M and not check[nx][ny] and MAP[nx][ny]:
                q.append([nx,ny])
                check[nx][ny] = True
                MAP[nx][ny] += MAP[x][y]

N, M= map(int,sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
check = [[False]*M for _ in range(N)]

print(BFS([0,0]))