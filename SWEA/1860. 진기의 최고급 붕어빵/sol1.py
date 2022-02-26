import sys

sys.stdin = open('input.txt')

T = int(input())

def intime_boongA(lst,N,M,K):
    cheak_sec = M+1
    boogA = K
    for i in range(len(lst)):
        if lst[i] < cheak_sec:
            return 'Impossible'
        if boogA < 0:
            return 'Impossible'

        if lst[i] >= cheak_sec+M:
            cheak_sec += M
            boogA = K

        if cheak_sec <= lst[i] < cheak_sec+M:
            boogA -= 1




for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    visit_sec = list(map(int, input().split()))
    visit_sec.sort()
    print(visit_sec)
    result = intime_boongA(visit_sec,N,M,K)
    print(f'#{tc} ')

