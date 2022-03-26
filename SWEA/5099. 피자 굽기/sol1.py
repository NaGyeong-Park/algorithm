import sys
from copy import deepcopy
sys.stdin = open('input.txt')

T = int(input())

def BFS():
    # 남은 피자들인 queue, oven, 인덱스 번호 index 리스트를 만들어준다.
    # 인덱스를 추적해주기 위해 cnt 변수 할당
    queue = deepcopy(lst[N:])
    oven = deepcopy(lst[:N])
    index = list(range(1,N+1))
    cnt = 0
    # 모든 피자의 치즈가 녹을 때까지 반복
    while any(oven) != False:
        for i in range(N):
            oven[i] = oven[i]//2
            # 모든 피자의 치즈가 녹으면 마지막으로 녹은 피자의 번호 반환
            if any(oven) == False:
                print(index[i])
                break
            # 피자의 치즈가 다 녹고, 기다리는 피자가 있다면
            if oven[i] == 0 and queue:
                    # 몇 번째 피자인지 인덱스에 할당해주고
                    cnt += 1
                    index[i] = N + cnt
                    # 다 녹은 피자를 기다리는 피자로 바꿔주고
                    oven[i] = queue[0]
                    # 기다리는 피자 리스트에서 뺴준다
                    queue = queue[1:]



for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    BFS()
