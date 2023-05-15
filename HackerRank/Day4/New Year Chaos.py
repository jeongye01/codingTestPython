#https://kinchi22.github.io/2019/02/20/new-year-chaos/
####내 풀이->테스트 통과 DATE=>5.14 풀이시간 120분 #타블로그 참고후 풀이
def minimumBribes(q):
    # Write your code here
    bribes = 0
    mins = [int(1e9),int(1e9)]
    for i in range(n-1,-1,-1):
        if q[i]-(i+1)>2:
            print("Too chaotic")
            return
        if q[i]>mins[0]: #여기서는 뇌물을 최대 두번만 사용한 경우임. 따라서 뒤에 있는 수들 최소값 두개만 따지면 됨.
            bribes+=2
        elif q[i]>mins[1]:
            bribes+=1
        if q[i]<mins[1]:
            mins=[mins[1],q[i]]
        elif q[i]<mins[0]:
            mins=[q[i],mins[1]]
        
    print(bribes)