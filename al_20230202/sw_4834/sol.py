## 횟수가 가장 많이 나온 카드와 그 횟수를 구하는 문제


import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for i in range(1,T+1):
    nums = [0]*10                           # 카드가 0~9 까지므로 카드의 횟수를 넣을 nums 리스트 생성
    N = int(input())
    A = input()                             # 리스트로 수를 받음
    for j in A:
        nums[int(j)] += 1                   # str에서 하나씩 정수로 바꾸고 그 정수에다가 하나씩 1을 더함
    result = 0
    card = 0
    for n in range(10):                     # nums 리스트 안에
        if nums[n] >= result:               # 크기를 비교하여
            result = nums[n]                # 크기가 크다면 result에 횟수를 저장
            card = n                        # 그리고 그 idx를 card 에저장
    print(f"#{i}",card ,result)             # 둘다 프린트
