# 별 찍기
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는다.

a = int(input())

for star in range(1, a+1):
    print("*" * star)