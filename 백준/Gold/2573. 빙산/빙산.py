import copy
from collections import deque


def BFS():
    global arr, carr
    carr = copy.deepcopy(arr)
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            x = dx[i] + nx
            y = dy[i] + ny
            if 0<=x<N and 0<=y<M and not arr[x][y] and carr[nx][ny]:
                    carr[nx][ny] -= 1
    arr = carr

def check_piece():
    cq = deque()
    cnt_piece = 0
    temp = False
    for i in range(N):
        for j in range(M):
            if cnt_piece > 1:
                return cnt_piece
            if arr[i][j]:
                q.append([i, j])
                if check[i][j]:
                    cq.append([i,j])
                    temp = True
                    check[i][j] = False
                    while cq:
                        cx, cy = cq.popleft()
                        for d in range(4):
                            x = cx + dx[d]
                            y = cy + dy[d]
                            if 0<=x<N and 0<=y<M and check[x][y] and arr[x][y]:
                                cq.append([x,y])
                                check[x][y] = False
                    cnt_piece += 1
    if temp == False:
        return False
    return cnt_piece


N, M = map(int, input().split())
arr = [0]*N
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    arr[i] = list(map(int, input().split()))
result = 0

while True:
    check = [[True]*M for _ in range(N)]
    piece = check_piece()
    if piece == False:
        result = 0
        break
    elif piece > 1:
        break
    BFS()
    result += 1
print(result)
