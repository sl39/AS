import sys
sys.stdin= open('./sample_input.txt')
TC = int(input())
for i in range(TC):
    N, M = map(int,input().split())    
    ls = list(map(int,input().split()))
    Maxx = 1 * M                            # 최소값이 1이고 개수가 M개 이므로 이렇게 잡음
    mini = 10000 * M                        # 최댓값이 10000이고 개수가 M 개이므로
    for start in range(N-M+1):
        mys = 0                             # 이웃한 M개의 수를 더하기 위한 mys 지정
        for ing in range(M):                # start 번째에서 시작해서 M 개를 더함
            mys += ls[start + ing]          # start = 3 M = 5
        if mys > Maxx:                      # mys가 Maxx 보다 크면 Maxx 에저장
            Maxx = mys
        if mys < mini:                      # mys가 mini 보다 작으면 mini 에 저장
            mini = mys
    print(f"#{i+1}",Maxx - mini)            # 차를 프린트


