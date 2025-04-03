def solve():
    n = int(input())
    p = list(map(int, input().split()))

    best_seq = []
    max_sum = -1

    for i in range(1 << n):
        seq = []
        for j in range(n):
            if (i >> j) & 1:
                seq.append(p[j])

        if len(seq) < 2:
            continue

        current_sum = 0
        for j in range(len(seq) - 1):
            current_sum += abs(seq[j] - seq[j+1])

        if current_sum > max_sum:
            max_sum = current_sum
            best_seq = seq
        elif current_sum == max_sum:
            if len(seq) < len(best_seq):
                best_seq = seq

    print(len(best_seq))
    print(*best_seq)


t = int(input())
for _ in range(t):
    solve()