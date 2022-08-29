# https://www.acmicpc.net/problem/1598

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/꼬리를 무는 숫자 나열.txt")

# 입력 받은 두 정수중 작은 값에서 큰 값으로 4를 더하면서 카운팅
# 작은 값에 큰 값보다 커지면 종료 
# 두수의 차이를 더해주면 높이 

a, b = map(int, input().split())
# 원점을 0으로 생각하기 위해 
a -= 1
b -= 1
# 가로 좌표는 4로 나눈 몫, 세로는 4로 나눈 나머지 
print(abs(a//4-b//4)+abs(a%4-b%4))