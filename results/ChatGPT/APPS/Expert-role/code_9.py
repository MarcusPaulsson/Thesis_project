def alice_score(s):
    score = 0
    count_ones = 0
    current_char = ''
    
    for char in s:
        if char == '1':
            count_ones += 1
        else:
            if count_ones > 0:
                score += (count_ones + 1) // 2  # Alice takes half (rounded up) of the 1s
                count_ones = 0

    if count_ones > 0:
        score += (count_ones + 1) // 2  # Final segment of 1s

    return score

def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        s = input().strip()
        results.append(alice_score(s))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()