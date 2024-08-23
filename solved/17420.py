from collections import defaultdict

N = int(input())

coupon = defaultdict(list)
a = list(map(int,input().split()))
for idx,b in enumerate(list(map(int,input().split()))):
    coupon[b].append(a[idx])
res = 0
prev_due = 0

for plan in sorted(list(coupon.keys())):
    new_due = 0
    for due in sorted(list(coupon.get(plan))):
        if due<prev_due or due<plan:
            postpone = max(plan,prev_due)-due
            pp = (postpone + 29) // 30 
            res += pp
            new_due = max(new_due,due+pp*30)
        else:
            pp = 0
            new_due = max(new_due,due)
    prev_due = max(prev_due,new_due)


print(res)