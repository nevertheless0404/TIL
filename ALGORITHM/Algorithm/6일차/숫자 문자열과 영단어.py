# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = s 
    # 딕셔너리를 이용해 풀기
    num_c = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    # .items()로 딕셔너리의 한쌍을 이루어준다.
    # 각방에 0, 1번으로 나누어진다.
    for item in num_c.items():
        # 숫자를 문자열로 바꿔서 출력하기 
        answer = answer.replace(item[0], str(item[1]))   

    return int(answer)