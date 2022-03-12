import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = 1

def DFS(lst):
    cheak_lst = [[False]*M for _ in range(N)]
    alpha_x = [-1,-1,0,1,1,1,0,-1]
    alpha_y = [0,1,1,1,0,-1,-1,-1]
    cheak_x = [1,0,-1,0]
    cheak_y = [0,1,0,-1]
    day = 0
    stack = [start]
    lst[stack[0][0]][stack[0][1]] = 0
    cheak_lst[stack[0][0]][stack[0][1]] = True
    cnt = -1
    while cnt != 0:
        cnt = 0
        pprint(lst)
        while stack:
            cnt += 1
            a = stack.pop()
            x = a[0]
            y = a[1]
            for i in range(8):
                now_x = x + alpha_x[i]
                now_y = y + alpha_y[i]
                if 0 <= now_x < N and 0 <= now_y < M and lst[now_x][now_y] == 1 and cheak_lst[now_x][now_y] == False:
                    che_cnt = 0
                    for j in range(4):
                        now_x2 = now_x + cheak_x[j]
                        now_y2 = now_y + cheak_y[j]
                        if 0 <= now_x2 < N and 0 <= now_y2 < M and lst[now_x2][now_y2] == 1:
                            che_cnt +=1
                        elif 0 <= now_x2 < N and 0 <= now_y2 < M and cheak_lst[now_x2][now_y2] == True:
                            che_cnt += 1
                        elif now_x2 == x and now_y2 == y:
                            che_cnt +=1
                    if che_cnt != 4 :
                        stack.append([now_x, now_y])
                        lst[now_x][now_y] = 0
                        cheak_lst[now_x][now_y] = True
                        break
        day += 1
    return(day)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        if 1 in lst[i]:
            start = [i, lst[i].index(1)]
            break
    print(DFS(lst))