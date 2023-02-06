import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
ls = list(range(1,13))
for T in range(TC):
    N, K = map(int,input().split())
    result = []                                 # 모든 경우의 수를 담을 리스트
    for i in range(1,1<<12):

        lis = []                                # 하나의 경우의 수를 담을 리스트
        
        for j in range(12):
        
            if i & (1<<j):                      # 여기까지는 모든 경우의 수를 다 계산
                lis.append(ls[j])               # 이때 i 번째의 경우의 수때 그때 만족하는 수를 고르고
        if len(lis) == N and sum(lis) == K:     # 그 경우중에 길이가 N 이고 합이 K 인 리스트를 골라서
                result.append(lis)              # result 리스트에 담는다
    print(f"#{T}", len(result))