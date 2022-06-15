import sys
N = int(sys.stdin.readline())
stack = list()
for i in range(N):
    temp = list(sys.stdin.readline().strip().split())
    for text in temp:
        print(text[::-1], end=' ')
    print()