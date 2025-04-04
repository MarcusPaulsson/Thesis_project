def min_replacements(ticket):
    first_half = ticket[:3]
    second_half = ticket[3:]
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    return abs(sum_first_half - sum_second_half) // 9

# Input
ticket = input()

# Output
print(min_replacements(ticket))