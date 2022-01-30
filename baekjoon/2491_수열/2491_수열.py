input_num = int(input())
in_lst = list(map(int, input().split()))

num_len = 1
num_big = 1
num_small = 1

if input_num == 0 :
    print(0)
elif input_num == 1 :
    print(1)
else :
    for i in range(0, input_num-1):
        if in_lst[i] <= in_lst[i+1]:
            num_big += 1
            if i == (input_num-2) and num_len < num_big :
                num_len = num_big
                num_big = 1
        else :
            if num_len < num_big :
                num_len = num_big
            num_big = 1
    
    for i in range(0, input_num-1):
        if in_lst[i] >= in_lst[i+1]:
            num_small += 1
            if i == input_num-2 and num_len < num_small  :
                num_len = num_small
                num_small = 1
        else :
            if num_len < num_small :
                num_len = num_small
            num_small = 1
    print(num_len)