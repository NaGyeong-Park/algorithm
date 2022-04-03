import sys
import pprint

sys.stdin = open('input.txt')

T = 1

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    rob_n, rob_m, direc = map(int, input().split())
    map_lst = []
    for _ in range(N):
        map_lst.append(list(map(int, input().split())))


    def direction(x):
        if x == 1:
            lst = [[1,0],[0,1],[-1,0],[0,-1]]
        elif x == 0:
            lst = [[0,-1],[1,0],[0,1],[-1,0]]
        elif x == 2:
            lst = [[0,1],[-1,0],[0,-1],[1,0]]
        else:
            lst = [[-1,0],[0,-1],[1,0],[0,1]]
        return lst

    def robot(rob_n, rob_m,map_lst,direc):
        stop = 0
        result = 0
        cnt = 0

        while stop < 1 :
            if map_lst[rob_n][rob_m] == 0:
                map_lst[rob_n][rob_m] = 2
                result += 1
                for i in direction(direc):
                    if not map_lst[rob_n + i[0]][rob_m+i[1]]:
                        direc = direc + direction(direc).index(i)
                        if direc >= 4 :
                            direc = direc - 4
                        rob_n = rob_n + i[0]
                        rob_m = rob_m + i[1]
                        break
                    else:
                        cnt += 1
                        if cnt == 4:
                            if map_lst[rob_n+i[0]][rob_m+i[1]] == 1:
                                stop = 1
                                return result
                            else:
                                rob_n = rob_n + i[1]
                                rob_m = rob_m + i[1]

    a = robot(rob_n, rob_m, map_lst, direc)

    pprint.pprint(map_lst)
    print(f'#{tc} {a}')

