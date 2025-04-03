def generate_good_permutations(n):
    from itertools import permutations

    def is_good(perm):
        # Function to check if a permutation is good
        idx_map = {value: idx for idx, value in enumerate(perm)}
        visited = [False] * n
        components = []

        for i in range(n):
            if not visited[i]:
                component = []
                x = i
                while not visited[x]:
                    visited[x] = True
                    component.append(perm[x])
                    x = idx_map[perm[x]]
                # Sort component and rotate to max
                max_val = max(component)
                max_index = component.index(max_val)
                rotated_component = component[max_index:] + component[:max_index]
                components.append(rotated_component)

        components.sort(key=lambda x: x[0])  # Sort by the first element
        result = []
        for comp in components:
            result.extend(comp)
        return result == list(perm)

    good_perms = []
    for perm in permutations(range(1, n + 1)):
        if is_good(perm):
            good_perms.append(perm)

    return good_perms

def find_kth_good_permutation(n, k):
    good_perms = generate_good_permutations(n)
    if k > len(good_perms):
        return -1
    else:
        return good_perms[k - 1]  # 1-based index

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = find_kth_good_permutation(n, k)
    if result == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))