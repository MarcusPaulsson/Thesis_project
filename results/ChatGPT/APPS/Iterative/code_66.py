def construct_string(n, k, t):
    # Use KMP (Knuth-Morris-Pratt) failure function to find the longest prefix which is also a suffix
    pi = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j

    # The length of the longest prefix which is also a suffix
    overlap_length = pi[-1]

    # Construct the final string
    non_overlapping_part = t[overlap_length:]
    result = t + non_overlapping_part * (k - 1)

    return result

def main():
    # Read input
    n, k = map(int, input().split())
    t = input().strip()

    # Validate input
    if n <= 0 or k <= 0 or len(t) != n:
        raise ValueError("Invalid input: n and k must be positive integers and the length of t must equal n.")

    # Get the constructed string
    result = construct_string(n, k, t)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()