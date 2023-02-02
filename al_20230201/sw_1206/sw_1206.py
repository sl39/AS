import sys
sys.stdin = open("./input.txt")

for i in range(10):
    N = int(input())
    AS = list(map(int,input().split()))
    mys = 0
    for j in range(2,N-2):
        A = [1,2,-1,-2]         # 왼쪽 2개 오른쪽 2개를 위한 리스트
        maxx = 0
        for k in A:
            if maxx < AS[j + k]:        # 만약에 양쪽 2개씩 생각 했을 때
                maxx = AS[j + k]        # 4개중 가장 큰거를 maxx에 저장
        if maxx >= AS[j]:               # 만약 maxx 가 j 번쨰보다 크면 
            pass                        # pass
        else:
            mys += AS[j] - maxx         # 아니면 j번째랑 maxx 차를 mys 에 더함
    print(f"#{i+1}", mys)