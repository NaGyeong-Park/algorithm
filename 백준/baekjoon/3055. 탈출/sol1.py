import sys
from collections import deque

sys.stdin = open('input.txt')

T = 4

def BFS1():
    while queue1:
        i, j = queue1.popleft()
        cheak_lst[i][j] = False
        for k in range(4):
            x = alpha_x[k] + i
            y = alpha_y[k] + j
            if 0<=x<R and 0<=y<C and cheak_lst[x][y] == True and lst[x][y] == 0:
                if map_lst[x][y] != 'D':
                    map_lst[x][y] = '*'
                    lst[x][y] = lst[i][j] + 1
                    queue_nxt1.append([x,y])
                    cheak_lst[i][j] = False
                elif map_lst[x][y] == 'D':
                    cheak_lst[i][j] = False
                    lst[x][y] = lst[i][j] + 1
                    queue_nxt1.append([x,y])

def BFS2():
    global cnt_all
    cnt_all += 1
    while queue2:
        i, j = queue2.popleft()
        cheak_lst2[i][j] = False
        if map_lst[i][j] == 'S':
            for k in range(4):
                x = alpha_x[k]+i
                y = alpha_y[k]+j
                if 0 <= x < R and 0 <= y < C and cheak_lst2[x][y] == True:
                    if map_lst[x][y] =='.' or map_lst[x][y] =='S':
                        lst2[x][y] = lst2[i][j] + 1
                        queue_nxt2.append([x,y])
                        map_lst[x][y] = 'S'
                        map_lst[i][j] = '.'
                    elif map_lst[x][y] == '*':
                        cheak_lst2 == False
                    elif map_lst[x][y] == 'D':
                        lst2[x][y] = lst2[i][j] + 1
                        print(f'findlst2{lst2}')
                        cnt_all += 1
                        break

for tc in range(1, T + 1):
    R, C = map(int, input().split())
    map_lst = [0]*R
    cheak_lst = [0]*R
    alpha_x = [1,0,-1,0]
    alpha_y = [0,1,0,-1]
    queue1 = deque([])
    for i in range(R):
        map_lst[i] = list(input())
        cheak_lst[i] = [True]*C
        for j in range(C):
            if map_lst[i][j] == 'X':
                cheak_lst[i][j] = False
            elif map_lst[i][j] == 'S':
                start = [i,j]
            elif map_lst[i][j] == 'D':
                end = [i,j]
            elif map_lst[i][j] == '*':
                queue1.append([i,j])
    queue_nxt1 = deque([])
    queue_nxt2 = deque([])


    cnt_all = 0
    lst = [[0] * C for _ in range(R)]
    lst2 = [[0] * C for _ in range(R)]
    cheak_lst2 = [[True] * C for _ in range(R)]
    queue2 = deque([start])

    while True:
        BFS2()
        BFS1()

        if lst2[end[0]][end[1]] != 0:
            print(f'#{tc} {lst2[end[0]][end[1]]}')
            break
        elif cnt_all >= 2500:
            if   
            print(f'#{tc} KAKTUS')
            break

        queue1 = queue_nxt1
        queue2 = queue_nxt2
        queue_nxt1 = queue_nxt2 = deque([])