#중간값 찾기
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 2분 
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    array=list(map(int,input().split()))
    array.sort()
    ans=array[len(array)//2]

    print(ans)