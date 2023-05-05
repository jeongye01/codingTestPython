# [S/W 문제해결 기본] 8일차 - 암호문3
#내풀이 아님

test_case=0
while test_case<10:
    test_case+=1
    N = int(input())
    li=list(map(int,input().split()))
    M = int(input())
    c = input().split()
    c_li = []
    tmp=[]
    tmp.append(c[0])
 
    for i in range(1,len(c)):
        if c[i] not in ['I','D','A']:tmp.append(int(c[i]))
        else:
            c_li.append(list(tmp))
            tmp=[]
            tmp.append(c[i])
    c_li.append(list(tmp))
 
    for i in range(M):
        command = c_li[i]
        if command[0]=='I':
            for num in reversed(command[3:]): li.insert(command[1],num)
        elif command[0]=='D':
            for _ in range(command[2]): del li[command[1]]
        else:
            for num in command[2:]: li.append(num)
    print('#'+str(test_case),end=' ')
    for j in range(10):
        print(li[j],end=' ')
    print()