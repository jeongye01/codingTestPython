#https://school.programmers.co.kr/learn/courses/30/lessons/68936
##내 풀이->테스트 통과 DATE=>6.20 풀이시간 20분 
zero=0
one=0
def splitArr(arr):
    p1 = []
    p2 = []
    for i in range(len(arr) // 2):
        p1.append(arr[i][0:len(arr) // 2])
        p2.append(arr[i][len(arr) // 2:])
    p3 = []
    p4 = []
    for i in range(len(arr) // 2, len(arr)):
        p3.append(arr[i][0:len(arr) // 2])
        p4.append(arr[i][len(arr) // 2:])
    return (p1, p2, p3, p4)

def dfs(arr):
    global one,zero
    if len(arr)==1:
        if arr[0][0]==0:
            zero+=1
        else:
            one+=1
        return
    summary=0
    for a in arr:
        summary+=sum(a)
    if summary==0:
        zero+=1
        return
    elif  summary==len(arr)**2:
        one+=1
        return
    p1, p2, p3, p4=splitArr(arr)
    dfs(p1)
    dfs(p2)
    dfs(p3)
    dfs(p4)


def solution(arr):
    dfs(arr)
    return [zero,one]