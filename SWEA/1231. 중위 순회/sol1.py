import sys

sys.stdin = open('input.txt')

def in_order(v):
    if v <= N:
        in_order(v*2)
        print(tree[v], end='')
        in_order(v*2+1)

for tc in range(1, 11):

    N = int(input())
    tree = [[0] for _ in range(N+1)]
    for i in range(1,N+1):
        info = input().split()
        tree[int((info[0]))]= info[1]

    print(f'#{tc}', end = ' ')
    in_order(1)
    print()

