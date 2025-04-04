def calculate_days_off(n):
    if n < 0:
        raise ValueError("Number of days cannot be negative.")
    
    # Calculate maximum possible days off
    max_days_off = min(2, n)

    # Calculate minimum possible days off
    weeks = n // 7
    remaining_days = n % 7

    # Minimum days off will be 2 for each complete week, plus depending on remaining days
    min_days_off = weeks * 2 + max(0, remaining_days - 5)

    return min_days_off, max_days_off

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of days: "))
        min_days_off, max_days_off = calculate_days_off(n)
        print(min_days_off, max_days_off)
    except ValueError as e:
        print(f"Invalid input: {e}")