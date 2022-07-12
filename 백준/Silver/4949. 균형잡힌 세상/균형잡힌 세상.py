import sys
lst = []

while True:
    temp = sys.stdin.readline().rstrip()
    if temp == ".":
        break
    temp.replace(" ","")
    check = []
    end = 0
    for i in temp:
        if end:
            break
        elif i == "(" or i == "[":
            check.append(i)
        elif i == ")":
            if not check or check[-1] != "(":
                print("no")
                end = 1
                break
            elif check[-1] == "(":
                check.pop()
        elif i == "]":
            if not check or check[-1] != "[":
                print("no")
                end = 1
                break
            elif check[-1] == "[":
                check.pop()
    if not check and not end:
        print("yes")
    elif not end:
        print("no")