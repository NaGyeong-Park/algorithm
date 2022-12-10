N = int(input())
data = []
for _ in range(N):
    name, num = input().split()
    data.append((int(num), name))

data = sorted(data, key=lambda student: student[0])

for name in data:
    print(name[1], end=' ')