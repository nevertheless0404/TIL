# https://www.acmicpc.net/problem/2897

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220809/몬스터 트럭.txt")

r, c = map(int, input().split())
parking = []
for _ in range(r):
    parking.append(input())
no_car = 0
one_car = 0
two_car = 0
tree_car = 0
four_car = 0

for i in range(r):
    for j in range(c):
        if i+1 == r or j+1 == c:
            break
        w = parking[i][j]
        k = parking[i][j+1]
        y = parking[i+1][j]
        z = parking[i+1][j+1]

        tmp = w+k+y+z

        if '#' in tmp:
            continue
        else:
            num = tmp.count('X')
            if num == 0:
                no_car += 1
            elif num == 1:
                one_car += 1
            elif num == 2:
                two_car += 1 
            elif num == 3:
                tree_car += 1
            elif num == 4:
                four_car += 1
print(no_car)
print(one_car)
print(two_car)
print(tree_car)
print(four_car)