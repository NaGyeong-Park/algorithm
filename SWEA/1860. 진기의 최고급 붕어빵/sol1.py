import sys

sys.stdin = open('input.txt')

T = int(input())

# N명 시간 M초 붕어빵 K개
def count_people(lst,N,M,K):
    num = (lst[0]//M)*M              # 첫 손님이 방문하기 전 마지막으로 붕어빵이 나온 시간
    boog = K*(lst[0]//M)             # 손님이 처음 왔을 때 만들어져있는 붕어빵 갯수
    pp = 0                           # 손님 리스트 인덱스는 0부터
    while pp < N:                    # 인덱스 범위만큼 반복
        if boog < 0:                 # 붕어빵이 없으면 불가능
            return 'Impossible'
        if num <= lst[pp] < num+M:   # 손님이 현재 시간대에 도착했다면
            boog -= 1                # 붕어빵 머거
            pp += 1                  # 다음손님~ 인덱스!
        elif num + M <= lst[pp]:     # 손님이 현재 시간대에 오지 않았다면
            num += M                 # 다음 붕어빵 나오는 시간으로 기준 바꿔주기
            boog += K                # 그만큼 붕어빵도 만들어주기
    return 'Possible'                # 조건문에서 걸리는 게 없었다면 가능!

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())         # 입력
    visit_sec = list(map(int, input().split()))
    visit_sec.sort()                            # 손님들 온 시간대로 정렬
    if visit_sec[0] < M:                        # 손님이 M초보다 빨리왔으면
        print(f'#{tc} Impossible')              # 기다려야되용;^;
    else:                                       # 아니면 함수사용 return
        result = count_people(visit_sec,N,M,K)
        print(f'#{tc} {result}')