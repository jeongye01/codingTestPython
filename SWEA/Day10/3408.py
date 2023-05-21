#세가지 합 구하기
##내 풀이->테스트 통과 DATE=>5.21 풀이시간 5분 
T=int(input())
result=[]
for tc in range(1,T+1):
    n=int(input())
    s1=n*(n+1)//2
    s2=n*n
    s3=n*n+n
    print(f"#{tc} {s1} {s2} {s3}")