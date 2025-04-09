def is_palindrome(time_str):
    return time_str == time_str[::-1]

def next_palindrome_time(hh, mm):
    minutes_passed = 0
    while True:
        if is_palindrome(f"{hh:02}:{mm:02}"):
            return minutes_passed
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        minutes_passed += 1

def main():
    current_time = input().strip()
    hh, mm = map(int, current_time.split(':'))
    print(next_palindrome_time(hh, mm))

if __name__ == "__main__":
    main()