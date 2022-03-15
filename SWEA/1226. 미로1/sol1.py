import sys

sys.stdin = open('input.txt')

T = 10

def BFS():
    queue = [start]
    alpha_x = [1,0,-1,0]
    alpha_y = [0,1,0,-1]
    while queue:
        a = queue[0]
        queue = queue[1:]
        # 상하좌우 움직이기
        for i in range(4):
            x = alpha_x[i] + a[0]
            y = alpha_y[i] + a[1]
            if 0<= x < N and 0<= y <N and cheak[x][y] == False:
                lst[x][y] = lst[a[0]][a[1]] + 1
                queue.append([x,y])
                cheak[x][y] = True
                # 도착할 곳에 도착하면 그냥 끝내버리기
                if x == end[0] and y == end[1] :
                    return 1

for tc in range(1, T + 1):
    t = int(input())
    N = 16
    cheak = [[False]*N for _ in range(N)]
    lst = [0]*N
    for i in range(N):
        lst[i] = list(map(int,input()))
        for j in range(N):
            if lst[i][j] == 0:
                pass
            elif lst[i][j] == 1:
                cheak[i][j] = True
            # 시작 인덱스
            elif lst[i][j] == 2:
                start = [i, j]
            # 끝 인덱스
            elif lst[i][j] == 3:
                end = [i,j]
    # 시작 위치 값 0으로 초기화
    lst[start[0]][start[1]] = 0
    print(f'#{tc}', end=' ')
    result = BFS()
    # 도착 할곳에 도착하지 못하면 return값 없으므로 0 출력
    if result == None:
        print(0)
    else:
        print(result)