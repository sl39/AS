import sys
sys.stdin = open("sample_in.txt")

T = int(input())
for i in range(T):
    N = int(input())
    bus = []
    for j in range(N):
        ls = list(map(int,input().split()))
        if ls[0] == 1:
            bus