from random import randint
import time

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
length = len(data)
result = (M%(K+1))*(data[length-1]*K+data[length-2])
result += (M//(K+1))*data[length-1]
print(result)


# sort vs len 실험
# for _ in range(10000):
#     data.append(randint(1,100))
# s1 = time.time()
# data.sort(reverse=True)
# length = len(data)
# a = data[length -1]
# b = data[length -2]
# e1 = time.time()
# print(e1-s1)


# result = 0
# count = 0
# max_count = 0
# while True:
#     if count == M:
#         break
#     if max_count == K:
#         result += data[1]
#         max_count = 0
#     else:
#         result += data[0]
#         max_count += 1
#     count += 1

# print(result)