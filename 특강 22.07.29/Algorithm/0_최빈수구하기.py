import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_최빈수구하기.txt")

T = int(input())
for test_case in range (1, T+1):
    N = int(input())
    # 점수를 입력 받아 리스트로 작성 
    score = list(map(int, input().split()))
    date = [0] * 101
    # 반복문으로 통해 score 값을 하나씩 확인
    # 그 값을 인덱스하여 date 리스트 값에 1씩 증가!
    for i in score:
        date[i] += 1
        
    max_m = 0
    # 반복문을 이용해 값을 할당해주고  
    # 최대값 구해주기 
    for j in range(0, len(date)):
        if date[j] >= max_m:
            max_index = j
            max_m = date[j]
    print('#{} {}'.format(N, max_index))

    
 


