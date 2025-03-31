def calculate_largest_product(numbers):
    if len(numbers) < 2:
        return None
    largest1 = max(numbers)
    numbers.remove(largest1)
    largest2 = max(numbers)
    return largest1 * largest2