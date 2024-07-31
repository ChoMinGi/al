N = int(input())
sample = list(map(int,input().split()))

total = float('inf')
sample.sort()
res = []
s=0
e=N-1

while(s<e):
    td = sample[s]+sample[e]
    if abs(td)<total:
        total = abs(td)
        res = [s,e]
    if td>=0:
        e-=1
    else:
        s+=1
        
print(*sorted([sample[res[0]],sample[res[1]]]))