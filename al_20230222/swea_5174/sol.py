import sys
sys.stdin = open("sample_input.txt")
from collections import deque

TC = int(input())

for T in range(1,TC+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    tree = [[] for i in range(E+2)]

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        tree[p].append(c)
    print(tree)
    q = deque([N])
    cnt = 0
    while q:
        cnt += 1
        p = q.popleft()
        for i in tree[p]:
            q.append(i)
    print(f'#{T}',cnt)