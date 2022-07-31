# https://www.acmicpc.net/problem/2577
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘01/01-ALGORITHM/1회차/김유영/20220725/0_숫자의개수.txt")
A = int(input())
B = int(input())
C = int(input())

abc = str(A * B * C)


# 반복문으로 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 확인
for i in range(10):
    print(abc.count(str(i)))