def determine_round_status(n, ratings):
    for a, b in ratings:
        if a != b:
            return "rated"
    
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            return "unrated"
    
    return "maybe"

if __name__ == "__main__":
    n = int(input().strip())
    ratings = [tuple(map(int, input().strip().split())) for _ in range(n)]
    result = determine_round_status(n, ratings)
    print(result)