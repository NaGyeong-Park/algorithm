import sys
from itertools import permutations

sys.stdin = open('input.txt')

T = int(input())


def calculation():
    cnt = 0
    global max_ans, min_ans
    for per in permu:
        cnt += 1
        nsum = lst[0]
        for o in range(1,N):
            if per[o-1] == 1:
                nsum += lst[o]
            elif per[o-1] == 2:
                nsum -= lst[o]
            elif per[o-1] == 3:
                nsum *= lst[o]
            else:
                if nsum < 0 :
                    nsum = -nsum // lst[o]
                    nsum = -nsum
                else:
                    nsum = nsum//lst[o]
        if max_ans < nsum:
            max_ans = nsum
        if min_ans > nsum:
            min_ans = nsum

for tc in range(1, T + 1):
    max_ans = -1000000000
    min_ans = 1000000000
    print(f'#{tc} ',end='')
    N = int(input())
    lst = list(map(int, input().split()))
    a = list(map(int, input().split()))
    oper = []
    o = 1
    for i in a:
        for j in range(i):
            oper.append(o)
        o += 1
    print(oper)
    calcul = set()
    permu = set(permutations(oper, N-1))
    calculation()
    print(permu)
    print(max_ans)
    print(min_ans)