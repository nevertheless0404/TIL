# https://www.acmicpc.net/problem/2309

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/일곱 난쟁이.txt")

list_ =[]
for _ in range(9):
    list_.append(int(input()))
total = sum(list_)

# 이중 for문을 통해 2개의 원소를 배재했을 때에 대한 모든 경우의 수를 찾아낸다.
for i in range(9):
    for j in range(i+1, 9):
        # 아홉난쟁이들의 합 - 가짜난쟁이의 합은 100이 되어야 한다.
        if total - list_[i]- list_[j] == 100:
            # 리스트에서 값을 지웠을 경우 인덱스 값이 달라지기 때문에 값을 저장 
            # 가짜난쟁이 2명을 빼준다.
            a, b = list_[i], list_[j]
            list_.remove(a)
            list_.remove(b)
            # 오름차순으로 정렬해주기 
            for k in sorted(list_):
                print(k)
            break
        # 7명이면 그냥 나와!
    if len(list_) == 7:
        break
            

