from collections import deque
from copy import deepcopy


def turn(n, d, m):
    if n + m < 0 or n + m > 3:
        return
    if m == -1:
        if COG[n + m][2] == COG[n][6]:
            return
    else:
        if COG[n][2] == COG[n + m][6]:
            return
    if d == 1:
        copy_cog[n + m].rotate(1)
    elif d == -1:
        copy_cog[n + m].rotate(-1)
    turn(n + m, -d, m)


COG = [deque(map(int, input())) for _ in range(4)]
K = int(input())
for i in range(K):
    check = 0
    copy_cog = deepcopy(COG)
    N, D = map(int, input().split())
    turn(N - 1, -D, -1)
    turn(N - 1, -D, 1)
    COG = copy_cog
    # if check == 1 or N == 1 or N == 4:
    if D == -1:
        COG[N - 1].rotate(-1)
    else:
        COG[N - 1].rotate(1)

result = 0
for i in range(4):
    if COG[i][0] == 1:
        result += 2 ** i
print(result)