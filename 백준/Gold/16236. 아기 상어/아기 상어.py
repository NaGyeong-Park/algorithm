from collections import deque

def BFS():
    global baby_size, time, baby, temp
    my_fish = []
    move_cnt = 1000
    queue = deque([baby])
    visited[baby[0]][baby[1]] = True
    while queue:
        now_x, now_y = queue.popleft()
        if bfs_lst[now_x][now_y] > move_cnt:
            break
        for i in range(4):
            x = now_x + direc_x[i]
            y = now_y + direc_y[i]
            if 0<=x<N and 0<=y<N and visited[x][y] == False:
                queue.append([x,y])
                visited[x][y] = True
                bfs_lst[x][y] = bfs_lst[now_x][now_y] + 1
                if [x,y] in cheak_fish and move_cnt >= bfs_lst[x][y]:
                    my_fish.append([x,y])
                    move_cnt = bfs_lst[x][y]
    if my_fish:
        if len(my_fish) > 1:
            my_fish.sort(key=lambda x : x[1])
            my_fish.sort(key=lambda x : x[0])
            my_fish = [my_fish[0]]
        x = my_fish[0][0]
        y = my_fish[0][1]
        time += bfs_lst[x][y]
        temp += 1
        if temp == baby_size:
            baby_size += 1
            temp = 0
        map_lst[x][y] = 0
        baby = [x,y]
        fish.remove([x,y])
        return 1
    return 0


N = int(input())
map_lst = [[0] for _ in range(N)]
fish = []
for i in range(N):
    map_lst[i] = list(map(int, input().split()))
    for j in range(N):
        if map_lst[i][j] == 9:
            baby = [i,map_lst[i].index(9)]
            map_lst[baby[0]][baby[1]] = 0
        elif map_lst[i][j] > 0:
            fish.append([i,j])
direc_x = [-1, 1, 0, 0]
direc_y = [0, 0, -1, 1]
baby_size = 2
end_cnt = 0
time = 0
temp = 0

while fish:
    cheak_fish = []
    end_cnt = 0
    visited = [[False] * N for _ in range(N)]
    for f in fish:
        if map_lst[f[0]][f[1]] > baby_size:
            visited[f[0]][f[1]] = True
            end_cnt += 1
        elif map_lst[f[0]][f[1]] != 0 and map_lst[f[0]][f[1]] < baby_size:
            cheak_fish.append(f)
        else:
            end_cnt += 1
    if end_cnt == len(fish):
        break
    bfs_lst = [[0] * N for _ in range(N)]
    result = BFS()
    if result == 0:
        break
print(time)