import sys
from collections import deque

def back_ground():
    global cheese, first_back
    q = deque([(0, 0)])
    if not first_back:
        arr[0][0] = 3
    else:
        arr[0][0] = first_back
    cheese = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not first_back:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = 3
                        q.append((nx, ny))
                    elif arr[nx][ny] == 1:
                        cheese.add((nx, ny))
                else:
                    if arr[nx][ny] == 1:
                        cheese.add((nx, ny))
                    elif not arr[nx][ny] or arr[nx][ny] == first_back - 1:
                        arr[nx][ny] = first_back
                        q.append((nx, ny))
    cheese = list(cheese)


def BFS():
    q2 = deque(cheese)
    while q2:
        x, y = q2.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == first_back:
                cnt += 1
                if cnt >= 2:
                    break
        if cnt > 1:
            arr[x][y] = 0


N, M = map(int, sys.stdin.readline().split(' '))
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
first_back = 0
back_ground()
first_back = 3
while cheese:
    result += 1
    BFS()
    first_back += 1
    back_ground()
print(result)