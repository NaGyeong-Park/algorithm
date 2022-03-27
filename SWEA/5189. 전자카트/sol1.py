import sys

sys.stdin = open('input.txt')

T = int(input())


def find_min(x, cnt):
    global result
    # 이동 횟수가 다 되었다면
    if cnt == N-1:
        # 0으로 돌아가는 값까지 총합을 구해
        sum_num = sum(arr) + map_lst[x][0]
        # 결과값과 비교해 더 작으면 결과값 갱신
        if result > sum_num:
            result = sum_num
            return
    # 재귀를 돌면서 이미 결과값보다 arr의 총합이 크다면 재귀 나오기
    if sum(arr) > result:
        return
    for i in range(len(cheak_lst)):
        if cheak_lst[i]:
            # 방문처리
            cheak_lst[i] = False
            # 어레이에 현재 위치의 map값을 넣어준다
            arr.append(map_lst[x][i])
            # 재귀
            find_min(i, cnt+1)
            arr.pop()
            # 다시 방문 안함으로 처리
            cheak_lst[i] = True


for tc in range(1, T + 1):
    print(f'#{tc} ', end='')
    N = int(input())
    cheak_lst = [[True] * N for _ in range(N)]
    # 0은 시작하는 곳이니까 방문처리 해주기!
    cheak_lst[0] = False
    map_lst = [list(map(int, input().split())) for _ in range(N)]
    # 결과값은 최대로 해놓기
    result = 100*11
    arr = []
    find_min(0, 0)
    print(result)