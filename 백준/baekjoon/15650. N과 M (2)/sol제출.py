def make_arr(k):
    if k == M:
        print(*arr)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)

            make_arr(k + 1)
            arr.pop()

            for j in range(i+1,N):
                visited[j] = False

N, M = map(int, input().split())
N_lst = list(range(1,N+1))

visited = [False for _ in range(N)]
arr = []

make_arr(0)