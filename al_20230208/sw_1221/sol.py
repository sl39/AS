import sys
sys.stdin = open("GNS_test_input.txt")

nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

TC = int(input())
for T in range(1,TC+1):
    A,B = map(str,input().split())
    ls = list(map(str,input().split()))
    dic = {}
    for i in nums:
        dic[i] = 0
    for i in ls:
        dic[i] = dic[i] + 1
    for i in dic:
        print(dic[i] * (i+" "))



