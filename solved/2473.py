N = int(input())
sample = list(map(int,input().split()))

total = float('inf')
sample.sort()
res = []
for i in range(N-2):
    now = sample[i]
    s=i+1
    e=N-1

    while(s<e):
        if e == i:
            e-=1
        if s == i:
            s+=1
        td = now+sample[s]+sample[e]
        if abs(td)<total:
            total = abs(td)
            res = [i,s,e]
        if td>=0:
            e-=1
        else:
            s+=1
        
print(*sorted([sample[res[0]],sample[res[1]],sample[res[2]]]))