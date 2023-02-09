import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    s1 = input().strip()
    s2 = input().strip()
    my_mx = 0
    for i in s1:
        count = 0
        for j in s2:
            if i == j:
                count += 1
        my_mx = max(my_mx,count)
    print(f"#{T}",my_mx)