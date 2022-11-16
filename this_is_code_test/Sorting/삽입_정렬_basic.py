data = [7,5,9,0,3,1,6,2,4,8]

data_length = len(data)
for i in range(1, data_length):
    min_index = i
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break

print(data)