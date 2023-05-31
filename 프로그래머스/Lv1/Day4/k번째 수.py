#https://school.programmers.co.kr/learn/courses/30/lessons/42748
#내 풀이->테스트 통과 DATE=>6.1 풀이시간 5분 
def solution(array, commands):
    answer = []
    for c in commands:
        new_array=array[c[0]-1:c[1]]
        answer.append(sorted(new_array)[c[2]-1])
    return answer