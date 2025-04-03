def max_beauty(n, trophies):
    max_golden = trophies.count('G')
    if max_golden == n or max_golden == 0:
        return max_golden

    golden_indices = [i for i in range(n) if trophies[i] == 'G']
    max_length = 0

    for i in range(len(golden_indices)):
        for j in range(i + 1, len(golden_indices)):
            if golden_indices[j] - golden_indices[i] - 1 == j - i - 1:
                max_length = max(max_length, golden_indices[j] - golden_indices[i] + 1)

    for i in range(n):
        if trophies[i] == 'S':
            for j in range(n):
                if trophies[j] == 'G':
                    temp_trophies = list(trophies)
                    temp_trophies[i], temp_trophies[j] = temp_trophies[j], temp_trophies[i]
                    temp_golden_indices = [k for k in range(n) if temp_trophies[k] == 'G']
                    temp_max_length = 0

                    for k in range(len(temp_golden_indices)):
                        for l in range(k + 1, len(temp_golden_indices)):
                            if temp_golden_indices[l] - temp_golden_indices[k] - 1 == l - k - 1:
                                temp_max_length = max(temp_max_length, temp_golden_indices[l] - temp_golden_indices[k] + 1)

                    max_length = max(max_length, temp_max_length)

    return max_length

n = int(input())
trophies = input()
print(max_beauty(n, trophies))