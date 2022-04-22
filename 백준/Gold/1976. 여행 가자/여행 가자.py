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
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    parent = [i for i in range(M+1)]
    for i in range(1,N+1):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(len(temp)):
            if temp[j] == 1:
                union(i,j+1)
    travel = list(map(int, sys.stdin.readline().split()))
    c = 0
    for i in range(M-1):
        if find(travel[i]) != find(travel[i+1]):
            print('NO')
            c = 1
            break
    if c == 0:
        print('YES')