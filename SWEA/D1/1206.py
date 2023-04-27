#View

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