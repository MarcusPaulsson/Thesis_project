x = float(input().strip())

for a in range(1, 11):
    for b in range(1, 11):
        if abs(a**b - x) < 1e-6:
            print(a, b)
            break