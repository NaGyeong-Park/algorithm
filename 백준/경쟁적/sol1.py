import sys
sys.stdin = open('input.txt')

T = int(input())

from collections import deque


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [0] * N
    q = []
    for i in range(N):
        arr[i] = list(map(int, input().split()))
        for j in range(N):
            if arr[i][j] > 0:
                q.append((i, j))
    q.sort()
    q = deque(q)
    S, X, Y = map(int, input().split())

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    if all(x == 0 for x in q):
        print(0)
    else:
        while q:
            nx, ny = q.popleft()
            for d in range(4):
                x = nx + dx[d]
                y = ny + dy[d]
                if 0 <= x < N and 0 <= y < N and arr[x][y] == 0:
                    q.append((x, y))
                    arr[x][y] = arr[nx][ny]
            if arr[nx][ny] == K:
                if not q:
                    break
                elif arr[q[0][0]][q[0][1]] != arr[nx][ny]:
                    cnt += 1
            if cnt == S:
                print(arr[X - 1][Y - 1])
                break