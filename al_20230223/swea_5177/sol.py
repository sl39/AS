import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    heap = [0]*(n+1)
    ls = list(map(int,input().split()))
    for i in range(n):
        p = i+1
        if i == 0:
            heap[p] = ls[i]
        else:
            heap[p] = ls[i]
            while p>0:
                if heap[p] < heap[p//2]:
                    heap[p] , heap[p//2] = heap[p//2], heap[p]
                    p = p//2
                else:
                    break
    mys = 0

    while n:
        n = n//2
        mys += heap[n]

    print(f'#{T}',end=" ")
    print(mys)

