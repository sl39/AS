import sys
sys.stdin = open("input.txt")

TC = int(input())
for T in range(1,TC+1):
    sr = input().strip()
    result = 1
    n  = len(sr)
    for j in range(n//2):
        if sr[j] == sr[-j-1]:
            pass
        else:
            result = 0
            break
    print(f"#{T}",result)