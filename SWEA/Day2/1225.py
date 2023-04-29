
#[S/W 문제해결 기본] 7일차 - 암호생성기
#내 풀이->테스트 통과 DATE=>4.29 풀이시간 100분 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n=int(input())
    array=list(map(int,input().split()))

    for i in range(8):
        array[i]%=150
    isEnd=False
    while not isEnd:
        # 1사이클
        for i in range(1,6):
            v=array[0]-i if array[0]-i>0 else 0
            array=array[1:]+[v]
            if(v==0):
                isEnd=True
                break

    print("#{}".format(test_case),end=" ")
    for i in array:
        print(i,end=" ")