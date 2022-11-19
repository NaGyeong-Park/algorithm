data = [5,7,9,0,3,1,6,2,4,8]
data_length = len(data)

def quick(data, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot],data[right]
        else:
            data[left], data[right] = data[right],data[left]
    quick(data, start, right-1)
    quick(data, right+1, end)

quick(data, 0, data_length-1)
print(data)