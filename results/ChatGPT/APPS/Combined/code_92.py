def find_integers(x):
    for a in range(1, 11):
        for b in range(1, 11):
            if abs(a * b - x) < 1e-6:
                return a, b

if __name__ == "__main__":
    x = float(input().strip())
    result = find_integers(x)
    print(result[0], result[1])