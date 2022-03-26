import sys

sys.stdin = open('input.txt')

T = int(input())


def BFS():
    # 시작 위치 : S
    queue = [S]
    # queue가 있을 때까지 반복
    while queue:
        a = queue[0]
        queue = queue[1:]
        # a와 연결된 위치들 중 방문 안한 곳이 있다면 a요소에 1을 더함(움직인 횟수)
        for i in lst[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[a]+1
    # 도착 위치 움직인 횟수 반환
    return visited[G]

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    # 노드에 방문했는지 리스트 만들어줌
    visited = [0]*(V+1)
    for i in range(E):
        a, b = map(int,input().split())
        lst[a].append(b)
        lst[b].append(a)
    # set을 이용해 중복을 없애주고, 리스트 정렬
    for i in range(V+1):
        lst[i] = list(set(lst[i]))
        lst[i].sort()
    S,G = map(int,input().split())
    print(f'#{tc}', end=' ')
    print(BFS())

