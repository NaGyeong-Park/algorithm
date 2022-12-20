def DFS(now):
    data[now[0]][now[1]] = 1
    for num in range(4):
        now_x = now[0] + dx[num]
        now_y = now[1] + dy[num]
        if 0<= now_x < N and 0<= now_y < M and data[now_x][now_y] == 0:
            DFS((now_x, now_y))
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
            stack = [(i,j)]
            result += DFS((i, j))
            
print(result)