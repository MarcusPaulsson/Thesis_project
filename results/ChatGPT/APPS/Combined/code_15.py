def is_favorite_in_sequence(a, b, c):
    if c == 0:
        return a == b
    return (b - a) % c == 0 and (b - a) // c >= 0

def main():
    a, b, c = map(int, input().split())
    result = "YES" if is_favorite_in_sequence(a, b, c) else "NO"
    print(result)

if __name__ == "__main__":
    main()