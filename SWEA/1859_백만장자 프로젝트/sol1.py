import sys

sys.stdin = open('input.txt')

T = int(input())

def i_wanna_rich(market):
    present_idx = 0
    buy = 0
    sum = 0
    i = 1
    while True:
        if i == len(market):
            return sum
        else:
            if market[present_idx] < market[i]:
                sum += - buy
                buy = 0
                present_idx = i
            else:
                buy += market[i]
                sum += market[present_idx]
        i += 1

for tc in range(1, T + 1):

    days = int(input())
    market_info = list(map(int, input().split()))
    market_info = market_info[::-1]
    market_info.append(1000001)

    result = i_wanna_rich(market_info)

    print(f'#{tc} {result}')

