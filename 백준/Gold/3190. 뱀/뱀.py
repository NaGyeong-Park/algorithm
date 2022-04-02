from collections import deque

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
change_sec = [0] * L
change_d = [0] * L
for i in range(L):
    a, b = map(str, input().split())
    change_sec[i] = int(a)
    change_d[i] = b
Q = deque()
Q.append([1, 1])
d = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
sec = 0
change_idx = 0
while Q:
    x, y = Q[-1]
    nxt = [x + dx[d], y + dy[d]]
    if 1 > nxt[0] or 1 > nxt[1] or nxt[0] > N or nxt[1] > N or nxt in Q:
        break
    elif nxt in apple:
        Q.append(nxt)
        apple.remove(nxt)
    else:
        Q.append(nxt)
        Q.popleft()
    sec += 1
    if sec in change_sec:
        if change_d[change_idx] == 'D':
            d = (d + 1) % 4
        else:
            d = (4 + d - 1) % 4
        change_idx += 1
print(sec + 1)