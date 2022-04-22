import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    
    print(f'#{tc} ')

    N, S = map(int, sys.stdin.readline().split())
    NUM = list(map(int, sys.stdin.readline().split()))
    start = 0
    end = 1
    temp = 0
    summary = 0
    result = 10001

    for start in range(N):
        print(f'start {start} end {end}')
        print(f'summ {summary}')
        while summary < S and end < N:
            summary += NUM[end]
            end +=1

        temp = end - start + 1
        print(temp)
        if summary >= S and temp < result:
            result = temp
            print(f'result change {result}')
        summary -= NUM[start]
    # while start < N:
    #     print(f'start {start} end {end}')
    #     print(f'summ {summary}')
    #     while summary < S and end < N:
    #         summary += NUM[end]
    #         end +=1
    #     temp = end - start + 1
    #     if temp < result:
    #         result = temp
    #     summary -= NUM[start]
    #     start += 1
    print(result)