def min_operations(a, b, c):
    min_ops = float('inf')
    best_triple = (0, 0, 0)
    
    for A in range(1, a + 1):
        for B in range(A, c + 1):
            if B % A == 0:  # B must be divisible by A
                for C in range(B, c + 1):
                    if C % B == 0:  # C must be divisible by B
                        ops = abs(a - A) + abs(b - B) + abs(c - C)
                        if ops < min_ops:
                            min_ops = ops
                            best_triple = (A, B, C)

    return min_ops, best_triple

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    operations, (A, B, C) = min_operations(a, b, c)
    print(operations)
    print(A, B, C)