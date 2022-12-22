from collections import deque

def BFS(start_location):
    queue = deque([start_location])
    while len(queue) > 0:
        now_x, now_y = queue.popleft()
        for direc in range(4):
            x = now_x + dx[direc]
            y = now_y + dy[direc]
            if 0<=x<N and 0<=y<M and data[x][y] == 1:
                data[x][y] = data[now_x][now_y] + 1
                queue.append((x,y))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
N, M = map(int, input().split())
data=[]
result = 0
for _ in range(N):
    data.append(list(map(int, input())))

BFS((0, 0))
print(data)
print(data[N-1][M-1])