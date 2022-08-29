# https://www.acmicpc.net/problem/9455

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/박스.txt")

for _ in range(int(input())):
    n, m = map(int,input().split())
    box = [input().split() for _ in range(n)] # 전체 리스트 생성
    ans = 0
    # 열 먼저 나열 
    for j in range(m):
        # 박스 이동거리 초기화
        cnt = 0
        for i in range(n-1,-1,-1): # 맨 뒤 리스트부터 거꾸로 탐색
            # 박스를 다 제 자리에 놓고 바닥을 1 
            if box[i][j] == '1':
                ans += cnt
            else:
                # 인덱스 값을 찾는 대신, 
                # 0이 나올 때마다 1씩 임시 카운트 값(cnt)을 추가해주면 된다.
                cnt += 1 
    print(ans)
    

