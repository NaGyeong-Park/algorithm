#스위치 갯수, 스위치 상태, 학생 수, 학생들의 성별과 가진 번호 입력
switch_num = int(input())
switch_lst = list(map(int, input().split()))
studen_num = int(input())
studen_lst = []
for i in range(studen_num):
    studen_lst.append(int(input()))
    

#배수 리스트 함수, 학생이 가진 번호와 스위치 갯수 입력
def multiple(num, swt_num):
    mul_lst = []
    #학생이 가진 번호의 배수가 스위치 배수보다 작거나 같다면 mul_lst에 저장
    for i in range(1,101):
        if num*i <= swt_num:
            mul_lst.append(num*i)
        else :
            return mul_lst

# 스위치 값 바꾸기 함수
def upsidedown(bin):
    if bin == 0 :
        return 1
    elif bin == 1 :
        return 0

# 여학생의 로직 구현
# 스위치 리스트, 학생이 가진 번호, 반환 할 빈 리스트
# num은 가지고있는 스위치 넘버에서 -1한 값(인덱스는 0번부터 시작하므로)
def girls_joke(lst, num, out_lst):
    # for문은 1부터 스위치 리스트 나누기 2의 올림 값까지 돈다
    for i in range(1,len(lst)//2+1):
        # IndexError가 날 경우 끝까지 확인한 것이므로 out_lst를 반환해줌
        #try : 
            # 음수값이면 out_lst 반환
            if num-i < 0 or num+i >len(lst) :
                return out_lst
            # 비교하는 두 리스트 요소가 다를 경우 out_lst 반환
            elif lst[num-i] != lst[num+i] :
                return out_lst
            # 조건 : 리스트 길이가 짝수
            # 리스트 첫번째와 끝번째 요소가 같다면 out_lst 반환
            elif num-i == 0 and num+i == len(lst)-1:
                out_lst += [num-i, num+i]
                return out_lst
            # 윗 경우들에 속하지 않는다면 out_lst에 인덱스 번호들 저장
            else : 
                out_lst += [num-i, num+i]
        #except IndexError :
        #    return out_lst

# 학생들의 수만큼 반복
for i in range(len(studen_lst)):

    # 학생의 첫번째 요소는 성별, 두번째는 주어진 번호로 지정
    sex = studen_lst[i][0]
    given_num = studen_lst[i][1]

    # 남학생
    if sex == 1 :
        # 남학생의 번호를 배수함수에 넣어줘 배수 리스트를 만든다.
        num_lst = multiple(given_num, switch_num)
        # 배수 번호 스위치들의 상태를 바꿔준다.
        for j in num_lst:
            switch_lst[j-1] = upsidedown(switch_lst[j-1])
    # 여학생
    else :
        turn_index_lst = []
        # 주어진 수가 첫번째 인덱스거나 끝번째라면 그 인덱스만 스위치 상태를 바꿔준다.
        if (given_num-1 == 0) or (given_num == len(switch_lst)) : 
            switch_lst[given_num-1] = upsidedown(switch_lst[given_num-1])

        else :
            # 여학생 함수에 스위치 리스트, 주어진 번호, 반환할 리스트를 넣어준다.
            girls_joke(switch_lst, given_num-1, turn_index_lst)
            # 주어진 번호를 반환된 리스트에 넣어준다.
            turn_index_lst.append(given_num-1)
            # 반환된 리스트에 저장된 번호의 스위치 상태를 바꾸어준다.
            for k in turn_index_lst:
                switch_lst[k] = upsidedown(switch_lst[k])

# 줄을 바꿔줄 번호를 리스트에 넣어준다.
cut_lst = [19, 39, 59, 79, 99]
# 스위치 상태 리스트의 요소들을 20개씩 출력
for index in range(len(switch_lst)):
    if index in cut_lst:
        print(switch_lst[index])
    else :
        print(switch_lst[index], end= ' ')