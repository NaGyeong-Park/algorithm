from collections import deque
import sys

sys.setrecursionlimit(10**5)

def BFS():
    global days
    while True:
        nation = []
        cnt = 0
        cheak = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if cheak[i][j] == False:
                    Q = deque()
                    Q.append([i,j])
                    cheak[i][j] = True
                    nation.append([[continent[i][j],i,j]])
                    while Q:
                        now_x, now_y = Q.popleft()
                        for d in range(4):
                            x = now_x + dx[d]
                            y = now_y + dy[d]
                            if 0<=x<N and 0<=y<N and not cheak[x][y] and L <= abs(continent[now_x][now_y] - continent[x][y]) <= R:
                                Q.append([x,y])
                                cheak[x][y] = True
                                nation[cnt].append([continent[x][y],x,y])
                    cnt += 1
        end_cnt = 0
        for i in range(len(nation)):
            if len(nation[i]) != 1:
                num = list(zip(*nation[i]))[0]
                sum_num = sum(num)//len(nation[i])
                for idx in nation[i]:
                    continent[idx[1]][idx[2]] = sum_num
            else:
                end_cnt += 1
        if end_cnt == N*N:
            return print(days)
        days += 1

N, L, R = map(int,input().split())
continent = [list(map(int, input().split())) for _ in range(N)]
nation = []
dx = [1,0,-1,0]
dy = [0,-1,0,1]
days = 0
BFS()