#https://school.programmers.co.kr/learn/courses/30/lessons/17681
##내 풀이->테스트 통과 DATE=>6.1 풀이시간 15분 
def solution(n, arr1, arr2):
    answer = []
    b1=[]
    b2=[]
    for a in arr1:
        tmp=[]
        while a>0:
            tmp.append(a%2)
            a//=2
        b1.append([0]*(n-len(tmp))+tmp[::-1])
    for a in arr2:
        tmp=[]
        while a>0:
            tmp.append(a%2)
            a//=2
        b2.append([0]*(n-len(tmp))+tmp[::-1])

    for i in range(n):
        tmp = ''
        for j in range(n):
            if b1[i][j] == 1 or b2[i][j] == 1:
                tmp+="#"
            else:
                tmp+=" "
        answer.append(tmp)
    return answer