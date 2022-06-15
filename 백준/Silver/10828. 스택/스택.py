import sys

N = int(sys.stdin.readline())
stack = list()
for i in range(N):
    temp = sys.stdin.readline().strip()
    if temp == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif temp == "size":
        print(len(stack))
    elif temp == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif temp == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(temp[5:]))