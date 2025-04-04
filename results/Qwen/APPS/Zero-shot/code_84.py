def can_be_sorted_by_swaps(s):
    n = len(s)
    color = [0] * n
    for i in range(1, n):
        if s[i] < s[i - 1]:
            color[i] = 1
    return color

def main():
    n = int(input())
    s = input()
    color = can_be_sorted_by_swaps(s)
    if color == "NO":
        print("NO")
    else:
        print("YES")
        print("".join(map(str, color)))

if __name__ == "__main__":
    main()