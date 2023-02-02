import sys
sys.stdin = open("sample_in.txt")

T = int(input())
for i in range(1,T+1):
    N = int(input())
    bus = []
    for j in range(N):
        ls = list(map(int,input().split()))
        if ls[0] == 1:
            bus.append(set(list(range(ls[1],ls[2]+1))))
        elif ls[0] == 2:
            r = list(range(ls[1],ls[2],2))
            r.append(ls[2])
            bus.append(set(r))
        else:
            if ls[1] % 2 == 0:
                lr =[ls[1]]
                for k in range(ls[1]+1,ls[2]):
                    if k % 4 ==0:
                        lr.append(k)
                lr.append(ls[2])
            else:
                lr = [ls[1]]
                for k in range(ls[1]+1,ls[2]):
                    if k %10 != 0 and k%3 == 0:
                        lr.append(k)
                lr.append(ls[2])
            bus.append(set(lr))
    us = bus[0]
    for j in range(1,N):
        us = us | bus[j]
    maxx = 0
    for j in us:
        cnt = 0
        for k in bus:
            if j in k:
                cnt += 1
        maxx = max(cnt,maxx)
    print(f"{i}",maxx)



