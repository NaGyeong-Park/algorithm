import sys
sys.stdin = open('input.txt')

T = int(input())

def greedy():
    result = 0
    # 컨테이너 무게가 화물 최대 적재무게와 같거나 작다면
    # 결과값에 컨테이너 무게를 더해주고, 컨테이너와 화물 무게를 0으로(없는셈) 만들기
    for i in range(N):
        for j in range(M):
            if t[j] >= w[i]:
                result += w[i]
                w[i] = 0
                t[j] = 0
                break
    return result

for tc in range(1, T + 1):
    
    print(f'#{tc} ',end='')
    N, M = map(int, input().split())
    w = list(map(int,input().split()))
    t = list(map(int,input().split()))
    # 내림차순으로 정렬!
    w.sort(reverse=True)
    t.sort(reverse=True)
    print(greedy())