H = int(input())
cnt = 0
for i in range(H+1):
    if '3' in str(i):
            cnt += 60*60
    else: 
        for j in range(60):
            if '3' in str(j):
                cnt += 60
            else :
                for k in range(60):
                    if '3' in str(k):
                        cnt+=1
print(cnt)