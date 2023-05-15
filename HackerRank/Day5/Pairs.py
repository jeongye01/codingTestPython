####내 풀이->테스트 통과 DATE=>5.15 풀이시간20분
#탐색은 무조건 BS로 하자
def find(value):
    st=0
    ed=n-1
    while st<=ed:
        mid=(st+ed)//2
        if arr[mid]==value:
            return True
        if arr[mid]>value:
            ed=mid-1
        else:
            st=mid+1
    return False

def pairs(k, arr):
    #comb=list(combinations(arr,2))
    ans=0
    arr.sort()
    for a in arr:
        if a>k:
            if find(a-k): # a+b=k일때 a쪽만 탐색하면 됨(중복 카운트 방지)
                ans+=1
    return ans