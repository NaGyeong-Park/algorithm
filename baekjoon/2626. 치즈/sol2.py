import sys
from pprint import pprint
from copy import deepcopy
sys.stdin = open('input.txt')

T = 1


for tc in range(1, T + 1):
    
    print(f'#{tc} ')

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        cheak_lst = [[True] * M for _ in range(N)]
        alpha_x = [-1, 0, 1, 0]
        alpha_y = [0, -1, 0, 1]

        def BFS():
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
                        queue.append([now_x, now_y])
            return cheak_lst


        def find_day():
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
                BFS()
                pprint(cheak_lst)
                pprint(lst)
            return (day, last)
        BFS()
        result = find_day()
        print(result)