#교환학생 
#양 끝단에 요일이 배치될 경우 7일이 걸리는 것이 아니라 이틀이면 된다는 것에 주의하자
#내 풀이->테스트 통과 DATE=>5.14 풀이시간 50분 
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=1e9

    #print(arr)
    start=-1
    while start<6:
        d = 0
        last = n
        start += 1
        if arr[start]!=1:
            continue
        while last > 0:
            for i in range(start,start+7):
                if last == 0:
                    break
                if arr[i%7] == 1:
                    last -= 1
                d += 1
                #print(d,1234,last)
        #print(d,"D")
        ans=min(ans,d)



    print(f"#{tc} {ans}")