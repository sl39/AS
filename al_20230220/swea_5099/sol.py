# 피자

import sys
sys.stdin = open("sample_input.txt")

TC = int(input())

for T in range(1,TC+1):
    n, m =map(int,input().split())
    arr = list(map(int,input().split()))

    A = 0
    front = n
    rear = 0
    pizza = list(range(n))

    res = []
    while A < m:
        if arr[pizza[rear]]:
            arr[pizza[rear]] = arr[pizza[rear]]//2
            if arr[pizza[rear]] == 0:
                res.append(pizza[rear]+1)
                A += 1
                if front < m:
                    pizza[rear] = front
                    front += 1
        rear = (rear+1)%n


    print(f"#{T}",res[-1])