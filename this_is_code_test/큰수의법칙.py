from random import randint
import time

N, M, K = map(int, input().split())
data = []
data.map(int, input().split())
# for _ in range(10000):
#     data.append(randint(1,100))
# s1 = time.time()
data.sort(reverse=True)
# length = len(data)
# a = data[length -1]
# b = data[length -2]
# e1 = time.time()
# print(e1-s1)
result = 0
count = 0
max_count = 0
while True:
    if count == M:
        break
    if max_count == K:
        result += data[1]
        max_count = 0
    else:
        result += data[0]
        max_count += 1
    count += 1

print(result)Ô