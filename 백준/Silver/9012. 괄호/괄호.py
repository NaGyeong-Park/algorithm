import sys

N = int(sys.stdin.readline())
for _ in range(N):
    temp = sys.stdin.readline()
    arr = []
    check = 0
    for i in range(len(temp)):
        if temp[i] == "(":
            arr.append(True)
        elif temp[i] == ")":
            if not arr:
                print("NO")
                check = 1
                break
            else:
                arr.pop()
    if arr:
        if not check:
            print("NO")
    elif not arr and not check:
        print("YES")