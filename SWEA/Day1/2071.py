#평균값 구하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
 
    array=list(map(int,input().split()))
    ans=0
    for i in range(10):
      ans+=array[i]
    ans=round(ans/10)

    print("#{} {}".format(test_case,ans))
    # ///////////////////////////////////////////////////////////////////////////////////
   