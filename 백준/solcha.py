import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    
    print(f'#{tc} ')
    N = int(input())
    population = list(map(int, input().split()))
    nation = [0]*(N+1)
    for i in range(N):
        temp = list(map(int, input().split()))
        n = temp.pop(0)
        for j in range(n):
