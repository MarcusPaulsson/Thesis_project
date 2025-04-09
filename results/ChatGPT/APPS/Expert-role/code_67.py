def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - a[i]
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            if target in a:
                if target != a[i] or a.count(target) > 1:
                    nice_indices.append(i + 1)

    return len(nice_indices), nice_indices

n = int(input())
a = list(map(int, input().split()))

k, indices = find_nice_indices(n, a)

print(k)
if k > 0:
    print(' '.join(map(str, indices)))