import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    print(f'#{tc} ',end='')
    N = int(input())
    # time_lst의 각 리스트 요소 두번째 요소를 기준으로 오름차순 sort
    time_lst = [list(map(int,input().split())) for i in range(N)]
    time_lst.sort(key= lambda x : x[1])
    cnt = 0
    end = 0
    for i in time_lst:
        # 시작시간이 현재 끝나는 시간이랑 같거나 크다면
        if i[0] >= end:
            # 한명 더 추가요~ / end값 i의 종료시간으로 갱신
            cnt+=1
            end=i[1]
    print(cnt)