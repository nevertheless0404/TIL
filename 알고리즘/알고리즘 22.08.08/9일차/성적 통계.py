# https://www.acmicpc.net/problem/5800

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/성적 통계.txt")

k = int(input())
for tc in range(k):
    student_score = input().split()
    # 학생수와 점수를 분리해줍니다.
    # 둘다 정수형으로 
    n = int(student_score[0])
    score = list(map(int, student_score[1:]))

    max_score = max(score)
    min_score = min(score)

    # 점수를 내림차순으로!
    score.sort(reverse=True)

    gaps = []

    # 점수 뒤에서 하나 뺀 것까지 반복 
    for i in range(n-1):
        # 현재 점수와 그 뒤에 인덱스에 있는 점수와 차이를 저장 
        gap = score[i] - score[i+1]
        gaps.append(gap)

    # 최대 차이를 저장하는 변수 
    largest_gap = max(gaps)

    print(f"Class {tc+1}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
