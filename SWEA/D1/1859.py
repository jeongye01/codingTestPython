#백만 장자 프로젝트
#내 풀이->테스트 통과 DATE=>1248 풀이시간 40분 
n=int(input())
array=list(map(int,input().split()))
array.reverse()
ans=0
for i in range(1,n):
    if array[i-1]>array[i]:
        ans+=(array[i-1]-array[i])
        array[i]=array[i-1]
      
print("#{} {}".format(test_case,ans))