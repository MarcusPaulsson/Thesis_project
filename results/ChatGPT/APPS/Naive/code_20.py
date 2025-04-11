def is_palindrome(time_str):
    return time_str == time_str[::-1]

def next_palindrome_time(hh, mm):
    minutes_passed = 0
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes_passed += 1
        time_str = f"{hh:02}:{mm:02}"
        if is_palindrome(time_str):
            return minutes_passed

def main():
    current_time = input().strip()
    hh, mm = map(int, current_time.split(':'))
    result = next_palindrome_time(hh, mm)
    print(result)

if __name__ == "__main__":
    main()