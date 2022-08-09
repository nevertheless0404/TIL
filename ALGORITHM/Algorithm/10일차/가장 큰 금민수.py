# https://www.acmicpc.net/problem/1526

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220809/가장 큰 금민수.txt")

n = int(input())
while True:
    flag = True
    for i in str(n):
        # 문자열로 변환해 4이거나 7이 아닌경우 false
        # 입력값보다 작거나 큰 금민수 중에서 가장 큰 수를 구해야 하기 때문에
        # 입력값에서부터 -1씩 해준다. 
        if i!= '4' and i!= '7':
            flag = False
            n -= 1
    if flag:
        print(n)
        break
