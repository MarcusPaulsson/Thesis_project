def can_reorder_strings(strings):
    # Step 1: Sort strings by length
    strings.sort(key=len)
    
    # Step 2: Check if each string is a substring of the next one
    for i in range(len(strings) - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"
    
    # Step 3: If all checks passed, return the ordered strings
    return "YES", strings

def main():
    # Input reading
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    # Get the result
    result = can_reorder_strings(strings)

    # Output the result
    if result == "NO":
        print(result)
    else:
        print(result[0])
        print("\n".join(result[1]))

if __name__ == "__main__":
    main()