# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    # answer = set()
    # 2개를 뽑아서 모든 경우의 수의 합을 구하기 위해 2중 for 문 이용 
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # 2개의 값을 더하여 리스트에 저장 
            if (numbers[i] + numbers[j] not in answer):
                answer.append(numbers[i]+numbers[j])
    answer.sort() #오름차순
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
