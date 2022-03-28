import sys

sys.stdin = open('input.txt')

T = int(input())


def make_arr(k):
    if k == M:
        print(*arr)
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)

            make_arr(k + 1)
            arr.pop()

            for j in range(i+1,N):
                visited[j] = False


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = list(range(1,N+1))

    visited = [False for _ in range(N)]
    arr = []

    make_arr(0)