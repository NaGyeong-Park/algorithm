def BFS(graph):
    map = graph
    visited = [0]*N
    for i in range(N):
        visited[i] = [0]*M
    visited[0][0] = 1
    queue_x = [0]
    queue_y = [0]
    find_x = [1,-1,0,0]
    find_y = [0,0, -1, 1]
    while queue_x and queue_y:
        my_x = queue_x[0]
        my_y = queue_y[0]
        queue_x = queue_x[1:]
        queue_y = queue_y[1:]
        if my_x == N-1 and my_y == M-1:
            return visited[my_x][my_y]
        for i in range(4):
            my_x_dir = my_x + find_x[i]
            my_y_dir = my_y + find_y[i]
            if 0 > my_x_dir or my_x_dir >= N or 0 > my_y_dir or my_y_dir >= M:
                continue
            elif map[my_x_dir][my_y_dir] == 0:
                continue
            elif visited[my_x_dir][my_y_dir] == 0 and map[my_x_dir][my_y_dir] == 1:
                queue_x.append(my_x_dir)
                queue_y.append(my_y_dir)
                visited[my_x_dir][my_y_dir] = visited[my_x][my_y] + 1


N, M = map(int, input().split())
lst = [0]*N
for i in range(N):
    lst[i] = list(map(int, input()))
print(BFS(lst))