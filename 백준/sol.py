import sys

sys.stdin = open('input.txt')

T = int(input())

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    print(f'uni fin {x} {y}')
    if x > y:
        x, y = y, x
    parents[y] = x

for tc in range(1, T + 1):
    print(f'#{tc} ',end='')
    N = int(input())
    ppu = list(map(int, input().split()))
    parents = [i for i in range(N+1)]
    for i in range(1,N+1):
        lst = list(map(int, input().split()))
        a = lst.pop(0)
        for j in range(a):
            print(f'i{i}j{lst[j]}')
            print(find(i))
            print(find(lst[j]))
            if find(i) != find(lst[j]):
                union(i, lst[j])
            print('change')
            print(find(i))
            print(find(lst[j]))
    group = set()
    print(parents)

    for i in range(1, N + 1):
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)