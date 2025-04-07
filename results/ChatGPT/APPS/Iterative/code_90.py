n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Check if we can reach n + 1 directly
if d >= n + 1:
    print("YES")
    print("0 " + " ".join(str(1) for _ in range(n)) + " 2")
else:
    # Create the answer array filled with zeros
    answer = [0] * n
    current_position = 0

    for i in range(m):
        # Place the platform at the current position
        answer[current_position:current_position + c[i]] = [i + 1] * c[i]
        current_position += c[i]

        # Check if we can jump from the last position of the last platform to n + 1
        if current_position - 1 + d >= n + 1:
            break

        # Move to the next platform position with at least d gap if it's not the last platform
        if i < m - 1:
            current_position += d

    # Final check to see if we can reach to n + 1
    if current_position - 1 + d < n + 1:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, answer)))