
from collections import deque
from itertools import combinations



def BFS():
    for now in range(len(home)):
        cheak = [[False] * N for _ in range(N)]
        Q = deque()
        Q.append(home[now])
        city[home[now][0]][home[now][1]] = 0
        cheak[home[now][0]][home[now][1]] = True
        while Q:
            now_x, now_y = Q.popleft()
            for i in range(4):
                x = now_x + dx[i]
                y = now_y + dy[i]
                if 0 <= x < N and 0 <= y < N and cheak[x][y] == False:
                    Q.append([x, y])
                    city[x][y] = city[now_x][now_y] + 1
                    cheak[x][y] = True
        for chi in range(len(chicken)):
            km[now][chi] = city[chicken[chi][0]][chicken[chi][1]]


def choose():
    global result
    for i in choose_lst:
        temp = 0
        for k in range(len(km)):
            temp_now = 1000000000
            for j in i:
                if temp_now > km[k][j]:
                    temp_now = km[k][j]
            temp += temp_now
            if temp > result:
                break
        if result > temp:
            result = temp
    print(result)


N, M = map(int, input().split())
city = [0] * N
home = []
chicken = []
for i in range(N):
    city[i] = list(map(int, input().split()))
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            home.append([i, j])
km = [[0] * len(chicken) for _ in range(len(home))]
choose_lst = list(combinations(list(range(len(chicken))), M))
result = 1000000000
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
BFS()
choose()
