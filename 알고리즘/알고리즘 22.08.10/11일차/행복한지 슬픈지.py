# https://www.acmicpc.net/problem/10769

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/행복한지 슬픈지.txt")

emoji = input()

e_happy = emoji.count(":-)")
e_sad = emoji.count(":-(")

if e_happy == 0 and e_sad == 0:
    print("none")
elif e_happy==e_sad:
    print("unsure")
elif e_happy > e_sad:
    print("happy")
else:
    print("sad")
