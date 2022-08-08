# https://www.acmicpc.net/problem/1436

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/영화감독 숌.txt")

n = int(input())
end = 666
cnt = 0

while True:
    # 1부터 차례대로 확인을 하여 666번을 포함하면
    # 증가 
    if '666' in str(end):  
        cnt += 1
        # 수가 같다면 
        # 출력하고 종료
    if cnt == n:
        print(end)
        break
    # '666'이 포함된 수가 나올때 까지 1씩 증가 
    end += 1
