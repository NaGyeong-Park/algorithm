import sys

sys.stdin = open('input.txt')

T = 4


def find_days(map):
    x_dir = [-1,1,0,0,-1,1]
    y_dir = [0,0,-1,1,0,0]
    day = 0
    cnt_now = 0
    while cnt_now != N*H:
        cnt_now = 0
        for floor in range(H):
            for x in range(N):
                if not 0 in map[floor][x]:
                    cnt_now += 1
                    if cnt_now == N*H:
                        return day
                for y in range(M):
                    if map[floor][x][y] == 1:
                        for i in range(6):
                            if i < 2:
                                my_h = floor + x_dir[i]
                                my_x = x + y_dir[i]
                                my_y = y + y_dir[i]
                                if -1 < my_h < H and map[my_h][my_x][my_y] == 0:
                                    map[my_h][my_x][my_y] = 1
                            else:
                                my_x = x + x_dir[i]
                                my_y = y + y_dir[i]
                                if -1 < my_x < N and -1 < my_y < M and map[floor][my_x][my_y] == 0:
                                    map[floor][my_x][my_y] = 1
                    elif map[floor][x][y] == 0:
                        cnt = 0
                        for i in range(6):
                            if i < 2:
                                my_h = floor + x_dir[i]
                                my_x = x + y_dir[i]
                                my_y = y + y_dir[i]
                                if -1 < my_h < H and map[my_h][my_x][my_y] == -1:
                                    cnt += 1
                                elif my_h < 0 or my_h >= H:
                                    cnt += 1
                            else:
                                my_x = x + x_dir[i]
                                my_y = y + y_dir[i]
                                if -1 < my_x < N and -1 < my_y < M and map[floor][my_x][my_y] == -1:
                                    cnt += 1
                                elif my_x < 0 or my_x >= N or my_y < 0 or my_y >= M:
                                    cnt += 1
                        if cnt == 6:
                            return -1
        day += 1

for tc in range(1, T + 1):
    print(f'#{tc} ')
    M,N,H = map(int, input().split())
    lst = [0]*H
    cnt_all = 0
    cnt_all1 = 0
    for j in range(H):
        lst[j] = [0]*N
        for i in range(N):
            lst[j][i] = list(map(int, input().split()))
            if not 0 in lst[j][i]:
                cnt_all +=1
    if cnt_all == N*H:
        print(0)
    else:
        print(find_days(lst))


