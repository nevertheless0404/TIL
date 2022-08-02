# https://www.acmicpc.net/problem/4949

import sys
from turtle import st
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220802/균형잡힌 세상.txt")

while True:
    string = input()
    if string == '.':
        break
    
    stack= []
    # 균형이 맞으면 True 안맞으면 False
    flag = True
    for i in string:
        if i == '(' : #stack에 넣음
            stack.append(i)
        elif i == ')':
            # 마지막 원소와 짝이 맞으면
            if stack and stack[-1] == '(': #stack이 안비었으면 
                stack.pop()
            else:
                flag = False
                break
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
        
    if not stack and flag: 
        print('yes')
    else:
        print('no')
