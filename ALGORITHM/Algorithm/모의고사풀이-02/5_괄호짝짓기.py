import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-04/1회차/김유영/_괄호짝짓기.txt")

t = 10
for tc in range(1, t+1):
    # 데스트 케이스 길이
    N = int(input())    
    # 괄호
    bracket = input()
    # 괄호를 담아줄 리스트
    stack = []
    result = 1
    #왼쪽괄호들을 다 스택에 저장
    for i in range(N):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[' or bracket[i] == '<':
            stack.append(bracket[i])

        # 위에 먼저 넣은 왼쪽과 밑에 나오는 오른쪽을 비교하여 
        # 스택에 저장된 것을 맨뒤에서 부터 하나씩 검사! 
        # 맞으면 1 아니면 0
        if bracket[i] == ')':
            # 1이상 들어가있고, '('와 맞지 않으면 0 
            # 그리고 바로 나와주기 ! 
            if len(stack) > 0 and stack.pop() != '(':
                result = 0
                break
        if bracket[i] == '}':
            if len(stack) > 0 and stack.pop() != '{':
                result = 0
                break
        if bracket[i] == ']':
            if len(stack) > 0 and stack.pop() != '[':
                result = 0
                break
        if bracket[i] == '>':
            if len(stack) > 0 and stack.pop() != '<':
                result = 0
                break



    print("#{} {}".format(tc,result ))
    
        
