data = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(data)+1)

for num in data:
    count[num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")