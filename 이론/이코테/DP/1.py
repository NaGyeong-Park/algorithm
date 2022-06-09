X = int(input())

arr = [0] * 1000000

arr[0] = 0
arr[1] = 0
arr[2] = 1
arr[3] = 1
lst = [2,3]

def find_num(n):
    for i in range(4, n+1):
        for j in lst:
            if i%j == 0:
                temp = i//j
                A = arr[temp] + 1
                if not arr[i] or A < arr[i]:
                    arr[i] = A
        temp = i-1
        A = arr[temp] + 1
        if not arr[i] or A < arr[i]:
            arr[i] = A

find_num(X)
print(arr[X])