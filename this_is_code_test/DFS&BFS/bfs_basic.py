from collections import deque

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited_list = [False for _ in range(9)]
queue = deque([1])
visited_list[1] = True
while True:
    if len(queue) == 0:
        break
    now = queue.popleft()
    print(now, end=" ")
    for next_node in graph[now]:
        if visited_list[next_node] == False:
            queue.append(next_node)
            visited_list[next_node] = True