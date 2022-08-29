# https://www.acmicpc.net/problem/15953

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220803/상금 헌터.txt")

t = int(input())

def score1(ranker):
    if ranker == 1:
        return 5000000
    elif 1 < ranker <= 3:
        return 3000000
    elif 3 < ranker <= 6:
        return 2000000
    elif 6 < ranker <= 10:
        return 500000
    elif 10 < ranker <= 15:
        return 300000
    elif 15 < ranker <= 21:
        return 100000
    else:
        return 0
def score2(ranker):
    if ranker == 1:
        return 5120000
    elif 1 < ranker <= 3:
        return 2560000
    elif 3 < ranker <= 7:
        return 1280000
    elif 7 < ranker <= 15:
        return 640000
    elif 15 < ranker <= 31:
        return 320000
    else:
        return 0
for _ in range(t):
    a,b = map(int, input().split())
    print(score1(a) + score2(b))
