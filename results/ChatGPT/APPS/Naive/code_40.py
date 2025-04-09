def determine_round_status(n, ratings):
    # Check if any rating has changed
    rated = any(a != b for a, b in ratings)
    if rated:
        return "rated"

    # Check for the order of participants
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            return "unrated"

    return "maybe"

def main():
    n = int(input())
    ratings = [tuple(map(int, input().split())) for _ in range(n)]
    result = determine_round_status(n, ratings)
    print(result)

if __name__ == "__main__":
    main()