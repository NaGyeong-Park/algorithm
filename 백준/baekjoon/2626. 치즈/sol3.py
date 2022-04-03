import sys
from pprint import pprint
sys.stdin = open('input.txt')


N, M = map(int, input().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cheak_x = [1, 0, -1, 0]
cheak_y = [0, 1, 0, -1]

def BFS():
    queue = [[0, 0]]
    cheak_lst = [[True] * M for _ in range(N)]
    while queue:
        x = queue[0][0]
        y = queue[0][1]
        queue = queue[1:]
        cheak_lst[x][y] = False
        for i in range(4):
            now_x = x + cheak_x[i]
            now_y = y + cheak_y[i]
            if 0 <= now_x < N and 0 <= now_y < M and lst[now_x][now_y] == 0 and cheak_lst[now_x][now_y] == True and not [now_x,now_y] in queue:
                queue.append([now_x, now_y])
    return cheak_lst

def find_day():
    cnt = -1
    day = 0
    while cnt != 0:
        last = cnt
        cnt = 0
        cheak_lst = BFS()
        for i in range(N):
            for j in range(M):
                if lst[i][j] == True:
                    if lst[i][j] == 1:
                        for k in range(4):
                            now_x = i + cheak_x[k]
                            now_y = j + cheak_y[k]
                            if 0 <= now_x < N and 0 <= now_y < M and cheak_lst[now_x][now_y] == False:
                                cnt += 1
                                lst[i][j] = 0
                                break
        day += 1
    return (day-1, last)

result = find_day()
print(result[0])
print(result[1])