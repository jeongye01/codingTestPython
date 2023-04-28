#  [S/W 문제해결 기본] 1일차 - Flatten
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 5분 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    array=list(map(int,input().split()))
    for i in range(n):
      maxIdx=array.index(max(array))
      minIdx=array.index(min(array))
      array[maxIdx]-=1
      array[minIdx]+=1
    ans=max(array)-min(array)
    print("#{} {}".format(test_case,ans))
  