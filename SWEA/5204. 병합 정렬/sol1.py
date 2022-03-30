import sys

sys.stdin = open('input.txt')

T = int(input())



def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    merge_arr = []
    l = r = 0
    if left_arr[len(left_arr) - 1] > right_arr[len(right_arr) - 1]:
        cnt += 1
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            merge_arr.append(left_arr[l])
            l += 1
        else:
            merge_arr.append(right_arr[r])
            r += 1
    merge_arr += left_arr[l:] + right_arr[r:]
    return merge_arr

for tc in range(1, T + 1):
    print(f'#{tc} ', end='')
    N = int(input())
    cnt = 0
    num_lst = list(map(int, input().split()))
    print(merge_sort(num_lst)[N//2],cnt)