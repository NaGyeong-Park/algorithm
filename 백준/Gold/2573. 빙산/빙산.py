import sys
import copy
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

# 빙하 녹이기
def BFS():
    global arr, carr
    carr = [x[:] for x in arr]
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            x = dx[i] + nx
            y = dy[i] + ny
            if 0<=x<N and 0<=y<M and not arr[x][y] and carr[nx][ny]:
                    carr[nx][ny] -= 1
    arr = carr

# 빙하 체크!
def check_piece():
    cq = deque()
    cnt_piece = 0
    # 빙하 모두 녹았는지 check할 변수 생성
    temp = False
    # 모든 map 탐색
    for i in range(N):
        for j in range(M):
            # 빙하 조각이 2개 이상이면 바로 return
            if cnt_piece > 1:
                return cnt_piece
            # 빙하가 있다면
            if arr[i][j]:
                # 일단 q에(녹일거에) 넣어주고
                q.append([i, j])
                # 방문하지 않은 빙하라면
                if check[i][j]:
                    # 조각 탐색에 넣어준다
                    cq.append([i,j])
                    temp = True
                    check[i][j] = False
                    # 주변 빙하 탐색
                    while cq:
                        cx, cy = cq.popleft()
                        for d in range(4):
                            x = cx + dx[d]
                            y = cy + dy[d]
                            # 주변 빙하들을 모두 방문처리 해준다
                            if 0<=x<N and 0<=y<M and check[x][y] and arr[x][y]:
                                cq.append([x,y])
                                check[x][y] = False
                    # 빙하탐색 BFS를 나왔다면 조각 한개 추가
                    cnt_piece += 1
    # 만약 모든 빙하가 녹앗다면 False return
    if temp == False:
        return False
    # 아니라면 빙하 조각 return
    return cnt_piece


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0]*N
    q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    result = 0

    # 모든 빙하가 녹을 때까지 or 조각이 2조각 이상일 때까지 반복
    while True:
        # 빙하 조각 check 및 q에 넣을 요소 탐색
        check = [[True]*M for _ in range(N)]
        piece = check_piece()
        # 만약 빙하 모두 녹았다면 0 출력
        if piece == False:
            result = 0
            break
        # 빙하가 2개 이상이라면 시간 출력
        elif piece > 1:
            break
        # 빙하 녹이기 BFS
        BFS()
        # 시간 +1
        result += 1
    print(result)