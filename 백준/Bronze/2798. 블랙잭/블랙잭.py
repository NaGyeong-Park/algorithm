import sys

def back(k):
    global answer
    if len(temp) == 3:
        result = sum(temp)
        if M >= result > answer:
            answer = result
        return
    elif sum(temp) > M:
        return
    for i in range(k,N):
        if visited[i]:
            continue
        temp.append(numbers[i])
        visited[i] = True
        back(i+1)
        visited[i] = False
        temp.pop()


N, M = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
visited = [False for _ in range(N)]
answer = 0
temp = []
result = 0
back(0)
print(answer)