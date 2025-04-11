def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = [i + 1 for i in range(n)]
    receivers = [i + 1 for i in range(n)]

    given = set()
    for i in range(n):
        if f[i] != 0:
            given.add(f[i])

    not_given = []
    for i in range(1, n + 1):
        if i not in given:
            not_given.append(i)

    zeros_indices = []
    for i in range(n):
        if f[i] == 0:
            zeros_indices.append(i)

    for i in range(len(zeros_indices)):
        f[zeros_indices[i]] = not_given[i]

    for i in range(len(zeros_indices)):
        if f[zeros_indices[i]] == zeros_indices[i] + 1:
            if i + 1 < len(zeros_indices):
                f[zeros_indices[i]], f[zeros_indices[i+1]] = f[zeros_indices[i+1]], f[zeros_indices[i]]
            else:
                
                for j in range(len(zeros_indices)):
                    if zeros_indices[j] + 1 != f[zeros_indices[i]]:
                        f[zeros_indices[i]], f[zeros_indices[j]] = f[zeros_indices[j]], f[zeros_indices[i]]
                        break
    print(*f)
solve()