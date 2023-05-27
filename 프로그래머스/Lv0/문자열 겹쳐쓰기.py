#https://school.programmers.co.kr/learn/courses/30/lessons/181943
def solution(my_string, overwrite_string, s):
    slist=list(my_string)
    slist[s:s+len(overwrite_string)]=list(overwrite_string)
    return "".join(slist)

#더 괜찮은 풀이
'''
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


'''