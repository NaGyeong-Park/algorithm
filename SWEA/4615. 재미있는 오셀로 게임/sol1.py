import sys

sys.stdin = open('sample_input.txt')

T = int(input())


# 오셀로 함수
def Othello(matrix, N, c,r, color):
    r_idx = [-1, -1, -1, 0, 0, 1, 1, 1]                 # 8군데를 둘러볼 r인덱스
    c_idx = [-1, 0, 1, -1, 1, -1, 0, 1]                 # 8군데를 둘러볼 c인덱스
    c = c-1                                             # 리스트의 인덱스는 0부터여서
    r = r-1                                             # 위치 입력값에 1을 빼줌
    matrix[r][c] = color                                # 말을 놓은 자리의 색을 내 색으로 바꿔줌

    for i in range(8):                                  # 8군데 탐색
        n = r_idx[i] + r                                # 둘러볼 위치 설정
        m = c_idx[i] + c
        if n < 0 or m < 0 or n >= N or m >= N:          # 둘러볼 곳이 인덱스 범위를 넘으면 pass
            pass
        else:
            if matrix[n][m] != color and matrix[n][m] != 0:    # 둘러볼 곳의 값이 다른 말이면
                chan_n = n
                chan_m = m
                cnt = 0
                find_col = 0
                while True:                                    # 둘러 볼 곳이 인덱스 범위 넘으면 break
                    if chan_m == -1 or chan_n == -1 or chan_m >= N or chan_n >= N:
                        break
                    else:
                        if matrix[chan_n][chan_m] == color:    # 둘러 볼 곳의 색이 내 색이면
                            find_col = 1                       # 그 사이에 다른 말이 껴있는 거니까
                            break                              # 찾았다고 알려주는 변수를 1로 바꿔주고 while 문 나오기
                        elif matrix[chan_n][chan_m] == 0:      # 둘러볼 곳이 0이면 내 색 사이에 다른 말이 없으니까 그냥 나오기
                            break
                        chan_n += r_idx[i]                     # 둘러볼 방향으로 한 번 더 움직이기
                        chan_m += c_idx[i]
                        cnt += 1                               # 둘러본 횟수 count

                if find_col == 1:                       # while문을 나왔는데 찾았다고 알려주는 변수 값이 1이면
                    for k in range(cnt):                # 초기 chan_n,m의 위치는 내 색이었기때문에 한번 뒤로 가주기
                        chan_n -= r_idx[i]              # 그리고 for문을 돌면서 탐색한 횟수만큼 내 색으로 바꿔주기
                        chan_m -= c_idx[i]
                        matrix[chan_n][chan_m] = color
    return matrix


for tc in range(1, T + 1):
    N, K = map(int, input().split())                # matrix 크기 N과 게임 횟수 K 입력
    matrix = [[0]*N for _ in range(N)]              # NxN matrix 생성
    fir = int(N/2)                                  # 초기 말을 세워주기 위한 가운뎃 값 할당
    matrix[fir-1][fir-1] = matrix[fir][fir] = 2     # 흰색 말 놓기
    matrix[fir-1][fir] = matrix[fir][fir-1] = 1     # 검은색 말 놓기

    for i in range(K):                              # 말을 놓을 때마다 매트리스 바꿔주기
        c, r, color = map(int,input().split())      # c, r, 말 색 입력
        Othello(matrix, N, c,r,color)               # 오셀로 함수에 넣어준다



    cnt_1 = 0
    cnt_2 = 0
    for i in range(N):                              # matrix의 검은 말/흰 말 갯수 세어주기
        for j in range(N):
            if matrix[i][j] == 1:
                cnt_1 +=1
            elif matrix[i][j] == 2:
                cnt_2 +=1

    print(f'#{tc} {cnt_1} {cnt_2}')                # 출력

