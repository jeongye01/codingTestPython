# [S/W 문제해결 기본] 5일차 - Magnetic
# 내풀이 아님
for tc in range(1, 11):
    width = int(input())
 
    matrix = [list(map(int, input().split())) for _ in range(width)]
 
    deadlock_cnt = 0
 
    for i in range(width):
        flag = 0
        for j in range(width):
            if matrix[j][i] == 1:
                flag = 1
            elif matrix[j][i] == 2:
                if flag:
                    deadlock_cnt += 1
                    flag = 0
     
    print(f"#{tc} {deadlock_cnt}")