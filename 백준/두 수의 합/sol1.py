import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    print(f'#{tc} ')
    N = int(sys.stdin.readline())
    NUM = sorted(list(map(int, sys.stdin.readline().split())))
    X = int(sys.stdin.readline())

    result = 0
    l, r = 0, N - 1
    summary = 0
    while l < r:
        summary = NUM[l] + NUM[r]
        if summary == X:
            result += 1
            l += 1
        elif summary < X:
            l += 1
        else:
            r -= 1
    print(result)