def find_number(n):
    if n == 1:
        return -1  # No single digit number satisfies the condition
    else:
        # Create a number with n digits, all digits are > 0 and none are divisible by themselves
        # For example, using digits from 2 to 9 can help avoid divisibility.
        # Using a pattern like 23, 24, 25, ..., to ensure that the number is not divisible by any of its digits.
        return ''.join(str((i % 9) + 1) for i in range(n))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        results.append(find_number(n))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()