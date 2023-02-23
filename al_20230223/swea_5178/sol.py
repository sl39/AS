import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    n, m, l =map(int,input().split())
    node = [0] * (n+1)
    for i in range(m):
        idx,value = map(int,input().split())
        node[idx] = value
    for i in range(n,0,-1):
        node[i//2] += node[i]
    print(f"#{T}", end=" ")
    print(node[l])
