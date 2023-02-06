for _ in range(10):
    A = int(input())
    B = []
    maxi = 0
    # 이 문제는 그냥 가로 세로 양쪽 대각선 합 중에 가장 큰 것을 고르는 문제이다
    for i in range(100):                    # 그래서 100개 의 합 중에서 가장 큰 수를 고르고
        C = list(map(int,input().split()))
        maxi = max(maxi, sum(C))
        B.append(C)
    for i in range(100):                    # 세로도 마찬가지
        summ = 0
        for j in range(100):
            summ += B[j][i]
        maxi = max(maxi,summ)
    summ = 0
    for i in range(100):                # 왼쪽위에서 오른쪽 아래로
        summ += B[i][i]
    maxi = max(summ,maxi)
    summ = 0
    for i in range(100):                # 오른쪽위에서 왼쪽 아래로
        summ += B[i][99-i]
    maxi = max(summ,maxi)
    print("#{0} {1}".format(A,maxi))