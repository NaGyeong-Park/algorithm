import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())


def BFS(nx,ny):
    cnt = 0
    q = deque()
    q.append([nx,ny])
    v[nx][ny] = True
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<N and arr[ax][ay] and not v[ax][ay]:
                v[ax][ay] = True
                q.append([ax,ay])
    return cnt
for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    v = [[False]*N for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not v[i][j]:
                result.append(BFS(i,j))
    result.sort()
    print(len(result))
    for i in result:
        print(i)