#View
#내 풀이->테스트 통과 DATE=>1248 풀이시간 40분 
n=int(input())
array=list(map(int,input().split()))
ans=0
for i in range(2,n-2):
    able=True
    cnt=int(1e9)
    for j in range(i-2,i+3):
        if(array[i]<=array[j] and i!=j):
            able=False
            break
        if(i!=j):
            cnt=min(cnt,array[i]-array[j])
    if(able):
        ans+=cnt
print("#"+str(test_case),str(ans))

'''
다른 유저 코드
for test_case in range(1,11):
    result = 0
    houseCount = int(input())
    house = list(map(int , input().split()))
    for i in range(2, houseCount-2):
        arMax = max(house[i-1],house[i-2],house[i+1],house[i+2])
        if house[i] > arMax:
            result += ( house[i] - arMax )

    print("#{} {}".format(test_case,result))

'''