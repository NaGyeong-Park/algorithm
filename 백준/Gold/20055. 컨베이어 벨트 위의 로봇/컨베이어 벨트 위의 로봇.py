import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    
    print(f'#{tc} ', end='')

    N, K = map(int, input().split())
    CONVEYOR = deque(map(int, input().split()))
    robot = deque([False]*N)
    level = 0
    while CONVEYOR.count(0) < K:
        level += 1
        CONVEYOR.rotate(1)
        robot.rotate(1)
        if robot[-1] == True:
            robot[-1] = False
        for i in range(N-2,-1,-1):
            if robot[i] and not robot[i+1] and CONVEYOR[i+1]:
                robot[i], robot[i+1] = robot[i+1], robot[i]
                CONVEYOR[i+1] -= 1
                if i+1 == N-1:
                    robot[i+1] = False
        if CONVEYOR[0]:
            robot[0] = True
            CONVEYOR[0] -= 1
        if CONVEYOR.count(0) >= K:
            break
    print(level)
