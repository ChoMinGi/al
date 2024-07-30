T = int(input())
INF = float('inf')

for _ in range(T):
    K = int(input())
    pages = list(map(int,input().split()))
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    prefix_sum = [0]
    pg= 0
    for i in range(K):
        pg+=pages[i]
        prefix_sum.append(pg)
    
    knuth = [[0 for _ in range(K+1)]for _ in range(K+1)]
    for i in range(1,K+1):
        knuth[i][i] = i
    for i in range(1,K):
        for s in range(1,K+1-i):
            e = s+i
            dp[s][e] = INF
            for k in range(knuth[s][e-1],knuth[s+1][e]+1):
                if k<K and dp[s][e]>dp[s][k]+dp[k+1][e]+prefix_sum[e]-prefix_sum[s-1]:
                    dp[s][e]= min(dp[s][e],dp[s][k]+dp[k+1][e]+prefix_sum[e]-prefix_sum[s-1])
                    knuth[s][e] = k
    print(dp[1][K])