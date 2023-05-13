###내 풀이->테스트 통과 DATE=>5.13 풀이시간 30분 . 투 포인터 알고리즘
#https://ifuwanna.tistory.com/464
def palindromeIndex(s):
    # Write your code here
    start=0
    end=len(s)-1
    while start<=end:
        if s[start]!=s[end]:
            ns1=s[0:start]+s[start+1:]
            ns2=s[0:end]+s[end+1:]
            if ns1==ns1[::-1]:
                return start
            elif ns2==ns2[::-1]:
                return end
            return -1
        else:
            start+=1
            end-=1
    return -1