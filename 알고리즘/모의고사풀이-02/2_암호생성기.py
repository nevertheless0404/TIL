from re import M
import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-04/1회차/김유영/_암호생성기.txt")

t = 10
for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))
    # 하나씩 - 해줄 숫자 
    count = 1

    while True:
        # 사이클을 돌면서 마이너스 해주기 
        cycle = num.pop(0) - count
        # 0이하 거나 0일 경우 추가 
        # 해당 번호와 함께 나오기 
        if cycle < 0:
            cycle = 0
        num.append(cycle)
        
        # 마지막 숫자가 0이 되었다면 반복문 종료 
        if cycle <= 0:
            break
        count += 1

        # 한 사이클에 5번이기 때문에 
        # 5이상이면 다시 초기화를 하고 
        # 추가 해준다. 
        if count > 5:
            count = 1
    
    print('#{}'.format(tc),end =" ")
    for i in num:
        print(i, end =" ")
    print()
 