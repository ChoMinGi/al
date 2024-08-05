a_list = list(*map(str,input().split()))
b_list = list(*map(str,input().split()))
A = len(a_list)
B = len(b_list)

# dp 배열 초기화 (2행만 사용)
dp = [[0] * (A + 1) for _ in range(2)]
sequence = [[""] * (A + 1) for _ in range(2)]

# LCS 길이 계산 및 수열 구축
for i in range(1, B + 1):
    for j in range(1, A + 1):
        if a_list[j - 1] == b_list[i - 1]:
            dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            sequence[i % 2][j] = sequence[(i - 1) % 2][j - 1] + a_list[j - 1]
        elif dp[(i - 1) % 2][j] >= dp[i % 2][j - 1]:
            dp[i % 2][j] = dp[(i - 1) % 2][j]
            sequence[i % 2][j] = sequence[(i - 1) % 2][j]
        else:
            dp[i % 2][j] = dp[i % 2][j - 1]
            sequence[i % 2][j] = sequence[i % 2][j - 1]

print(dp[B % 2][A])
print(''.join(sequence[B % 2][A]))