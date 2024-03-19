from itertools import combinations

def get_subsets(weights):
    subsets = []
    for i in range(len(weights) + 1):
        for combo in combinations(weights, i):
            subsets.append(sum(combo))
    return subsets

def count_ways(N, C, weights):
    # 물건을 두 그룹으로 나눔
    A, B = weights[:N//2], weights[N//2:]
    
    # 각 그룹에 대한 모든 가능한 무게 조합을 구함
    A_subsets = get_subsets(A)
    B_subsets = get_subsets(B)
    B_subsets.sort()  # 이분 탐색을 위해 정렬
    
    count = 0
    for a_weight in A_subsets:
        low, high = 0, len(B_subsets)
        # 이분 탐색으로 가능한 B의 조합 중 C-a_weight 이하가 되는 것의 수를 찾음
        while low < high:
            mid = (low + high) // 2
            if a_weight + B_subsets[mid] <= C:
                low = mid + 1
            else:
                high = mid
        count += low
    
    return count
N, C = map(int, input().split())
weights = list(map(int, input().split()))


result = count_ways(N,C,weights)
print(result)