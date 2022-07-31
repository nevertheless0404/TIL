import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_소득불균형.txt")

T = int(input())
for tese_case in range(1, T+1):
    n = int(input())
    date = list(map(int, input().split()))
    # 입력받은 평균을 구해준다.
    avg = sum(date)//n
    count = 0
    # 평균 이하인 사람들을 구해준다. 
    for i in date:
<<<<<<< HEAD
        if i <= avg:   # 평균이하
            count += 1   # 평균이하인 사람들은 더해준다.
    print('#{} {}'.format(tese_case,count))
=======
        if i <= avg:    # 평균이하
        
            count += 1    # 평균이하인 사람들을 더해준다.
    print('#{} {}'.format(tese_case,count))
>>>>>>> a2c2f513366ccb1f657b2864b1be6be35c71d48f
