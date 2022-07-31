import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T+1):
    # '-'를 써야 하므로 숫자가 아니라 문자로
    num = input()
    # replace로 '-'를 공백으로 처리해준다.
    num = num.replace('-','')
    
# num안에 '34569'가 들어가고 숫자의 개수가 16이면
    if num[0] in '34569' and len(num) == 16:
        # 1로 출력
        print(f'#{test_case} 1')

    else:
        # 아니면 0으로 출력
        print(f'#{test_case} 0')