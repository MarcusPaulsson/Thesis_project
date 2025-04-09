def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    q = [(n, 0)]
    visited = {n}

    while q:
        curr, moves = q.pop(0)

        if curr == m:
            print(moves)
            return

        next_vals = [curr * 2, curr * 3]

        for next_val in next_vals:
            if next_val <= m and next_val not in visited:
                q.append((next_val, moves + 1))
                visited.add(next_val)

    print(-1)

solve()