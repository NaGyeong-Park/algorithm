from itertools import combinations



def BFS():
    for b in blank:
        global result
        temp = 0
        copy_check = [check[i][:] for i in range(N)]
        copy_check[b[0][0]][b[0][1]] = False
        copy_check[b[1][0]][b[1][1]] = False
        copy_check[b[2][0]][b[2][1]] = False
        q = virus[:]
        while q:
            nx, ny = q.pop(0)
            for d in range(4):
                x = dx[d] + nx
                y = dy[d] + ny
                if 0 <= x < N and 0 <= y < M and copy_check[x][y] == True:
                    q.append([x, y])
                    copy_check[x][y] = False
        for i in range(N):
            temp += copy_check[i].count(True)
        if temp > result:
            result = temp


N, M = map(int, input().split())
virus = []
blank = []
result = 0
check = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    check.append(list(map(int, input().split())))
    for j in range(M):
        if check[i][j] == 2:
            virus.append([i, j])
            check[i][j] = False
        elif check[i][j] == 1:
            check[i][j] = False
        else:
            check[i][j] = True
            blank.append([i, j])

blank = list(combinations(blank, 3))
BFS()
print(result)