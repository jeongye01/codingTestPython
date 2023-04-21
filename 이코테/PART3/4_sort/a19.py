n = int(input())
data = list(map(int, input().split())) 
data.sort()
# 중간값(median)을 출력
print(data[(n - 1) // 2])


'''
내 풀이->테스트 통과 DATE:4.22
n=int(input())
array=list(map(int,input().split()))

array.sort()
mid=len(array)//2
result=[]
if(len(array)%2==0):
    for tmp in [array[mid-1],array[mid]]:
        summary=0
        for j in range(n):
            summary+=abs(j-tmp)
            result.append([summary,tmp])
        result.sort(key=lambda x:(x[0],x[1]))
    print(result[0][1])
else:
    print(array[mid])


'''