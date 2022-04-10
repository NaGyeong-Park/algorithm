import sys
from itertools import permutations,combinations
sys.stdin = open('input.txt')

T = int(input())


def BFS():
    # 빈칸 3개 조합 리스트를 돈다
    for b in blank:
        global result
        temp = 0
        # 빈칸 3개를 벽으로 만들어준다(False 상태)
        copy_check = [check[i][:] for i in range(N)]
        copy_check[b[0][0]][b[0][1]] = False
        copy_check[b[1][0]][b[1][1]] = False
        copy_check[b[2][0]][b[2][1]] = False

        # 바이러스를 퍼트려준다(BFS)
        q = virus[:]
        while q:
            nx, ny = q.pop(0)
            for d in range(4):
                x = dx[d] + nx
                y = dy[d] + ny
                # 인덱스 범위가 벗어나지않고, 빈 칸이면 바이러스를 퍼트려준다.
                if 0<=x<N and 0<=y<M and copy_check[x][y] == True:
                    q.append([x,y])
                    copy_check[x][y] = False
        # temp에 안전공간을 세어준다
        for i in range(N):
            temp += copy_check[i].count(True)
        # 기존 result 값보다 temp가 크다면 바꿔준다.
        if temp > result:
            result = temp


for tc in range(1, T + 1):
    
    print(f'#{tc} ',end='')

    N, M = map(int, input().split())
    virus = []
    blank = []
    result = 0
    check = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # 바이러스 리스트와 빈칸 리스트, check 리스트를 만들어준다.
    for i in range(N):
        check.append(list(map(int,input().split())))
        for j in range(M):
            if check[i][j] == 2:
                virus.append([i,j])
                check[i][j] = False
            elif check[i][j] == 1:
                check[i][j] = False
            else:
                check[i][j] = True
                blank.append([i,j])

    # 빈 칸의 3개 조합을 만들어준다.
    # combinations와 permutations의 시간 : 452ms 1824ms
    # combinations와 permutations의 메모리 : 119060KB 136240KB
    blank = list(combinations(blank,3))
    BFS()
    print(result)