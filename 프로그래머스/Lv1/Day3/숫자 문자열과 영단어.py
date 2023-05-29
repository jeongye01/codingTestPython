#https://school.programmers.co.kr/learn/courses/30/lessons/81301
##내 풀이->테스트 통과 DATE=>5.29 풀이시간 15분 
def solution(s):
    answer = ""
    nums={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    tmp=""
    for x in s:
        if ord('a')<=ord(x)<=ord('z'):
            tmp+=x
            if tmp in nums:
                answer += nums[tmp]
                tmp = ""
        else:
            answer+=x
    return int(answer)

'''
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


'''