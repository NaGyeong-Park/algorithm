X = int(input())

def find_num(n, lst):
    if n==1:
        return 0
    elif lst[n] != -1:
        return lst[n]
    else:
        if n%6 == 0:
            lst[n] = min(find_num(n//3,lst), find_num(n//2,lst)) + 1
        elif n % 3 == 0:
            lst[n] = min(find_num(n // 3, lst), find_num(n-1,lst)) + 1
        elif n % 2 == 0:
            lst[n] = min(find_num(n // 2, lst), find_num(n-1,lst)) + 1
        else:
            lst[n] = find_num(n-1, lst) + 1
        return lst[n]


lst = [-1] * 1000001
lst[0] = lst[1] = 0
print(find_num(X,lst))