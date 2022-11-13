data = [7,5,9,0,3,1,6,2,4,8]
data_length = len(data)

for i in range(0, data_length):
    min_index = i
    for j in range(i, data_length):
        if data[j] < data[min_index]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]

print(data)