import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-04/1회차/김유영/_어디에단어가들어갈수있을까.txt")

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    # 들어갈 수 있는 자리수 초기화 
    result = 0
    # 가로 단어 길이 확인
    for i in range(n):
        count = 0
        for j in range(n):
            # 흰색이 나오면 증가
            if data[i][j] == 1:
                count += 1
                # 검정색이거나 마지막 행일 경우 
                # count 값과 k 값이 같을 경우 
                # 최종 수를 증가 시킨다.
            if data[i][j] == 0 or j == n - 1:
                if count == k:
                    result += 1
                # 값이 0 일 경우 초기화 
            if data[i][j] == 0:
                count = 0
        
    # 세로 길이 확인
    for i in range(n):
        count = 0   
        for j in range(n):
            if data[j][i] == 1:
                count += 1
            if data[j][i] == 0 or j == n - 1:
                if count == k:
                    result += 1
                if data[j][i] == 0:
                    count = 0
    
    print('#%d %d' % (tc, result))


    