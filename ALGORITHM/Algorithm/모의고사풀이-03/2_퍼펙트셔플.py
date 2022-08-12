from ctypes.wintypes import WORD
import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-05/1회차/김유영/_퍼펙트셔플.txt")


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    word = list(input().split())
    answer = []
    # 교차 해서 담기 위해 
    card = 0
    card_1 = (n+1)//2 
    
    # 우선 카드를 정확히 절반으로 나누고 교차해서
    # 다시 넣어주기 
    # 뒤에 있는거 까지 넣어주기
    for i in range(n//2):
        # 절반 나눠진 앞에 부분만 넣어주기
        answer.append(word[card])
        # 절반 나워진 뒤에 부분 넣어주기
        answer.append(word[card_1])
        # 번갈아 가면서 넣어주기!
        card , card_1 = card + 1, card_1 + 1 
        
# 홀수에서 뒤에 더 있다면 넣어주기 
    if n % 2 == 1:
        answer.append(word[n//2])
  

    print('#{} {}'.format(tc, " ".join(map(str, answer))))



