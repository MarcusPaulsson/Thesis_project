try:
    x = float(input().strip())
    a = (int(x * 10) % 10) + 1
    b = (int(x * 100) % 10) + 1
    print(a, b)
except ValueError:
    print("Invalid input. Please enter a valid number.")