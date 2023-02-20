# 암호 생성
### 아이디어
### 하나씩 넘어가면서 t를 빼줌
### t가 5를 넘어가면 1로 바꿔주고
### rear에 하나씩 더해주고 8로 나눈 나머지로 바꿔줌




import sys
sys.stdin = open("input.txt")
for T in range(1,11):
    tc = int(input())
    nums = list(map(int,input().split()))
    t = 1
    rear = 0


    while True:

        # 만약에 빼준 값이 0보다 작거나 같으면
        # 0으로 바꿔주고 while 문 종료
        if nums[rear] - t <= 0:
            nums[rear] = 0
            break
            
        # 아니면 계속해서 빼줌
        else:
            nums[rear] -= t

        # rear를 1더해주고 8로 나눈 나머지로 바꿔줌
        rear = (rear+1) % 8

        # t 도 마찬가지로 더하기 1을 해주고  6이되면 다시 1로 바꿔줌
        t += 1
        if t == 6:
            t = 1



    print(f"#{T}", end=" ")

    # nums[rear] 값이 0 이므로
    # rear + 1 부터 시작해서 하나씩 출력한다
    for i in range(8):
        rear = (rear+1)%8
        if i == 7:
            print(nums[rear])
        else:
            print(nums[rear],end=" ")
