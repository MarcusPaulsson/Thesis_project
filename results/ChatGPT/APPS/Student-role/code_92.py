def can_transform(s, t):
    return set(s) & set(t) != set()

def main():
    q = int(input())
    for _ in range(q):
        s = input().strip()
        t = input().strip()
        if can_transform(s, t):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()