N = int(input())
result = 0
time_lst = sorted(list(map(int,input().split())))
for i in range(1,N+1):
    result += sum(time_lst[:i])
print(result)
