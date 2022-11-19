data = [5,7,9,0,3,1,6,2,4,8]
data_length = len(data)

def quick(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    tail = data[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    print(data, left_side, right_side)
    
    return quick(left_side) + [pivot] + quick(right_side)

result = quick(data)
print(result)