###내 풀이->테스트 통과 DATE=>5.14 풀이시간 15분
def superDigit(n, k):
    # Write your code here
    nrr= list(map(int,str(n)))
    ans=sum(nrr)*k #n*k를 먼저하지 말고 sum(n)에 k를 곱하는게 효율적!
    while ans>=10:
        nrr=list(map(int,str(ans)))
        ans=sum(nrr)
    return ans