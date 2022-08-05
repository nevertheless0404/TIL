import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-04/1회차/김유영/_조교의성적매기기.txt")

credit = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    score = []
    for _ in range(n):
        # 중간, 기말, 과제 점수 받아오기
        a, b, c = map(int, input().split())
        total_value = (a * 0.35) + (b * 0.45) + (c * 0.2)
        score.append(total_value)

    # 구하고 싶은 학생의 점수를 할당 
    student_k = score[k-1]
    # 내림차순으로 정렬
    score.sort(reverse=True)

    # n/10 명의 학생들에게 동일한 평점을 부여할 수 있음
    value = n // 10
    # 학생의 점수를 해당한 것을 인덱스로 찾아 평점을 나눈다.
    answer = score.index(student_k) // value

    print('#%d %s' % (tc, credit[answer]))


