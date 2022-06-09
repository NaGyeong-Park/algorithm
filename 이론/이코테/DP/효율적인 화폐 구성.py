N, M = map(int, input().split())
# lst = [0]*N
# for i in range(N):
#     lst[i] = int(input())
#
# arr = [-1]*(M+1)
# arr[0] = 0
# for i in range(1,M+1):
#     if i in lst:
#         arr[i] = 1
#     else:
#         temp = []
#         for j in lst:
#             if i-j >= 0 and arr[i-j] != -1:
#                 temp.append(arr[i-j])
#         if temp:
#             arr[i] = min(temp) + 1
# print(arr[-1])

# 모범 코드
array = []
for i in range(N):
    array.append(int(input()))

d = [10001] * (M+1)
d[0] = 0
for i in range(N):
    for j in range(array[i], M+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)
if d[M] == 10001:
    print(-1)
else:
    print(d[m])