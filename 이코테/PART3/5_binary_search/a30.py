from bisect import bisect_left, bisect_right
#“fro”로 시작되는 마지막 단어의 위치를 찾고, “fro”로 시작되는 첫 단어의 위치를 찾아서 그 위치의 차이를 계산하면 될 것이다. 
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]
def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입
    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::- 1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer



'''
내 풀이 -> 테스트 불통
def bs(wds,q):
    start=0
    end=len(wds)-1
    while (start<=end):
        mid=(start+end)//2
        isMatch=True
        for i in range(len(q)): #앞에서 부터 비교
            if(q[i]!=wds[mid][i] and q[i]!="?"):
                isMatch=False
                break
        if isMatch:
            return mid
        else:
            if(q[i]<wds[mid]):
                end=mid-1
            elif(q[i]>wds[mid]):
                start=mid+1
    return -1
  
def solution(words, queries):
    answer = [0]*len(queries)
    array=[[] for _ in range(10001)] #길이별로 문자열 모아두는 리스트
    for w in words:
        array[len(w)].append(w)
    words.sort()
    for i in range(len(queries)):
        wds=array[len(queries[i])][:]
        while True:
            idx=bs(wds,queries[i])
            if(idx==-1):
                break
            answer[i]+=1
            wds=wds[0:idx]+wds[idx+1:]
    return answer
'''