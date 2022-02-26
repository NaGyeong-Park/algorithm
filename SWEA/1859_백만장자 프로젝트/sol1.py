import sys

sys.stdin = open('input.txt')

T = int(input())


# 처음풀때 : 잘 풀렸는데...? 메모리 초과
# 현열님 풀이를 참고한 결과...쓸모없는 변수를 2개나 선언해서 사용했기 때문...; 7000kb를 차지하고 있었다
# 로직 : 뒤에서부터 큰 숫자를 찾고 그거보다 큰 수가 나타나기 전까지 사고 큰 숫자로 팔기

# 수익 계산 함수
def i_wanna_rich(market):
    # 현재 max값 idx값 변수, 산 가격 변수, 총계, 인덱스 변수
    present_idx = 0
    buy = 0
    sum = 0
    i = 1
    # for문같이 while 활용
    while True:
        # 인덱스가 끝 값이면 끝내기
        if i == len(market):
            return sum
        else:
            # 만약 현재 max값보다 i인덱스 값이 크다면
            if market[present_idx] < market[i]:
                # 총계 값에서 산 돈을 빼주고 산 돈변수 초기화
                sum += - buy
                buy = 0
                # 현재 max 인덱스값을 i로 바꾸기
                present_idx = i
            # 아니라면 산 값에 현재 인덱스값 더해주기 / 총계 sum에 현재 max값 더해주기
            else:
                buy += market[i]
                sum += market[present_idx]
        i += 1


for tc in range(1, T + 1):

    # 판매날들 입력 / 가격정보 리스트로 받기
    days = int(input())
    market_info = list(map(int, input().split()))
    # 뒤에서부터 살펴보기 위해서 리스트 슬라이싱
    market_info = market_info[::-1]
    # 함수에서 마지막 인덱스 값이 현재 max값보다 작을 경우에 else문으로 가기때문에 buy값을 빼주지않고 끝남  
    # 이를 방지하기위해 큰 값을 마지막에 넣어줌
    market_info.append(1000001)

    # 함수 대입해 총계 값 구하기
    result = i_wanna_rich(market_info)
    # 출력
    print(f'#{tc} {result}')

