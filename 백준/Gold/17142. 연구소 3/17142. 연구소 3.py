import sys

sys.stdin = open('input.txt')
from itertools import combinations
from collections import deque
import copy
T = int(input())

def BFS():
    # 바이러스 조합 다 돌기
    for i in range(len(virus_lst)):
        # map과 cheak 리스트 딥카피로 복사해주기(계속 쓰려구)
        result_now = 0
        map_lst_copy = copy.deepcopy(map_lst)
        cheak_lst_copy = copy.deepcopy(cheak_lst)
        # 큐 값에 조합넣기
        queue = deque(virus_lst[i])
        # 큐 안에 있는 값들 다 방문 흔적 남기기
        for idx in range(M):
            cheak_lst_copy[queue[idx][0]][queue[idx][1]] = False

        # BFS
        while queue:
            now_x,now_y = queue.popleft()
            for j in range(4):
                x = now_x + direc_x[j]
                y = now_y + direc_y[j]
                if 0 <= x < N and 0 <= y < N and cheak_lst_copy[x][y] == True:
                    queue.append([x,y])
                    cheak_lst_copy[x][y] = False
                    map_lst_copy[x][y] = map_lst_copy[now_x][now_y] + 1

        # 최소값 찾기
        for i in range(N):
            for j in range(N):
                if [i,j] in virus:
                    map_lst_copy[i][j] = -1
            # 하나라도 바이러스가 안퍼졌으면 -1로 break해 결과값 안주기
            if True in cheak_lst_copy[i]:
                result_now = -1
                break
            # 그 행의 최댓값 찾아 result_now보다 크면 result_now를 min_num으로 갱신
            min_num = max(map_lst_copy[i])
            if result_now < min_num:
                result_now = min_num
        # result_now 값이 -1이 아니면, 결과값 리스트에 넣어준다.
        if result_now != -1:
            result.append(result_now)


for tc in range(1, T + 1):
    print(f'#{tc} ', end='')
    # N, M, cheak_lst, map_lst, virus 위치(위치 입력시 그 위치 map에서 0으로 바꿔줌), 상하좌우 리스트, 결과값 리스트 입력
    N, M = map(int, input().split())
    cheak_lst = [[True for _ in range(N)] for _ in range(N)]
    map_lst = [0]*N
    virus = []
    result = []
    direc_x = [1,-1,0,0]
    direc_y = [0,0,1,-1]
    # map 입력받기
    for i in range(N):
        map_lst[i] = list(map(int, input().split()))
        for j in range(N):
            # 벽이면 cheak_lst에 False로 표시해주고, map에 -1로 해주기
            # -1로 하는 이유는 바이러스 놓자마자 퍼지는 상황 대비!(벽이 1이므로 시간이 1로 나옴)
            if map_lst[i][j] == 1:
                cheak_lst[i][j] = False
                map_lst[i][j] = -1
            # 2는 바이러스 좌표 리스트에 넣어주고, map에서는 0으로 표기
            elif map_lst[i][j] == 2:
                virus.append([i,j])
                map_lst[i][j] = 0
    # 바이러스 M개를 놓을 수 있는 조합
    virus_lst = list(combinations(virus, M))

    # BFS
    BFS()

    # 만약 result 리스트가 비었으면 바이러스 퍼질 수 없음
    # 아니면 최소시간 출력
    if len(result) == 0:
        print(-1)
    else:
        print(min(result))