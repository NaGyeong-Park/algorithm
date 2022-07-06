import sys
from collections import deque


def check_island():
    global island, land_num, start, land_idx
    temp_lst = []
    q = deque([start])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] and not island[nx][ny]:
                    map[nx][ny] = land_num
                    island[nx][ny] = True
                    q.append((nx, ny))
                if not map[nx][ny] and map[x][y] and not (x,y) in temp_lst:
                    temp_lst.append((x, y))
    land_idx.append(temp_lst)


def BFS(n,min_num):
    global answer
    q = deque(land_idx[n - 1])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if temp_map[x][y] + 1 > min_num:
                    break
                if temp_map[nx][ny] == 0:
                    if temp_map[x][y] == -n:
                        temp_map[nx][ny] = 1
                    else:
                        temp_map[nx][ny] = temp_map[x][y] + 1
                    q.append((nx, ny))
                elif temp_map[nx][ny] != -n and temp_map[nx][ny] < 0:
                    if temp_map[x][y] < min_num:
                        min_num = temp_map[x][y]
                elif temp_map[x][y] != -n and temp_map[nx][ny] > temp_map[x][y] + 1:
                    temp_map[nx][ny] = temp_map[x][y] + 1
                    q.append((nx, ny))
    return min_num


N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
land_num = 0
land_idx = []
answer = 2000000
island = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not island[i][j] and map[i][j]:
            land_num -= 1
            map[i][j] = land_num
            island[i][j] = True
            start = (i, j)
            check_island()
for i in range(abs(land_num) - 1):
    temp_map = [row[:] for row in map]
    result = BFS(i + 1,answer)
    if result < answer:
        answer = result
print(answer)