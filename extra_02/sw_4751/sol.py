import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(TC):
    sr = input().strip()
    s_l = len(sr)
    s1 = "." + ".#.." *s_l
    s2 = ".#"*s_l*2 + "."
    s3 = "#"
    for i in sr:
        s3 = s3+"." + i + "."+ "#"
    s4 = ".#"*s_l*2 + "."
    s5 = "." + ".#.." *s_l
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)