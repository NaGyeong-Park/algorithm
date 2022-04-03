# 수열갯수, 수열 목록을 받는다
input_num = int(input())
in_lst = list(map(int, input().split()))

# 큰, 작은, 비교해줄 변수를 지정해준다.(초기값 1)
num_len = 1
num_big = 1
num_small = 1

# 수열갯수가 0이거나 1이면 순서대로 0, 1 출력
if input_num == 0 :
    print(0)
elif input_num == 1 :
    print(1)
# 왼쪽부터 오른쪽으로 커지는것/작아지는 것으로 케이스를 나눈다
else :
    # 커지는 수열
    for i in range(0, input_num-1):
        # i와 뒤에 인덱스 값을 비교해서 뒤 값이 더 크면 num_big에 1 추가
        if in_lst[i] <= in_lst[i+1]:
            num_big += 1
            # 만약 인덱스 i값이 끝에서 두번째고 num_len이 num_big보다 작다면
            # num_big 값을 num_len 값에 저장하고 num_big을 초기화해준다.
            if i == (input_num-2) and num_len < num_big :
                num_len = num_big
                num_big = 1
        # 인덱스 값 i, i+1를 비교했을때 i > i+1일 때
        # num_len < num_big의 경우 num_len값을 num_big값으로 바꿔주고
        else :
            if num_len < num_big :
                num_len = num_big
            # num_big을 초기화하고 다시 for문을 돈다
            num_big = 1
    
    # 작아지는 수열, 로직은 위와 동일
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
    
    # num_len의 값을 출력
    print(num_len)