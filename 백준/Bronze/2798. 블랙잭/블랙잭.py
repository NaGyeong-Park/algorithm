import sys
from itertools import combinations

def combi():
    answer = 0
    for lst in numbers:
        if answer < sum(lst) <= M:
            answer = sum(lst)
    return answer


N, M = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = list(combinations(numbers,3))

print(combi())