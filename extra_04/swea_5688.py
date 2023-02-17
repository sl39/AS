### 세제곱근을 찾아라 

TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    print(f"#{T}",end = " ")
    for i in range(int(n**(1/3))+2):
        if i**3 == n:
            print(i)
            break
    else:
        print(-1)
