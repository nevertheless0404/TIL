import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_직사각형길이찾기.txt")
T = int(input())
for tc in range(1, 1+T):
    number = list(map(int, input().split()))
    # 정렬해주기 
    number.sort()
# a와 b가 다를 때 d는 a와 b중 하나 마주봄
# c 도 a,b 하나랑 마주봄 
    if number[0]!= number[1]:
        print('#{} {}'.format(tc, number[0]))
    else:
        print('#{} {}'.format(tc,number[2]))