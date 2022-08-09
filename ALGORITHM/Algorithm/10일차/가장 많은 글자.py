# https://www.acmicpc.net/problem/1371

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220809/가장 많은 글자.txt")
input = sys.stdin.read
# 길이 결과값을 저장할 리스트 
words = [0]*26
s = input().replace('\n',' ').replace(' ','')

# words 리스트의 0번 인덱스부터 해당 문자가 존재한다면 증가
for i in s:
    words[ord(i)-97] += 1

for j in range(26):
    # 최댓값이 같다면 
    if words[j] == max(words):
        # 알파벳 순으로 앞서는 것부터 출력
        print(chr(97+j), end = '')
