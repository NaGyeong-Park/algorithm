# 난쟁이 키 입력
dwarf_lst = []
for i in range(9):
    dwarf_lst.append(int(input()))

#난쟁이 찾는 함수, 난쟁이 키 리스트 입력
def find_real_dwarf(find_dwarf_lst):
    sum = 0
    # 모든 난쟁이의 키를 더해준다.
    for i in find_dwarf_lst:
        sum += i

    # 난쟁이 두명의 키를 빼준다
    for i in range(len(find_dwarf_lst)-1):
        sum -= find_dwarf_lst[i]
        for j in range(1,len(find_dwarf_lst)):
            sum -= find_dwarf_lst[j]
            
            # 두명의 키를 빼준 값이 100이면 그 키 2개를 난쟁이 키 리스트에서 없애기
            if sum == 100 :
                find_dwarf_lst.pop(i)
                find_dwarf_lst.pop(j-1)
                return find_dwarf_lst
            
            # 100이 아니라면 다시 난쟁이 키 합에 더해주기
            else :
                sum += find_dwarf_lst[j]    
                
        # 100이 아니라면 다시 난쟁이 키 합에 더해주기
        sum += find_dwarf_lst[i]


find_real_dwarf(dwarf_lst)
# 난쟁이 리스트 정렬
dwarf_lst.sort()

# 진짜 난쟁이 키들 출력
for elem in dwarf_lst:
    print(elem)