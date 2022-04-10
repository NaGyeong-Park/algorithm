import sys

input = sys.stdin.readline

def dfs(r, c, idx, total):
    global max_total
    if max_total >= total + max_val * (3 - idx):
        return
    if idx == 3:
        max_total = max(max_total, total)
        return
    else:
        for i in range(4):
            nr = r + di[i]
            nc = c + dj[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if idx == 1:
                    visited[nr][nc] = 1
                    dfs(r, c, 2, total+matrix[nr][nc])
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + matrix[nr][nc])
                visited[nr][nc] = 0

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0 ,-1]

max_total = 0
max_val = max(map(max, matrix))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0 ,matrix[i][j])
        visited[i][j] = 0

print(max_total)