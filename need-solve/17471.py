def generate_subsets(N):
    all_subsets = []
    for mask in range(1 << N):  # 2^N 경우의 수
        subset = [i for i in range(N) if mask & (1 << i)]
        all_subsets.append(subset)
    return all_subsets

# 예를 들어 N=3일 경우, 부분집합을 생성해보기
N = 3
subsets = generate_subsets(N)
for subset in subsets:
    print(subset)
