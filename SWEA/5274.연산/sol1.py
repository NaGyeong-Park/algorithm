import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

def ope():
    while result:
        number, cnt = result.popleft()
        if number == M:
            return cnt
        for i in range(4):
            if i == 0:
                if 0<number+1<1000001 and not visited[number+1]:
                    result.append((number+1,cnt+1))
                    visited[number+1] = True
            elif i == 1:
                if 0<number*2<1000001 and not visited[number*2]:
                    result.append((number*2,cnt+1))
                    visited[number*2] = True
            elif i == 2:
                if 0<number-1<1000001 and not visited[number-1]:
                    result.append((number-1, cnt + 1))
                    visited[number-1] = True
            else:
                if 0<number-10<1000001 and not visited[number-10]:
                    result.append((number-10, cnt + 1))
                    visited[number-10] = True
    return 0

for tc in range(1, T + 1):
    print(f'#{tc} ',end='')
    N, M = map(int, input().split())
    result = deque()
    result.append((N,0))
    visited = [False]*1000001
    print(ope())