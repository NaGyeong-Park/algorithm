import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

T = int(input())


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for tc in range(1, T + 1):

    print(f'#{tc} ',end='')
    N, M = map(int, sys.stdin.readline().split())
    parent = [i for i in range(N)]
    result = 0
    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        if find(A) == find(B) and not result:
            result = i+1
        union(A,B)
    print(result)