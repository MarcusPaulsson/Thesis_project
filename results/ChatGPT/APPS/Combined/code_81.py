def can_reorder_strings(strings):
    # Sort strings by their lengths
    strings.sort(key=len)

    # Check if the ordering is valid
    for i in range(1, len(strings)):
        # Check if the previous string is a substring of the current string
        if strings[i - 1] not in strings[i]:
            return False, []

    return True, strings

def main():
    n = int(input().strip())
    strings = [input().strip() for _ in range(n)]
    
    is_possible, ordered_strings = can_reorder_strings(strings)

    if is_possible:
        print("YES")
        print("\n".join(ordered_strings))
    else:
        print("NO")

if __name__ == "__main__":
    main()