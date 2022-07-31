import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-03/1회차/김유영/_암호문1.txt")

for test_Case in range(1,11) : 
 
    oringe_m = int(input())
    origin = list(map(int, input().split()))
    command_n = int(input())
    command = list(input().split())
 
    for i in range(len(command)):
        if command[i] == 'I':
            index = int(command[i+1])
            nums = int(command[i+2])
             
            for j in range(nums):
                origin.insert(index + j,int(command[(i+3)+j]))
 
        else:
            continue
 
        new_origin = ' '.join(map(str,origin[:10]))
         
    print(f'#{test_Case}', new_origin)