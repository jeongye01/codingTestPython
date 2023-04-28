#최빈수 구하기
#내 풀이->테스트 통과 DATE=>4.27 풀이시간 15분 
n=int(input())
array=list(map(int,input().split()))
points=[0]*101
for p in array:
    points[p]+=1
    
maximum=0 
for i in range(101):
    if(maximum<=points[i]):
        maximum=points[i]
        ans=i
    

print("#{} {}".format(test_case,ans))

