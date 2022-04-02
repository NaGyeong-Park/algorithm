import sys
sys.stdin = open('input.txt')

T = int(input())


def DFS():
    global d
    stack = [[r,c]]
    v = -1
    while stack or v != 0:
        v = 0
        now_x, now_y = stack.pop()
        map_lst[now_x][now_y] = 2
        for i in range(4):
            direc = (d+i)%4
            x = now_x + direc_x[direc]
            y = now_y + direc_y[direc]
            if 0<=x<N and 0<=y<M and map_lst[x][y] == 0:
                stack.append([x,y])
                d = direc + 1
                v = 1
                break
        if v == 0:
            back_x = now_x+direc_x[(d+1)%4]
            back_y = now_y+direc_y[(d+1)%4]
            if map_lst[back_x][back_y] == 2:
                stack.append([back_x,back_y])
                v = 1
            elif map_lst[back_x][back_y] == 1:
                v = 0
                return

def direction(d):
    if d == 3:
        d = 1
    elif d == 1:
        d = 3
    else:
        d = d
    return d

for tc in range(1, T + 1):
    
    print(f'#{tc} ',end='')
    N, M = map(int, input().split())
    r,c,d = map(int, input().split())
    map_lst = [0]*N
    for i in range(N):
        map_lst[i] = list(map(int,input().split()))
    map_lst[r][c] = 2
    d = direction(d)
    direc_x = [0,1,0,-1]
    direc_y = [-1,0,1,0]
    DFS()
    cnt = 0
    for i in range(N):
        cnt += map_lst[i].count(2)
    print(cnt)