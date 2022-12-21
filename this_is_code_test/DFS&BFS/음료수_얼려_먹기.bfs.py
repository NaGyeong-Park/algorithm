from collections import deque

def BFS(start_location):
    queue = deque([start_location])
    while len(queue) > 0:
        now_x, now_y = queue.popleft()
        data[now_x][now_y] = 1
        for direc in range(4):
            x = now_x + dx[direc]
            y = now_y + dy[direc]
            if 0<=x<N and 0<=y<M and data[x][y] == 0:
                queue.append((x,y))
    return 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]
N, M = map(int, input().split())
data=[]
result = 0
for _ in range(N):
    data.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            result += BFS((i, j))

print(result)