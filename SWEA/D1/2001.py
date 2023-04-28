#파리 퇴치

#내 풀이->테스트 통과 DATE=>4.28 풀이시간 8분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    ans=-1e9
    board=[]
    for _ in range(n):
        board.append(list(map(int,input().split())))
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp=0
            for a in range(m):
                for b in range(m):
                    tmp+=board[i+a][j+b]
            ans=max(ans,tmp)


    
    print("#{} {}".format(test_case,ans))