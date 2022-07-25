# 두 정수 A와 B를 입력받은 다음, A+B를 출력하느 프로그램
# 첫째 줄에 테스트 케이스 개수 T
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)

t = int(input())
# 반복문
for i in range(t):
    a, b = map(int, input().split(','))
    print(a+b)
