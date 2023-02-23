import sys
sys.stdin = open('sample_input.txt')
input = sys.stdin.readline

def compare(n):
    global num
    if n <= N:
        tree[n] = stack[n-1]
        num = n
        while num > 0:
            num = num//2
            if tree[n] < tree[num]:
                tree[n], tree[num] = tree[num], tree[n]
            else:
                break
        compare(n+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    stack = list(map(int, input().split()))
    num = 0
    compare(1)
    result = 0
    while N > 0:
        N = N // 2
        result += tree[N]
    print(f'#{tc} {result}')
    print(tree)