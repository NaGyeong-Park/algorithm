N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

print(*sorted(data))