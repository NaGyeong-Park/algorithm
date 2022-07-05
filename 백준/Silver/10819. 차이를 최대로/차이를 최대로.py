import sys
from itertools import permutations
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(permutations(arr))
result = 0
for i in arr:
    temp = 0
    for idx in range(N - 1):
        temp += abs(i[idx] - i[idx + 1])
    if temp > result:
        result = temp
print(result)