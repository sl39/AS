# 회전

import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f"#{T}",arr[m%n])
