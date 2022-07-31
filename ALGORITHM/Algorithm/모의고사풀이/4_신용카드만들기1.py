import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_신용카드만들기1.txt")

T = int(input())
for test_case in range(1 ,T+1):
    credit_num = list(map(int, input().split()))
    # print(credit_num)
    credit_num_sum = 0
    for index in range(len(credit_num)):
<<<<<<< HEAD
        # 짝수는 그래도 더하고 홀수는 곱하기 *2 를 한다.
=======
        # 짝수는 그대로 더하고 홀수는 곱하기 *2 를한다.
>>>>>>> a2c2f513366ccb1f657b2864b1be6be35c71d48f
        if (index+1) % 2 == 0:
            credit_num_sum += credit_num[index]
        else:
            credit_num_sum +=(credit_num[index] * 2)
    
    # 반복문을 돌려 확인하고, 10으로 떨어지는 것이 16번째 번호로 들어간다.
    for j in range(10):
        temp = credit_num_sum + j

        if temp % 10 == 0:
            result = j
            break

    print('#{} {}'.format(test_case,result))
            
    

        

