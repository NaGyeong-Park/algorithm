import sys

sys.stdin = open('s_input.txt')

T = int(input())

# 지나가는 노선 카운트
def cnt_pass_bus(line_lst, sta_num):
    cnt = 0
    # 버스 노선의 사이에 정거장 번호가 있으면
    # 카운트
    for i in line_lst:
        if i[0] <= sta_num <= i[1]:
            cnt += 1
    return cnt


for tc in range(1, T + 1):
    # 버스 노선 갯수 입력
    bus_line_num = int(input())
    bus_line = []
    # 버스 노선을 리스트로 묶어 리스트에 넣어준다.
    for i in range(bus_line_num):
        A = list(map(int,input().split()))
        bus_line.append(A)

    # 정류장 갯수 입력
    station_num = int(input())

    # Test case 숫자 출력
    print(f'#{tc}',end='')
    # 정류장 갯수만큼 반복
    for _ in range(station_num):
        # 정류장 번호 입력
        station = int(input())
        # 지나간 노선 카운트 함수로 지나간 버스 가지수 도출
        print(f' {cnt_pass_bus(bus_line,station)}', end='')
    print()
