import sys

sys.stdin = open('input.txt')

T = int(input())

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def num_sum(x,nsum):
    if parents[x] == x:
        return nsum+popu[x-1]
    parents[x] = num_sum(parents[x],nsum+popu[x-1])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x

for tc in range(1, T + 1):
    print(f'#{tc} ',end='')
    N = int(input())
    popu = list(map(int, input().split()))
    parents = {i: i for i in range(1, N + 1)}
    lst = []
    for i in range(N):
        a = list(map(int, input().split()))
        s = a.pop(0)
        for j in range(s):
            lst.append(i+1)
            lst.append(a[j])
    for i in range(len(lst)//2):
        a, b = lst[i * 2], lst[i * 2 + 1]
        if find(a) != find(b):
            union(a, b)
    group = set()

    for i in range(1, N + 1):
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(len(group))