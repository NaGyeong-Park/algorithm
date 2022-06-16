import sys

N = int(sys.stdin.readline())
stack = []
check = [False] * N
result = []
for i in range(N):
    num = int(sys.stdin.readline()) - 1
    if not stack or stack[-1] < num:
        for j in range(num + 1):
            if not check[j]:
                stack.append(j)
                check[j] = True
                result.append('+')
        stack.pop()
        result.append('-')
    elif num == stack[-1]:
        stack.pop()
        result.append('-')
if stack or check.count(False):
    print("NO")
else:
    print('\n'.join(result))