from itertools import combinations
from collections import deque
import copy

def BFS():
    for i in range(len(virus)):
        result_now = 0
        map_lst_copy = copy.deepcopy(map_lst)
        cheak_lst_copy = copy.deepcopy(cheak_lst)
        queue = deque(virus[i])
        for idx in range(M):
            cheak_lst_copy[queue[idx][0]][queue[idx][1]] = False
        while queue:
            now_x,now_y = queue.popleft()
            for j in range(4):
                x = now_x + direc_x[j]
                y = now_y + direc_y[j]
                if 0 <= x < N and 0 <= y < N and cheak_lst_copy[x][y] == True:
                    queue.append([x,y])
                    cheak_lst_copy[x][y] = False
                    map_lst_copy[x][y] = map_lst_copy[now_x][now_y] + 1
        for i in range(N):
            if True in cheak_lst_copy[i]:
                result_now = -1
                break
            min_num = max(map_lst_copy[i])
            if result_now <= min_num:
                result_now = min_num
        if result_now != -1:
            result.append(result_now)



N, M = map(int, input().split())
cheak_lst = [[True for _ in range(N)] for _ in range(N)]
map_lst = [0]*N
virus = []
result = []
direc_x = [1,-1,0,0]
direc_y = [0,0,1,-1]
for i in range(N):
    map_lst[i] = list(map(int, input().split()))
    for j in range(N):
        if map_lst[i][j] == 1:
            cheak_lst[i][j] = False
            map_lst[i][j] = -1
        elif map_lst[i][j] == 2:
            virus.append([i,j])
            map_lst[i][j] = 0
virus = list(combinations(virus, M))
BFS()
if len(result) == 0:
    print(-1)
else:
    print(min(result))