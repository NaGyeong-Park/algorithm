N, M = map(int, input().split())
data = []
result = 0
# min
# for _ in range(N):
#     now_max_num = min(list(map(int, input().split())))
#     if result < now_max_num: result = now_max_num
# print(result)

for i in range(N):
    data.append(list(map(int, input().split())))
    now_min_num = 100001
    for j in range(M):
        if data[i][j] < now_min_num:
            now_min_num = data[i][j]
    if result < now_min_num: result = now_min_num
print(result)