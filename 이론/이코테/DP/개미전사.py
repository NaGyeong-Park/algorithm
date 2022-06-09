N = int(input())
Arr = list(map(int, input().split()))

d = [0]*100

d[0] = Arr[0]
d[1] = max(Arr[0], Arr[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+Arr[i])

print(d[N-1])