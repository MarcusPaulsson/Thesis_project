def lexicographically_minimal_string(s: str) -> str:
    t = []  # Stack to hold characters from s
    u = []  # Result string as a list of characters
    s = list(s)  # Convert string to a list for efficient operations

    while s or t:
        # While there are characters in s, we compare and move characters
        while s and (not t or s[0] <= t[-1]):
            t.append(s.pop(0))  # Move character from s to t

        if t:
            u.append(t.pop())  # Move character from t to u

    return ''.join(u)  # Join list u into a string and return

# Input and output handling
if __name__ == "__main__":
    s = input().strip()
    result = lexicographically_minimal_string(s)
    print(result)