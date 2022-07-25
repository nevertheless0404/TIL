# 두 정수 A와 B를 입력받은 다음, A+B를 출력하느 프로그램
# 첫째 줄에 테스트 케이스 개수 T

t = int(input())
# 반복문
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)