# https://www.acmicpc.net/problem/2864

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220803/5와 6의 차이.txt")

A, B = map(str, input().split())
if "6" in A or "6" in B:
    A = A.replace("6","5")
    B = B.replace("6","5")
_min = sum(map(int, [A, B]))

if "5" in A or "5" in B:
    A = A.replace("5","6")
    B = B.replace("5","6")
_max = sum(map(int, [A, B]))
print (_min, _max)

# 2.
# A, B = input().split()

# min_ = int(A.replace('6', '5')) + int(B.replace('6','5'))
# max_ = int(A.replace('5', '6')) + int(B.replace('5','6'))

# print(min_, max_)