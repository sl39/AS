# import sys
# sys.stdin = open("sample_input.txt")

def BruteForce(str1, str2):   # 패턴 매칭 알고리즘 이용
    i = 0
    j = 0
    while i < s1 and j < s2:
        if str1[i] != str2[j]:
            j = j - i
            i = - 1
        i = i + 1
        j = j + 1
    if i == s1:
        return 1
    else:
        return 0

TC = int(input())

for T in range(1,TC+1):
    str1 = input().strip()
    str2 = input().strip()
    s1 = len(str1)
    s2 = len(str2)
    print(f"#{T}",BruteForce(str1, str2))

