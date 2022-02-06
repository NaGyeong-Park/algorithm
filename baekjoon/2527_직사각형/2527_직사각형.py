square_lst = []
for i in range(4):
    square_lst.append(list(map(int, input().split())))

for square in square_lst:
    square1_lst = square[0:4]
    square2_lst = square[4:]

    square1_set_set = set(square1_lst)
    square2_set_set = set(square2_lst)
    square1_line_set = set()

    for i in range(square1_lst[0],square1_lst[2]+1):
        for j in range(square1_lst[1], square1_lst[3]+1):
            square1_set_set.add((i,j))

    for i in range(square2_lst[0],square2_lst[2]+1):
        for j in range(square2_lst[1], square2_lst[3]+1):
            square2_set_set.add((i,j))

    for k in range(square1_lst[0],square1_lst[2]+1):
        square1_line_set.add((k,square1_lst[1]))
        square1_line_set.add((k,square1_lst[3]))

    for j in range(square1_lst[1], square1_lst[3]+1):
        square1_line_set.add((square1_lst[0],j))
        square1_line_set.add((square1_lst[2],j))

    num = 0

    for elem in square2_set_set:
        if elem in (square1_set_set - square1_line_set) :
            num += 1 

    if len(square1_set_set & square2_set_set) == 1 :
        print('c')
    elif len(square1_set_set & square2_set_set) > 1 :
        if num == 0 :
            print('b')
        else :
            print('a')
    elif len(square1_set_set & square2_set_set) == 0 :
        print('d')