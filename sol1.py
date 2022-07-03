import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input.txt')

T = int(input())

def BFS(start, size_eat):
    visited = [[0]*N for _ in range(N)]
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    q = deque([start])
    visited[start[0]][start[1]] = 1
    temp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N:
                if (not MAP[nx][ny] or MAP[nx][ny] == size_eat[0]) and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                elif 0 < MAP[nx][ny] < size_eat[0] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                    temp.append([visited[nx][ny],nx,ny])
    return temp,visited

for tc in range(1, T + 1):
    
    print(f'#{tc} ')
    N = int(sys.stdin.readline())
    check = [[False]*N for _ in range(N)]
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    baby = [2,0]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 9:
                start = [i,j]
                MAP[i][j] = 0
    count = 0
    end = 0
    while not end:
        e, visit = BFS(start, baby)
        if e:
            a = deepcopy(e)
            e.sort(key=lambda x : x[2])
            e.sort(key=lambda x : x[1])
            e.sort(key=lambda x : x[0])
            start = e[0][1:]
            count += visit[start[0]][start[1]]-1

            baby[1] += 1
            if baby[0] == baby[1]:
                baby = [baby[0]+1,0]
                MAP[start[0]][start[1]] = 0
        else:
            end = 1
    print(count)