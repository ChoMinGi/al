import sys

input = sys.stdin.readline

def max_profit(price_list):
    max = 0
    res = 0
    for p in price_list[::-1]:
        if p>max:
            max = p
        else:
            res+=max-p
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    print(max_profit(list(map(int,input().split()))))
    
