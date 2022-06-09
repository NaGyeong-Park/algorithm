X = int(input())

# arr = [0] * 1000001
#
# for i in range(2, X+1):
#     arr[i] = arr[i-1] + 1
#     if i%2 == 0:
#         arr[i] = min(arr[i], arr[i//2]+1)
#     if i%3 == 0:
#         arr[i] = min(arr[i], arr[i//3]+1)
#     if i%5 == 0:
#         arr[i] = min(arr[i], arr[i//5]+1)
#
# print(arr[X])

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
