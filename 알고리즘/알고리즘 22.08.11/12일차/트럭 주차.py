# https://www.acmicpc.net/problem/2979


import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220811/트럭 주차.txt")

a, b, c = map(int, input().split())
# 시간
arr = [0] * 100
answer = 0
for _ in range(3):
    begin, end = map(int, input().split())
    for i in range(begin, end):
        arr[i] += 1
# 시간을 딕셔너리에 넣어서 곱해주고 값을 만들어주기
for j in arr:
    answer += {0:0, 1:a, 2:b*2, 3:c*3}[j] 
print(answer)