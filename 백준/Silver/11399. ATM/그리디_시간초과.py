# 시간초과
def back_tracking(idx):
    global result
    n_sum = 0
    if idx == N:
        for i in range(N):
            n_sum += sum(arr[:i + 1])
        if result > n_sum:
            result = n_sum
        return
    for i in range(N):
        if not visited[i]:
            arr.append(time_lst[i])
            visited[i] = True
            back_tracking(idx + 1)
            arr.pop()
            visited[i] = False
    return


N = int(input())
visited = [False for _ in range(N)]
time_lst = list(map(int, input().split()))
result = 10000000000000
arr = []
back_tracking(0)
print(result)
