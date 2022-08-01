# https://www.acmicpc.net/problem/1076

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/저항.txt")

a = input()
b = input()
c = input()

colors = {'black': 0, 'brown': 1, 'red':2, 'orange':3, 'yellow':4,
          'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
print((colors[a]*10 + colors[b])* (10**colors[c]))