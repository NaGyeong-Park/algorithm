import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

def find_min(x,y,sum_num):
    global result
    # 맨 끝 위치에 도달했으면
    if x == N-1 and y == N-1:
        # 맨 마지막 위치 값을 더해주고 결과값과 비교해 더 작다면 결과값 갱신
        sum_num += map_lst[x][y]
        if result > sum_num:
            result = sum_num
            return
    # 재귀 도중 sum_num값이 이미 결과값보다 크다면 재귀 나오기
    if sum_num > result:
        return
    # 상 우로 확인
    for i in range(2):
        now_x = x + direc_x[i]
        now_y = y + direc_y[i]
        # 인덱스 범위 안나가고, 방문하지 않았다면
        if 0<=x<N and 0<=y<N and cheak_lst[x][y] == True:
            cheak_lst[x][y] = False # 방문처리
            find_min(now_x,now_y,sum_num+map_lst[x][y]) #이동한 값 재귀
            cheak_lst[x][y] = True # 나와서 다시 노방문~

for tc in range(1, T + 1):
    
    print(f'#{tc} ', end='')
    N = int(input())
    # 상, 우로 이동
    direc_x = [1,0]
    direc_y = [0,1]
    cheak_lst = [[True]*N for _ in range(N)]
    map_lst = [list(map(int, input().split())) for _ in range(N)]
    result = 10*2*N # 최대값으로 해줌
    find_min(0,0,0)
    print(result)