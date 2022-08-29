# https://www.acmicpc.net/problem/2161

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/카드1.txt")

from collections import deque
# 1. 
n = int(input())
card = []
for number in range(1, n+1):
    card.append(number)

while len(card) > 1:
    # 맨 앞에 카드를 뒤로!
    print(card.pop(0), end=" ")
    card.append(card.pop(0))

print(card[0])


# 2. 
n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    print(queue.popleft(),end = " ")
    queue.append(queue.popleft())

print(queue[0])
