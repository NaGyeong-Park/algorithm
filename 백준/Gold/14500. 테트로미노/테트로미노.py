N, M = map(int, input().split())
num_map = [list(map(int, input().split())) for _ in range(N)]
squa_x = [1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -2, -1, -2, 1, 2, 1, 2, -1, 1, -1, 1]
squa_y = [0, 1, 0, 1, 0, 1, 1, 2, 0, -1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
tri_x = [1, 1, 1, -1, -1, -1, 0, 0]
tri_y = [0, 1, 2, 0, 2, 1, -1, 3]
result = 0
for i in range(N):
    for j in range(M):
        if j < M - 1:
            sum_2 = sum(num_map[i][j:j + 2])
            for d in range(0, 22, 2):
                x1 = i + squa_x[d]
                x2 = i + squa_x[d + 1]
                y1 = j + squa_y[d]
                y2 = j + squa_y[d + 1]
                if 0 <= x1 < N and 0 <= y1 < M and 0 <= x2 < N and 0 <= y2 < M:
                    sum_squa = sum_2 + num_map[x1][y1] + num_map[x2][y2]
                    if result < sum_squa:
                        result = sum_squa
            if j != M - 2:
                sum_2 += num_map[i][j + 2]
                for d in range(7):
                    x = i + tri_x[d]
                    y = j + tri_y[d]
                    if 0 <= x < N and 0 <= y < M:
                        sum_squa = sum_2 + num_map[x][y]
                        if result <= sum_squa:
                            result = sum_squa
        if i <= N - 4:
            sum_squa = 0
            for d in range(4):
                sum_squa += num_map[i + d][j]
                if result <= sum_squa:
                    result = sum_squa
print(result)