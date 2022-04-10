import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs(idx, sum, leftoper):
    print(f'idx{idx} sum{sum} left{leftoper}')
    global mi, ma

    if idx == n:
        if sum < mi:
            mi = sum
        if sum > ma:
            ma = sum
        return

    if leftoper[0] != 0:
        leftoper[0] -= 1
        dfs(idx + 1, sum + num[idx], leftoper)
        leftoper[0] += 1

    if leftoper[1] != 0:
        leftoper[1] -= 1
        dfs(idx + 1, sum - num[idx], leftoper)
        leftoper[1] += 1

    if leftoper[2] != 0:
        leftoper[2] -= 1
        dfs(idx + 1, sum * num[idx], leftoper)
        leftoper[2] += 1

    if leftoper[3] != 0:
        leftoper[3] -= 1
        if sum >= 0:
            dfs(idx + 1, sum // num[idx], leftoper)
        else:
            dfs(idx + 1, -(-sum // num[idx]), leftoper)
        leftoper[3] += 1




for tc in range(1, T + 1):

    n = int(input())
    num = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    mi = 1000000000
    ma = -1000000000

    dfs(1, num[0], oper[:])

    print(ma, mi)

