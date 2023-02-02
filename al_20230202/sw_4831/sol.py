


# 먼저 충전소 사이의 거리가 한번 충전으로 갈 수 있는 거리보다 멀면 0을 출력
# 아니면 현재 위치에서 갈수 있는 충전소중 가장 먼 곳에 있는 충전소에서 충전


import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for i in range(1,T+1):
    K, N, M = map(int,input().split())
    # K는 갈수 있는 거리,N은 정류장 수, M은 충전소 수

    elec = [0] + list(map(int, input().split()))

    bus = 0
    # 버스의 시작 위치

    MMM = 0
    
    for j in range(M):
        # 충전소 간의 거리를 구하는 코드
        if MMM < elec[j+1] - elec[j]:

            # 충전소 간의 거리중 최대를 구함
            MMM = elec[j+1] - elec[j]
    
    if MMM > K:
        # 1. 그 거리가 K보다 큰 경우

        print(f"#{i}",0)
        # 0 을 출력
    
    else:
        # 2. 작거나 같은 경우
        count = 0

        while bus+K < N:
            # 만약에 버스의 현재 위치에서 K를 더한 거리가 도착 위치 보다 크면 종료
            stl = 0
            for j in range(len(elec)):

                if elec[j] <= bus + K:
                    # 버스의 갈수 있는 거리 중 최대값
                    st = elec[j]
                    # 충전소 리스트들이 정렬 되어 있으므로
                    stl = j
                    # 그리고 그 값의 인덱스를 stl에 저장


                    # 이렇게 돌리면 마지막에 남는건 갈 수 있는 충전소중 가장 먼 거리에 있는 충전소에 도착하게 됨

                else:                               # 만약 그 다음 충전소가 갈수 있는 거리보다 멀리 있다면 for문을 빠져 나옴
                    break

            elec = elec[stl+1:]                     # 지나간 충전소는 제외함
            bus = st                                # 그리고 그 충전소에서 버스는 충전을 함
            count += 1                              # 충전소를 한번 들렀으므로 count += 1

        print(f"#{i}", count)                       # 그리고 count를 프린트

