import sys
sys.setrecursionlimit(100000)

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if parent[x] > parent[y]:
        parent[x] = y
    else:
        parent[y] = x


N, M = map(int,sys.stdin.readline().split())
parent = [i for i in range(0, N + 1)]

for i in range(M):
    C, A, B = map(int,sys.stdin.readline().split())
    if C == 0:
        union(A, B)
    else:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')