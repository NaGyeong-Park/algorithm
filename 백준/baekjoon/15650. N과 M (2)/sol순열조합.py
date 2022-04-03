import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = list(range(1,N+1))
    result = list(combinations(N_lst,M))
    for i in result:
        print(*i)