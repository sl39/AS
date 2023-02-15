import sys
sys.stdin = open("s_input.txt")

TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    price = list(map(int, input().split()))
    stack = []
    max_idx = 0
    pre = 0
    res = 0
    while max_idx < N:
        for i in range(max_idx,N):
            if price[i] > price[max_idx]:
                max_idx = i
        for i in range(pre,max_idx):
            res += price[max_idx] - price[i]
        pre = max_idx+1
        max_idx += 1
    print(f"#{T}", res)