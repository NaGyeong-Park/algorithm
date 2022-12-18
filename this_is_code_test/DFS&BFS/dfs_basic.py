graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
now = 1
visited_list = [False for _ in range(9)]
def DFS(graph, now, visited_list):
    visited_list[now] = True
    print(now, end=" ")
    for next in graph[now]:
        if visited_list[next] != True:
            DFS(graph, next, visited_list)
DFS(graph, now, visited_list)