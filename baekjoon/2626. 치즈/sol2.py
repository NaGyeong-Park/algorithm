import sys
from pprint import pprint
from copy import deepcopy
sys.stdin = open('input.txt')

T = 1


def BFS(lst, cheak_lst):
    queue = [[0, 0]]
    while queue:
        x = queue[0][0]
        y = queue[0][1]
        queue = queue[1:]
        cheak_lst[x][y] = False
        for i in range(4):
            now_x = x + alpha_x[i]
            now_y = y + alpha_y[i]
            if 0 <= now_x < N and 0 <= now_y < M and lst[now_x][now_y] == 0 and cheak_lst[now_x][now_y] == True:
                queue.append([now_x,now_y])
    return cheak_lst

def find_day(lst, cheak_lst):
    cnt = -1
    day = 0
    while cnt != 0:
        last = cnt
        cnt = 0
        for i in range(N):
            for j in range(M):
                if lst[i][j] == True:
                    if lst[i][j] == 1:
                        for k in range(4):
                            now_x = i + alpha_x[k]
                            now_y = j + alpha_y[k]
                            if 0 <= now_x < N and 0 <= now_y < M and cheak_lst[now_x][now_y] == False:
                                cnt += 1
                                lst[i][j] = 0
                                break
        day += 1
        cheak_lst = BFS(lst, cheak_lst)
    return (day, last)
for tc in range(1, T + 1):
    
    print(f'#{tc} ')

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        cheak_lst = [[True] * M for _ in range(N)]
        for i in range(N):
            if 1 in lst[i]:
                start = [i-1, lst[i].index(1)]
                break
        alpha_x = [-1, 0, 1, 0]
        alpha_y = [0, -1, 0, 1]
        cheak = BFS(lst,cheak_lst)
        result = find_day(lst, cheak)
        print(result)