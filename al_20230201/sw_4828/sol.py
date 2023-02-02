import sys
sys.stdin= open('./sample_input.txt')
TC = int(input())
for T in range(TC):
    N = int(input())
    mini = 1000000                          # input의 최대값이 1000000이므로  mini를 설정
    Maxx = 1                                # 최솟값이 1 이므로 mini를 설정

    ls = list(map(int,input().split()))     # 리스트 받기

    for i in range(N):                      # for 문을 이용해 ls를 순회
        if Maxx < ls[i]:                    # i번째 원소가 Maxx 보다 크다면 Maxx = ls[i]
            Maxx = ls[i]
        if mini > ls[i]:                    # i번째 원소가 mini 보다 작다면 mini = ls[i]
            mini = ls[i]
    print(f"#{T+1}",Maxx - mini)            #Maxx - mini