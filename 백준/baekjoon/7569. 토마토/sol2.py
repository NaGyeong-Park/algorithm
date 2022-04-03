import sys
from collections import deque

queue = deque([])
M,N,H = map(int, input().split())
lst = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
cnt_all = 0
for j in range(H):
    for i in range(N):
        lst[j][i] = list(map(int, sys.stdin.readline().split()))
        for k in range(H):
            if lst[j][i][k] == 1:
                queue.append((j,i,k))

def BFS():
    dx, dy, dz = [1,0,-1,0,0,0], [0,1,0,-1,0,0], [0,0,0,0,1,-1]
    while queue:
        h, x, y = queue.popleft()
        for i in range(6):
            z_now = h + dz[i]
            x_now = x + dx[i]
            y_now = y + dy[i]
            if 0<=x_now<N and 0<=y_now<M and 0<=z_now<H and lst[z_now][x_now][y_now] == 0:
                queue.append((z_now,x_now,y_now))
                lst[z_now][x_now][y_now] = lst[h][x][y] + 1

BFS()
result = 0
for j in lst:
    for i in j:
        for k in i:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(i))
print(result-1)