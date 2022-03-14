import sys
from collections import deque

N, M, F = map(int, input().split())
lst = [0 for _ in range(N)]
cheak_lst = [[False for _ in range(N)] for _ in range(N)]
cnt_lst = [[0 for _ in range(N)] for _ in range(N)]
find_x = [1, 0, -1, 0]
find_y = [0, 1, 0, -1]

for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if lst[i][j] == 1:
            cheak_lst[i][j] = True

people = [0 for _ in range(M + 1)]
for i in range(M + 1):
    people[i] = list(map(int, sys.stdin.readline().split()))
    people[i][0] -= 1
    people[i][1] -= 1
    if i > 0:
        people[i][2] -= 1
        people[i][3] -= 1

for _ in range(M):
    def BFS():
        cnt_lst = [[0 for _ in range(N)] for _ in range(N)]
        queue = deque([people[0]])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                now_x = x + find_x[i]
                now_y = y + find_y[i]
                if 0 <= now_x < N and 0 <= now_y < N:
                    if cheak_lst[now_x][now_y] == False and cnt_lst[now_x][now_y] == 0:
                        queue.append([now_x, now_y])
                        cnt_lst[now_x][now_y] = cnt_lst[x][y] + 1
        cnt_lst[people[0][0]][people[0][1]] = 0
        return cnt_lst


    def find_short():
        min_val = 401
        people[0] = end = [0, 0]
        cnt_error = 0
        for i in range(1, M + 1):
            if people[i][0] == False:
                cnt_error += 1
            else:
                cnt_km = cnt_lst[people[i][0]][people[i][1]]
                if cnt_km == 0 and people[i][0] != people[0][0] and people[i][0] != people[0][1]:
                    cnt_error += 1

                if cnt_km == min_val:
                    if people[i][0] == people[0][0]:
                        if people[i][1] < people[0][1]:
                            min_val = cnt_km
                            people[0] = [people[i][0], people[i][1]]
                    elif people[i][0] < people[0][0]:
                        min_val = cnt_km
                        people[0] = [people[i][0], people[i][1]]
                elif cnt_km < min_val:
                    min_val = cnt_km
                    people[0] = [people[i][0], people[i][1]]

        for i in range(1, M + 1):
            if people[i][:2] == people[0]:
                end = people[i][2:]
                people[i] = [False, False]
        if cnt_error == M:
            if M == 1:
                pass
            else:
                print(-1)
                exit(0)
        return min_val, people, end


    cnt_lst = BFS()
    min_val, people, end = find_short()
    F -= min_val
    if F < 0 or type(F) == None:
        print(-1)
        exit(0)
    else:
        cnt_lst = BFS()
        distance = cnt_lst[end[0]][end[1]]
        F -= distance
        if F < 0:
            print(-1)
            exit(0)
        F += distance * 2
        people[0] = [end[0], end[1]]

print(F)